/* Materials Discovery Network — entry module.
 *
 * Loads graph.json, creates a shared store, mounts the Cytoscape graph
 * (desktop only) and the filter rail, and wires their state together.
 *
 * Phases shipped here:
 *   - Phase 3: graph rendering (NetworkGraph in graph.js).
 *   - Phase 4: filter rail with live counts + URL state (Filters in filters.js).
 *
 * Mobile (<768px): graph DOM is hidden by CSS, the JS payload itself
 * bails before importing Cytoscape's runtime (graph never instantiates).
 * The page falls through to the always-rendered <nav class="network-fallback">.
 */
import { NetworkGraph } from "./graph.js";
import { Filters } from "./filters.js";
import { createStore, emptyState } from "./store.js";

async function loadGraphData() {
  const url = `${document.documentElement.dataset.basePath || ""}/materials/graph.json`;
  const res = await fetch(url, { credentials: "same-origin" });
  if (!res.ok) throw new Error(`graph.json: HTTP ${res.status}`);
  return res.json();
}

async function init() {
  const container = document.getElementById("network-graph");
  if (!container) return;

  const isDesktop = window.matchMedia("(min-width: 768px)").matches;

  let data;
  try {
    data = await loadGraphData();
  } catch (err) {
    console.error("[network] graph.json load failed:", err);
    container.innerHTML =
      '<div class="network-graph-skeleton">Could not load network. ' +
      'Use the list below to browse materials.</div>';
    return;
  }

  const store = createStore(emptyState(data));

  // Mount filter rail (works on desktop + tablet, even when graph hidden).
  const rail = document.getElementById("network-rail");
  let filters = null;
  if (rail) {
    filters = new Filters(rail, data, store);
    filters.hydrate();
  }

  // Desktop only: instantiate Cytoscape and bridge filter state.
  let graph = null;
  if (isDesktop) {
    graph = new NetworkGraph(container, data);
    await graph.render();
    store.subscribe((s) => {
      graph.applyFilter((node) => s.filteredNodeIds.has(node.id));
    });
    // Apply initial filter state (URL-derived).
    graph.applyFilter((node) => store.get().filteredNodeIds.has(node.id));
  } else {
    // Mobile: hide the loading skeleton placeholder; the DOM-nav is the UI.
    container.innerHTML = "";
  }

  window.__efl_network = { graph, filters, store, data };
}

if (document.readyState === "loading") {
  document.addEventListener("DOMContentLoaded", init);
} else {
  init();
}
