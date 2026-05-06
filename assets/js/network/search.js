/* Search — Phase 5.
 *
 * Wires the page's search input to Pagefind's runtime API and to the
 * shared store. Pagefind itself is loaded on first keystroke (lazy) so
 * the initial bundle stays slim. Result URLs become a Set; the store's
 * filteredNodeIds is intersected with that Set on the next recompute.
 *
 * Phase 0 §C1 keeps a single-line search; the prompt's compound facet
 * vocabulary (e.g. tag:foo course:klasse-7) is out of scope for this
 * phase but the Filters module handles those dimensions natively.
 */

const DEBOUNCE_MS = 80;

export class Search {
  constructor(input, store, graphData, filters) {
    this.input = input;
    this.store = store;
    this.data = graphData;
    this.filters = filters;
    this._pf = null;
    this._lastQuery = "";
    this._timer = null;
  }

  hydrate() {
    // Restore the query from URL state (already in the store after
    // Filters.hydrate ran).
    const q = this.store.get().query || "";
    if (q) this.input.value = q;
    this._wire();
    if (q) this._runSearch(q);
  }

  _wire() {
    this.input.addEventListener("input", () => {
      clearTimeout(this._timer);
      const q = this.input.value;
      this._timer = setTimeout(() => this._runSearch(q), DEBOUNCE_MS);
    });
    document.addEventListener("keydown", (e) => {
      if (e.key === "/" && !this._isTyping(e.target)) {
        e.preventDefault();
        this.input.focus();
      } else if (e.key === "Escape" && document.activeElement === this.input) {
        this.input.value = "";
        this._runSearch("");
        this.input.blur();
      }
    });
  }

  _isTyping(el) {
    if (!el) return false;
    const tag = (el.tagName || "").toLowerCase();
    return tag === "input" || tag === "textarea" || el.isContentEditable;
  }

  async _ensurePagefind() {
    if (this._pf) return this._pf;
    try {
      const url = `${document.documentElement.dataset.basePath || ""}/pagefind/pagefind.js`;
      const mod = await import(/* @vite-ignore */ url);
      this._pf = mod;
      if (mod.options) await mod.options({ excerptLength: 24 });
      return mod;
    } catch (err) {
      console.warn("[search] pagefind not available:", err);
      this._pf = null;
      return null;
    }
  }

  async _runSearch(q) {
    q = (q || "").trim();
    if (q === this._lastQuery) return;
    this._lastQuery = q;
    const s = this.store.get();
    this.store.set({ query: q, searchUrls: q ? null : null });

    if (!q) {
      this.store.set({ searchUrls: null });
      this.filters.recompute();
      return;
    }

    const pf = await this._ensurePagefind();
    if (!pf) {
      // Fall back to client-side substring on title/description.
      const ql = q.toLowerCase();
      const matched = new Set();
      for (const n of this.data.nodes) {
        if (n.type !== "article") continue;
        if ((n.title || "").toLowerCase().includes(ql) ||
            (n.description || "").toLowerCase().includes(ql)) {
          matched.add(n.url);
        }
      }
      this.store.set({ searchUrls: matched });
      this.filters.recompute();
      return;
    }

    try {
      const result = await pf.search(q);
      const urls = new Set();
      for (const r of result.results) {
        const data = await r.data();
        if (data && data.url) urls.add(data.url);
      }
      this.store.set({ searchUrls: urls });
    } catch (err) {
      console.warn("[search] query failed:", err);
      this.store.set({ searchUrls: new Set() });
    }
    this.filters.recompute();
  }
}

/**
 * Wire search results into the filter pipeline. Filters.recompute() now
 * intersects with searchUrls (when set). This is called by main.js right
 * after Filters is constructed.
 */
export function patchFiltersForSearch(filters) {
  const baseRecompute = filters.recompute.bind(filters);
  filters.recompute = function () {
    const s = filters.store.get();
    const ids = new Set();
    const urls = s.searchUrls;
    for (const n of filters.data.nodes) {
      if (!filterPasses(filters, n, s)) continue;
      if (urls && !matchesSearch(n, urls, filters.data)) continue;
      ids.add(n.id);
    }
    filters.store.set({ filteredNodeIds: ids });
    // URL state is unchanged for query (Filters already manages it).
    if (typeof filters.writeUrlState === "function") filters.writeUrlState();
    else writeUrlStatePassthrough(filters.store.get());
  };
}

// Local copies of the gating helpers so search.js doesn't import
// internals from filters.js. This keeps the patch self-contained.
function filterPasses(filters, node, state) {
  const f = state.facets;
  if (f.type.size && !f.type.has(node.type)) return false;
  if (f.course.size && !f.course.has(node.course)) return false;
  if (f.topic.size && !f.topic.has(node.topic)) return false;
  if (f.tags.size) {
    if (!node.tags || !node.tags.some((t) => f.tags.has(t))) return false;
  }
  return true;
}
function matchesSearch(node, urls, data) {
  if (node.type === "article") return urls.has(node.url);
  // pres/ws inherit their parent article's match.
  const parent = data.nodes.find((n) => n.id === node.parent_article);
  return parent && urls.has(parent.url);
}
function writeUrlStatePassthrough(state) {
  const params = new URLSearchParams();
  if (state.facets.type.size)   params.set("type", [...state.facets.type].join(","));
  if (state.facets.course.size) params.set("course", [...state.facets.course].join(","));
  if (state.facets.topic.size)  params.set("topic", [...state.facets.topic].join(","));
  if (state.facets.tags.size)   params.set("tags", [...state.facets.tags].join(","));
  if (state.query) params.set("q", state.query);
  const qs = params.toString();
  const url = qs ? `${window.location.pathname}?${qs}` : window.location.pathname;
  window.history.replaceState(null, "", url);
}
