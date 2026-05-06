#!/usr/bin/env bash
# Migrate one Klassenstufe folder (track_e_kl07, track_gm_kl05, ...).
# Usage: bash _scripts/migrate_grade.sh <track-folder>
set -euo pipefail

if [[ $# -ne 1 ]]; then
  echo "usage: $0 <track-folder>"; exit 2
fi

folder="$1"
units=$(ls "$folder/units" | grep -v '^_' | grep '\.qmd$' | sed "s|^|$folder/units/|")

if [[ -z "$units" ]]; then
  echo "no .qmd files in $folder/units"; exit 1
fi

# shellcheck disable=SC2086
python _scripts/migrate_to_hugo.py $units
