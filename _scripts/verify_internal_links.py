"""Walk public/, extract every internal href, confirm it resolves to a file.

Picks up minified HTML attribute syntax (`href=/path/`) and quoted forms.
External links and mailto: are skipped. Anchors inside the same page
(`#frag`) are accepted as resolved if the host page exists.

Exits non-zero on any unresolved internal link.
"""
from __future__ import annotations

import re
import sys
from collections import defaultdict
from pathlib import Path

PUBLIC = Path(__file__).resolve().parents[1] / "public"
SITE_BASE = "/efl"

# Match href="..." OR href='...' OR href=... (minified, no quotes).
HREF_RE = re.compile(
    r"""href\s*=\s*(?:"([^"]+)"|'([^']+)'|([^\s>]+))""",
    re.IGNORECASE,
)
SRC_RE = re.compile(
    r"""src\s*=\s*(?:"([^"]+)"|'([^']+)'|([^\s>]+))""",
    re.IGNORECASE,
)


def is_external(target: str) -> bool:
    if target.startswith(("http://", "https://", "//", "mailto:",
                          "tel:", "data:", "javascript:")):
        return True
    return False


def resolve(target: str, src_html: Path) -> Path | None:
    """Return the public/ Path the target points at, or None if unresolved."""
    target = target.split("#", 1)[0].split("?", 1)[0]
    if not target:
        return src_html  # in-page anchor
    if target.startswith(SITE_BASE + "/"):
        rel = target[len(SITE_BASE):]
    elif target.startswith("/"):
        rel = target
    else:
        # Relative path.
        rel = "/" + str(src_html.parent.relative_to(PUBLIC) / target).replace("\\", "/")
    rel = rel.lstrip("/")

    candidates = [
        PUBLIC / rel,
        PUBLIC / rel / "index.html",
    ]
    for c in candidates:
        if c.is_file():
            return c
    return None


def main() -> int:
    if not PUBLIC.is_dir():
        print(f"public/ missing — run hugo --minify first", file=sys.stderr)
        return 2

    broken: dict[str, list[str]] = defaultdict(list)  # target -> sources
    checked = 0
    skipped_external = 0

    for html in PUBLIC.rglob("*.html"):
        try:
            txt = html.read_text(encoding="utf-8", errors="replace")
        except Exception:
            continue

        for m in HREF_RE.finditer(txt):
            target = m.group(1) or m.group(2) or m.group(3)
            if not target:
                continue
            if is_external(target):
                skipped_external += 1
                continue
            checked += 1
            if resolve(target, html) is None:
                broken[target].append(html.relative_to(PUBLIC).as_posix())

        for m in SRC_RE.finditer(txt):
            target = m.group(1) or m.group(2) or m.group(3)
            if not target:
                continue
            if is_external(target):
                skipped_external += 1
                continue
            checked += 1
            if resolve(target, html) is None:
                broken[target].append(html.relative_to(PUBLIC).as_posix())

    print(f"Checked {checked} internal href/src targets "
          f"(skipped {skipped_external} external).")
    if not broken:
        print("All internal links resolve.")
        return 0
    print(f"\n{len(broken)} unique broken targets:")
    for tgt in sorted(broken)[:40]:
        srcs = broken[tgt]
        print(f"  {tgt}  (in {len(srcs)} pages, e.g. {srcs[0]})")
    return 1


if __name__ == "__main__":
    raise SystemExit(main())
