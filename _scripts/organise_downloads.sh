#!/usr/bin/env bash
# Move exam PDFs produced by `quarto render` from the per-Unit folders
# under docs/track_*_kl*/units/ into the canonical
# docs/downloads/<track>/kl<NN>/ tree with the canonical filename.
#
# Quarto renders unit<NN>_<slug>_exam.qmd into
#   docs/track_<x>_kl<NN>/units/unit<NN>_<slug>_exam.pdf
# We move that file to:
#   docs/downloads/<x>/kl<NN>/unit<NN>_<slug>_exam.pdf
set -euo pipefail

DOCS="${DOCS:-docs}"

if [ ! -d "$DOCS" ]; then
  echo "organise_downloads: $DOCS does not exist — did quarto render run?" >&2
  exit 1
fi

shopt -s nullglob

moved=0
for f in "$DOCS"/track_*_kl*/units/unit*_exam.pdf; do
  rel="${f#$DOCS/}"
  # rel = track_<x>_kl<NN>/units/unit<NN>_<slug>_exam.pdf
  course="${rel%%/*}"             # track_<x>_kl<NN>
  fname="${rel##*/}"              # unit<NN>_<slug>_exam.pdf

  # split track_<x>_kl<NN>
  rest="${course#track_}"         # <x>_kl<NN>
  track="${rest%%_kl*}"           # <x>
  kk="${rest##*_kl}"              # <NN>

  dest_dir="$DOCS/downloads/$track/kl$kk"
  mkdir -p "$dest_dir"
  mv "$f" "$dest_dir/$fname"
  moved=$((moved + 1))
done

echo "organise_downloads: moved $moved exam PDF(s)."
