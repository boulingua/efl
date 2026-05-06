/* Materials Discovery Network — Cytoscape graph layer.
 *
 * Library choice: Cytoscape.js + cytoscape-fcose.
 *   - Handles 500-2000 nodes smoothly with fcose.
 *   - Themeable via stylesheet objects that read CSS custom properties
 *     at render time, so dark/light swaps cost a single re-style call.
 *   - First-class compound-node support if we later group by course.
 *   - Smaller and more maintained than D3-force for this exact use case;
 *     sigma.js is faster but harder to style; vis-network has a heavier
 *     visual default.
 *
 * Bundled by Hugo's js.Build (esbuild) — no loose <script> tags, no CDN
 * dependency. CSS variables are read at runtime so the same compiled JS
 * works in light + dark mode.
 */
import cytoscape from "cytoscape";
import fcose from "cytoscape-fcose";

cytoscape.use(fcose);

const TYPE_SHAPES = {
  article: "ellipse",
  presentation: "round-rectangle",
  worksheet: "round-diamond",
};

/** Read a CSS custom property from :root and trim whitespace. */
function cssVar(name, fallback) {
  const v = getComputedStyle(document.documentElement)
    .getPropertyValue(name)
    .trim();
  return v || fallback;
}

/** Map topic id → CSS variable name (must match data/topics.yml ids). */
function topicColor(topicId) {
  if (!topicId) return cssVar("--network-text-meta", "rgba(0,0,0,0.55)");
  return cssVar(`--topic-${topicId}`, "#888");
}

/** Build a Cytoscape stylesheet from current CSS-variable values. */
function buildStylesheet() {
  return [
    {
      selector: "node",
      style: {
        "background-color": (ele) => topicColor(ele.data("topic")),
        "border-width": 0,
        "label": "",
        "width": (ele) => (ele.data("type") === "article" ? 16 : 12),
        "height": (ele) => (ele.data("type") === "article" ? 16 : 12),
        "shape": (ele) => TYPE_SHAPES[ele.data("type")] || "ellipse",
        "transition-property": "opacity, width, height",
        "transition-duration": "200ms",
        "transition-timing-function": "ease-out",
      },
    },
    {
      selector: 'node[type = "presentation"], node[type = "worksheet"]',
      style: { "opacity": 0.85 },
    },
    {
      selector: "node:selected",
      style: {
        "border-width": 2,
        "border-color": cssVar("--network-highlight", "#E8C547"),
      },
    },
    {
      selector: ".dimmed",
      style: { "opacity": 0.12 },
    },
    {
      selector: ".hovered",
      style: {
        "width": 24,
        "height": 24,
        "z-index": 999,
      },
    },
    {
      selector: "edge",
      style: {
        "curve-style": "straight",
        "width": (ele) => Math.max(0.6, 0.4 * (ele.data("weight") || 1)),
        "opacity": 0.45,
        "line-color": (ele) =>
          ele.data("kind") === "same-article"
            ? cssVar("--network-edge-structural", "rgba(0,0,0,0.30)")
            : topicColor(ele.source().data("topic")),
        "transition-property": "opacity, width",
        "transition-duration": "200ms",
      },
    },
    {
      selector: 'edge[kind = "same-article"]',
      style: { "opacity": 0.6 },
    },
  ];
}

export class NetworkGraph {
  constructor(container, graphData) {
    this.container = container;
    this.data = graphData;
    this.cy = null;
  }

  async render() {
    const elements = [
      ...this.data.nodes.map((n) => ({ data: n })),
      ...this.data.edges.map((e) => ({
        data: { id: `${e.source}__${e.target}`, ...e },
      })),
    ];
    this.cy = cytoscape({
      container: this.container,
      elements,
      style: buildStylesheet(),
      wheelSensitivity: 0.2,
      minZoom: 0.2,
      maxZoom: 4,
      layout: {
        name: "fcose",
        quality: "default",
        randomize: false,
        animate: false,
        fit: true,
        padding: 30,
        nodeRepulsion: 6500,
        idealEdgeLength: 80,
        edgeElasticity: 0.45,
        nestingFactor: 0.1,
        gravity: 0.25,
      },
    });

    this.cy.on("mouseover", "node", (e) => {
      e.target.addClass("hovered");
      this._showTooltip(e.target);
    });
    this.cy.on("mouseout", "node", (e) => {
      e.target.removeClass("hovered");
      this._hideTooltip();
    });
    this.cy.on("tap", "node", (e) => {
      const n = e.target;
      const url = n.data("url");
      if (!url) return;
      const t = n.data("type");
      // Article -> navigate; presentation/worksheet -> download.
      if (t === "article") {
        window.location.href = url;
      } else {
        const a = document.createElement("a");
        a.href = url;
        a.download = "";
        document.body.appendChild(a);
        a.click();
        a.remove();
      }
    });

    // Theme toggle: re-apply stylesheet when Coder switches color scheme.
    const root = document.documentElement;
    const observer = new MutationObserver(() => {
      this.cy.style().fromJson(buildStylesheet()).update();
    });
    observer.observe(root, {
      attributes: true,
      attributeFilter: ["class", "data-theme"],
    });

    return this;
  }

  /**
   * Public API used by the filter and search modules.
   * @param {(node: object) => boolean} predicate Returns true if the node
   *   should remain visible. Non-matching nodes are dimmed (opacity 0.12),
   *   not removed, so the network's structure stays legible.
   */
  applyFilter(predicate) {
    if (!this.cy) return;
    const dim = [];
    const lit = [];
    this.cy.nodes().forEach((n) => {
      if (predicate(n.data())) lit.push(n);
      else dim.push(n);
    });
    this.cy.batch(() => {
      lit.forEach((n) => n.removeClass("dimmed"));
      dim.forEach((n) => n.addClass("dimmed"));
      this.cy.edges().forEach((e) => {
        const dimmed = e.source().hasClass("dimmed") ||
                       e.target().hasClass("dimmed");
        e.toggleClass("dimmed", dimmed);
      });
    });
  }

  _showTooltip(node) {
    const tip = this._tip || this._makeTip();
    const d = node.data();
    tip.querySelector(".network-tip-title").textContent = d.title;
    tip.querySelector(".network-tip-meta").textContent =
      `${d.course || ""} · ${d.topic || ""}`;
    tip.style.opacity = "1";
    const rect = this.container.getBoundingClientRect();
    const pos = node.renderedPosition();
    tip.style.left = `${rect.left + pos.x + 18}px`;
    tip.style.top = `${rect.top + pos.y - 12 + window.scrollY}px`;
  }

  _hideTooltip() {
    if (this._tip) this._tip.style.opacity = "0";
  }

  _makeTip() {
    const tip = document.createElement("div");
    tip.className = "network-tip";
    tip.innerHTML =
      '<div class="network-tip-title"></div>' +
      '<div class="network-tip-meta"></div>';
    document.body.appendChild(tip);
    this._tip = tip;
    return tip;
  }
}
