/* Tiny pub/sub state container for the Materials Discovery Network.
 *
 * No framework. Single source of truth shared by graph + filters + list.
 * Subscribers receive the new state on every set(); they decide what to
 * re-render based on a shallow diff.
 *
 * State shape:
 *   {
 *     facets: { type: Set, course: Set, topic: Set, tags: Set },
 *     query:  string,           // search box (Phase 5)
 *     hovered: string | null,   // node id (Phase 5)
 *     filteredNodeIds: Set      // derived; updated by Filters
 *   }
 */
export function createStore(initial) {
  let state = initial;
  const subs = new Set();
  return {
    get: () => state,
    set(patch) {
      state = { ...state, ...patch };
      subs.forEach((fn) => fn(state));
    },
    subscribe(fn) {
      subs.add(fn);
      return () => subs.delete(fn);
    },
  };
}

export function emptyState(graph) {
  return {
    facets: {
      type:   new Set(),
      course: new Set(),
      topic:  new Set(),
      tags:   new Set(),
    },
    query: "",
    hovered: null,
    filteredNodeIds: new Set(graph.nodes.map((n) => n.id)),
  };
}
