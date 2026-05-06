/* List view + graph↔list sync — Phase 5.
 *
 * Renders a card grid below the graph, sourced from the current
 * filteredNodeIds (Set in the shared store). On the EFL dataset the
 * list always shows a meaningful subset because Cytoscape DIMS rather
 * than removes filtered-out nodes; the list is the canonical "what's
 * in scope right now" view, the graph is the topology.
 *
 * Bidirectional sync:
 *   - Hover a card → store.hovered = nodeId → graph.js highlights the
 *     matching node.
 *   - Hover a node (in graph.js) → store.hovered = nodeId → this list
 *     scrolls the matching card into view.
 *   - Click pres/ws card → triggers download via the <a download>.
 *   - Click article card → navigates.
 */

const TOPIC_LABELS = {
  themen: "Themen",
  interkulturell: "Interkulturell",
  "text-medien": "Text & Medien",
};

const TYPE_GLYPH = { article: "●", presentation: "▪", worksheet: "◆" };
const TYPE_LABEL = { article: "Article", presentation: "Slides", worksheet: "Worksheet" };

const COURSE_LABEL = (id) => {
  const m = (id || "").match(/^track-(e|gm)\/kl(\d{2})$/);
  if (!m) return id;
  return `Track ${m[1] === "gm" ? "G+M" : "E"} · Klasse ${parseInt(m[2], 10)}`;
};

const ARTICLE_PAGE_SIZE = 60;

export class List {
  constructor(container, graphData, store) {
    this.container = container;
    this.data = graphData;
    this.store = store;
    this.cardsByNode = new Map();
    store.subscribe((s) => this._onState(s));
  }

  hydrate() {
    this._render(this.store.get());
  }

  _onState(s) {
    this._render(s);
    this._applyHover(s.hovered);
  }

  _render(s) {
    const filtered = s.filteredNodeIds;
    // Group: one card per article, rolling up its pres/ws as type chips.
    const articles = [];
    for (const n of this.data.nodes) {
      if (n.type !== "article") continue;
      if (!filtered.has(n.id)) continue;
      articles.push(n);
    }
    articles.sort((a, b) => a.title.localeCompare(b.title));

    const html = [];
    if (articles.length === 0) {
      html.push(this._emptyState(s));
    } else {
      const shown = articles.slice(0, ARTICLE_PAGE_SIZE);
      for (const a of shown) {
        const presId = a.related && a.related[0];
        const wsId   = a.related && a.related[1];
        const pres = presId && this.data.nodes.find((n) => n.id === presId);
        const ws   = wsId   && this.data.nodes.find((n) => n.id === wsId);
        const presIn = pres && filtered.has(pres.id);
        const wsIn   = ws   && filtered.has(ws.id);

        html.push(`<li class="network-card network-card--article" data-node-id="${escapeAttr(a.id)}" style="--topic: var(--topic-${a.topic || 'themen'})">`);
        html.push(`  <div class="network-card-header">`);
        html.push(`    <h3 class="network-card-title"><a href="${escapeAttr(a.url)}">${escapeHtml(a.title)}</a></h3>`);
        html.push(`    <span class="network-card-meta">${escapeHtml(COURSE_LABEL(a.course))} · ${escapeHtml(TOPIC_LABELS[a.topic] || a.topic || '')}</span>`);
        html.push(`  </div>`);
        if (a.tags && a.tags.length) {
          html.push(`  <ul class="network-card-tags">${a.tags.slice(0, 6).map((t) => `<li>${escapeHtml(t)}</li>`).join("")}</ul>`);
        }
        html.push(`  <div class="network-card-types">`);
        html.push(`    <span class="glyph-article">${TYPE_GLYPH.article}</span><span>${TYPE_LABEL.article}</span>`);
        if (presIn && pres.url) {
          html.push(`    <a class="glyph-presentation" href="${escapeAttr(pres.url)}" download data-node-id="${escapeAttr(pres.id)}">${TYPE_GLYPH.presentation}<span class="visually-hidden"> presentation</span></a>`);
        }
        if (wsIn && ws.url) {
          html.push(`    <a class="glyph-worksheet" href="${escapeAttr(ws.url)}" download data-node-id="${escapeAttr(ws.id)}">${TYPE_GLYPH.worksheet}<span class="visually-hidden"> worksheet</span></a>`);
        }
        html.push(`  </div>`);
        html.push(`</li>`);
      }
      if (articles.length > shown.length) {
        html.push(`<li class="network-card" style="grid-column: span 3; text-align:center; color:var(--network-text-meta)">+${articles.length - shown.length} more match. Refine filters or search to narrow.</li>`);
      }
    }

    this.container.innerHTML = html.join("");
    this.cardsByNode.clear();
    this.container.querySelectorAll("li[data-node-id]").forEach((li) => {
      this.cardsByNode.set(li.dataset.nodeId, li);
      li.addEventListener("mouseenter", () => this.store.set({ hovered: li.dataset.nodeId }));
      li.addEventListener("mouseleave", () => this.store.set({ hovered: null }));
    });
  }

  _applyHover(nodeId) {
    this.cardsByNode.forEach((li, id) => {
      li.classList.toggle("hovered", id === nodeId);
    });
    if (nodeId) {
      const li = this.cardsByNode.get(nodeId);
      if (li && this._shouldScroll(li)) {
        li.scrollIntoView({ behavior: "smooth", block: "nearest" });
      }
    }
  }

  _shouldScroll(li) {
    const rect = li.getBoundingClientRect();
    return rect.top < 100 || rect.bottom > window.innerHeight - 60;
  }

  _emptyState(s) {
    const facetCount =
      s.facets.type.size + s.facets.course.size +
      s.facets.topic.size + s.facets.tags.size;
    return `
      <li style="grid-column: 1 / -1">
        <div class="network-empty">
          <svg width="96" height="96" viewBox="0 0 96 96" fill="none" aria-hidden="true">
            <circle cx="40" cy="40" r="20" stroke="currentColor" stroke-width="2"/>
            <line x1="55" y1="55" x2="80" y2="80" stroke="currentColor" stroke-width="3" stroke-linecap="round"/>
            <line x1="32" y1="40" x2="48" y2="40" stroke="currentColor" stroke-width="1.5"/>
            <line x1="40" y1="32" x2="40" y2="48" stroke="currentColor" stroke-width="1.5"/>
          </svg>
          <p>No materials match the current filters${s.query ? ` and search “${escapeHtml(s.query)}”` : ""}.</p>
          ${facetCount > 0 ? `<p style="font-size:0.875rem">Try removing one of the ${facetCount} active filter${facetCount === 1 ? "" : "s"}, or hit <kbd>Reset all</kbd>.</p>` : ""}
        </div>
      </li>`;
  }
}

function escapeHtml(s) {
  return String(s)
    .replace(/&/g, "&amp;").replace(/</g, "&lt;")
    .replace(/>/g, "&gt;").replace(/"/g, "&quot;");
}
function escapeAttr(s) { return String(s).replace(/"/g, "&quot;"); }
