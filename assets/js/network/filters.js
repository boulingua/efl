/* Filter rail with live counts + URL state — Phase 4.
 *
 * Renders four facet groups (type / course / topic / tags) into the rail
 * container. Date facet dropped per Phase 0 §C1 (no date frontmatter on
 * this site). Within a facet: OR. Across facets: AND.
 *
 * Counts are "other-facets-fixed": each chip shows how many items would
 * remain if that chip were the only one toggled in its own facet, holding
 * all other facets at their current state. This lets the user see what
 * adding/removing the chip would do without exploring blindly.
 *
 * URL state is mirrored on every change via history.replaceState. On
 * page load, the current URL is parsed once and applied before first
 * paint, so there's no flash of unfiltered content.
 */

const URL_KEYS = {
  type: "type",
  course: "course",
  topic: "topic",
  tags: "tags",
  query: "q",
};

/** Parse the current URL query string into a facet state patch. */
export function readUrlState(graphData) {
  const params = new URLSearchParams(window.location.search);
  const facets = {
    type:   new Set(),
    course: new Set(),
    topic:  new Set(),
    tags:   new Set(),
  };
  for (const [stateKey, urlKey] of Object.entries(URL_KEYS)) {
    if (stateKey === "query") continue;
    const v = params.get(urlKey);
    if (v) v.split(",").filter(Boolean).forEach((x) => facets[stateKey].add(x));
  }
  return { facets, query: params.get(URL_KEYS.query) || "" };
}

/** Write the current state back to the URL (via replaceState). */
function writeUrlState(state) {
  const params = new URLSearchParams();
  for (const [stateKey, urlKey] of Object.entries(URL_KEYS)) {
    if (stateKey === "query") {
      if (state.query) params.set(urlKey, state.query);
      continue;
    }
    const set = state.facets[stateKey];
    if (set.size) params.set(urlKey, [...set].join(","));
  }
  const qs = params.toString();
  const url = qs ? `${window.location.pathname}?${qs}` : window.location.pathname;
  window.history.replaceState(null, "", url);
}

/**
 * Decide whether a node passes the active facets.
 * - Skips a facet's check if its set is empty (means "no filter").
 * - Within a facet: OR (set membership).
 * - Across facets: AND (every facet must pass).
 */
export function nodePasses(node, facets) {
  if (facets.type.size  && !facets.type.has(node.type))   return false;
  if (facets.course.size && !facets.course.has(node.course)) return false;
  if (facets.topic.size && !facets.topic.has(node.topic))  return false;
  if (facets.tags.size) {
    if (!node.tags || !node.tags.some((t) => facets.tags.has(t))) return false;
  }
  return true;
}

/** Compute how many nodes would match if the given chip were on, holding
 *  all OTHER facets at their current state. */
function countFor(graphData, facets, facetKey, chipValue) {
  const probe = {
    type: facetKey === "type"
      ? new Set([chipValue])
      : facets.type,
    course: facetKey === "course"
      ? new Set([chipValue])
      : facets.course,
    topic: facetKey === "topic"
      ? new Set([chipValue])
      : facets.topic,
    tags: facetKey === "tags"
      ? new Set([chipValue])
      : facets.tags,
  };
  let n = 0;
  for (const node of graphData.nodes) {
    if (nodePasses(node, probe)) n++;
  }
  return n;
}

const COURSE_LABEL = (id) => {
  const m = id.match(/^track-(e|gm)\/kl(\d{2})$/);
  if (!m) return id;
  return `${m[1] === "gm" ? "G+M" : "E"} · Klasse ${parseInt(m[2], 10)}`;
};
const TYPE_LABEL = { article: "● Article", presentation: "▪ Presentation", worksheet: "◆ Worksheet" };
const TYPE_ORDER = ["article", "presentation", "worksheet"];
const COURSE_ORDER = (a, b) => a.id.localeCompare(b.id);

const TAG_TOP_N = 15;

export class Filters {
  constructor(rail, graphData, store) {
    this.rail = rail;
    this.data = graphData;
    this.store = store;
    this.tagsExpanded = false;
    store.subscribe(() => this.render());
  }

  /** Read URL on init, write to store, render. */
  hydrate() {
    const { facets, query } = readUrlState(this.data);
    this.store.set({ facets, query });
    this.recompute();
  }

  /** Recompute filteredNodeIds + sync URL. */
  recompute() {
    const s = this.store.get();
    const ids = new Set();
    for (const n of this.data.nodes) {
      if (nodePasses(n, s.facets)) ids.add(n.id);
    }
    this.store.set({ filteredNodeIds: ids });
    writeUrlState(this.store.get());
  }

  toggleChip(facetKey, value) {
    const s = this.store.get();
    const set = new Set(s.facets[facetKey]);
    if (set.has(value)) set.delete(value);
    else set.add(value);
    this.store.set({ facets: { ...s.facets, [facetKey]: set } });
    this.recompute();
  }

  reset() {
    this.store.set({
      facets: {
        type:   new Set(),
        course: new Set(),
        topic:  new Set(),
        tags:   new Set(),
      },
      query: "",
    });
    this.recompute();
  }

  render() {
    const s = this.store.get();
    const { facets } = s;
    const html = [];

    // Type facet.
    html.push('<div class="network-facet"><h3>Type</h3><div class="network-chip-row">');
    for (const t of TYPE_ORDER) {
      const count = countFor(this.data, facets, "type", t);
      const on = facets.type.has(t);
      html.push(this._chip("type", t, TYPE_LABEL[t], count, on));
    }
    html.push("</div></div>");

    // Topic facet (with swatches).
    html.push('<div class="network-facet"><h3>Topic</h3><div class="network-chip-row">');
    for (const t of this.data.facets.topics) {
      const count = countFor(this.data, facets, "topic", t.id);
      const on = facets.topic.has(t.id);
      html.push(this._chip(
        "topic", t.id,
        `<span class="swatch" style="background:var(--topic-${t.id})"></span> ${escapeHtml(t.label_en)}`,
        count, on
      ));
    }
    html.push("</div></div>");

    // Course facet.
    html.push('<div class="network-facet"><h3>Course</h3><div class="network-chip-row">');
    for (const c of [...this.data.facets.courses].sort(COURSE_ORDER)) {
      const count = countFor(this.data, facets, "course", c.id);
      const on = facets.course.has(c.id);
      html.push(this._chip("course", c.id, escapeHtml(COURSE_LABEL(c.id)), count, on));
    }
    html.push("</div></div>");

    // Tags facet — top N + expand link.
    const tagsSorted = [...this.data.facets.tags].sort((a, b) => b.count - a.count);
    const tagsShown = this.tagsExpanded ? tagsSorted : tagsSorted.slice(0, TAG_TOP_N);
    html.push(
      `<div class="network-facet"><h3>Tags <span class="count" style="text-transform:none;letter-spacing:normal">${this.tagsExpanded ? tagsSorted.length : `top ${Math.min(TAG_TOP_N, tagsSorted.length)} of ${tagsSorted.length}`}</span></h3><div class="network-chip-row">`
    );
    for (const t of tagsShown) {
      const count = countFor(this.data, facets, "tags", t.id);
      const on = facets.tags.has(t.id);
      html.push(this._chip("tags", t.id, escapeHtml(t.id), count, on));
    }
    if (tagsSorted.length > TAG_TOP_N) {
      html.push(
        `<button class="network-chip" data-action="toggle-tags">${this.tagsExpanded ? "Show top 15" : `Show all ${tagsSorted.length}`}</button>`
      );
    }
    html.push("</div></div>");

    // Reset.
    const anyActive = facets.type.size + facets.course.size + facets.topic.size + facets.tags.size + (s.query ? 1 : 0) > 0;
    html.push(
      `<button class="network-chip" data-action="reset" ${anyActive ? '' : 'disabled style="opacity:0.4;cursor:default"'}>Reset all</button>`
    );

    this.rail.innerHTML = html.join("");
    this._wire();

    // Update the visible status line (shared with main.js).
    this._updateStatus();
  }

  _chip(facetKey, value, label, count, pressed) {
    const disabled = count === 0 && !pressed;
    return (
      `<button class="network-chip" type="button"` +
      ` aria-pressed="${pressed}"` +
      ` data-facet="${facetKey}" data-value="${escapeAttr(value)}"` +
      (disabled ? ' disabled style="opacity:0.5;cursor:default"' : '') +
      `>${label} <span class="count">${count}</span></button>`
    );
  }

  _wire() {
    this.rail.querySelectorAll("button[data-facet]").forEach((btn) => {
      btn.addEventListener("click", () => {
        if (btn.disabled) return;
        this.toggleChip(btn.dataset.facet, btn.dataset.value);
      });
    });
    const reset = this.rail.querySelector('button[data-action="reset"]');
    if (reset) reset.addEventListener("click", () => this.reset());
    const toggle = this.rail.querySelector('button[data-action="toggle-tags"]');
    if (toggle) toggle.addEventListener("click", () => {
      this.tagsExpanded = !this.tagsExpanded;
      this.render();
    });
  }

  _updateStatus() {
    const status = document.getElementById("network-status-text");
    if (!status) return;
    const s = this.store.get();
    const total = this.data.nodes.length;
    const visible = s.filteredNodeIds.size;
    const facetCount =
      s.facets.type.size + s.facets.course.size +
      s.facets.topic.size + s.facets.tags.size;
    status.textContent =
      facetCount === 0 && !s.query
        ? `${total} items · no filters`
        : `${visible} of ${total} items shown · ${facetCount} filter${facetCount === 1 ? "" : "s"} active`;
  }
}

function escapeHtml(s) {
  return String(s)
    .replace(/&/g, "&amp;")
    .replace(/</g, "&lt;")
    .replace(/>/g, "&gt;")
    .replace(/"/g, "&quot;");
}
function escapeAttr(s) {
  return String(s).replace(/"/g, "&quot;");
}
