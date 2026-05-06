/* Materials Discovery Network — entry module.
 *
 * Loads graph.json, creates a shared store, mounts:
 *   - the Cytoscape graph (desktop only)
 *   - the filter rail
 *   - the search box
 *   - the list view
 * and wires their state together via a single store.
 *
 * Phases shipped:
 *   - Phase 3: graph rendering (NetworkGraph in graph.js).
 *   - Phase 4: filter rail with live counts + URL state (Filters).
 *   - Phase 5: Pagefind search + list view + bidirectional hover sync
 *              (Search, List).
 *
 * Mobile (<768px): Cytoscape is not instantiated, but filters + search
 * + list still work over the DOM. The search index is the same Pagefind
 * artefact regardless of viewport.
 */
import { NetworkGraph } from "./graph.js";
import { Filters } from "./filters.js";
import { Search, patchFiltersForSearch } from "./search.js";
import { List } from "./list.js";
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

  // Filter rail (works on desktop + tablet + mobile).
  const rail = document.getElementById("network-rail");
  let filters = null;
  if (rail) {
    filters = new Filters(rail, data, store);
    patchFiltersForSearch(filters);
    filters.hydrate();
  }

  // Search input (above or beside the graph).
  const searchInput = document.getElementById("network-search-input");
  if (searchInput && filters) {
    const search = new Search(searchInput, store, data, filters);
    search.hydrate();
  }

  // List view (always visible — it's the canonical filtered subset).
  const listEl = document.getElementById("network-list");
  let list = null;
  if (listEl) {
    list = new List(listEl, data, store);
    list.hydrate();
  }

  // Desktop: instantiate Cytoscape and bridge filter+hover state.
  let graph = null;
  if (isDesktop) {
    graph = new NetworkGraph(container, data);
    await graph.render();
    // Filter changes -> dim non-matching nodes.
    store.subscribe((s) => {
      graph.applyFilter((node) => s.filteredNodeIds.has(node.id));
    });
    graph.applyFilter((node) => store.get().filteredNodeIds.has(node.id));

    // Graph hover -> store, so the list highlights/scrolls.
    graph.cy.on("mouseover", "node", (e) => {
      store.set({ hovered: e.target.id() });
    });
    graph.cy.on("mouseout", "node", () => {
      store.set({ hovered: null });
    });
    // Store hover -> graph highlight (when triggered by list hover).
    store.subscribe((s) => {
      graph.cy.batch(() => {
        graph.cy.nodes().removeClass("hovered");
        if (s.hovered) {
          const n = graph.cy.getElementById(s.hovered);
          if (n) n.addClass("hovered");
        }
      });
    });
  } else {
    container.innerHTML = "";
  }

  window.__efl_network = { graph, filters, list, store, data };
}

if (document.readyState === "loading") {
  document.addEventListener("DOMContentLoaded", init);
} else {
  init();
}
