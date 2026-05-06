/* Materials Discovery Network — entry module.
 *
 * Loads graph.json, mounts the Cytoscape graph (desktop only — mobile
 * gets the DOM accessibility nav and skips the JS payload entirely
 * via a viewport check before this module is even imported).
 *
 * Phase 3 of the network: graph rendering only. Filters, search, and
 * list-sync land in Phases 4 and 5. The exports below are what those
 * later modules will consume.
 */
import { NetworkGraph } from "./graph.js";

async function loadGraphData() {
  const url = `${document.documentElement.dataset.basePath || ""}/materials/graph.json`;
  const res = await fetch(url, { credentials: "same-origin" });
  if (!res.ok) {
    throw new Error(`graph.json: HTTP ${res.status}`);
  }
  return res.json();
}

async function init() {
  const container = document.getElementById("network-graph");
  if (!container) return;

  // Below 768px the markup hides the graph via CSS and the page
  // delegates to the DOM-nav. We still don't want to fetch graph.json
  // there, since the JSON is ~400KB on the EFL dataset.
  if (!window.matchMedia("(min-width: 768px)").matches) return;

  try {
    const data = await loadGraphData();
    const graph = new NetworkGraph(container, data);
    await graph.render();
    // Park the instance on window for Phase 4+ to grab.
    window.__efl_network = { graph, data };
  } catch (err) {
    console.error("[network] init failed:", err);
    container.innerHTML =
      '<div class="network-graph-skeleton">Could not load network. ' +
      'Use the list below to browse materials.</div>';
  }
}

if (document.readyState === "loading") {
  document.addEventListener("DOMContentLoaded", init);
} else {
  init();
}
