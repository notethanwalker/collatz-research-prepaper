#!/usr/bin/env bash
# Render only with installed programs and task-local TeX/cache state.
set -euo pipefail
BASE="$(cd -- "$(dirname -- "${BASH_SOURCE[0]}")/.." && pwd)"
BUILD="$BASE/build"
INPUT="${1:-$BASE/output/Collatz_PrePaper_Audit_2026-10-21.md}"
STEM="$(basename -- "$INPUT" .md)"
export TEXMFVAR="$BUILD/texmf-var"
export TEXMFCONFIG="$BUILD/texmf-config"
export TEXMFHOME="$BUILD/texmf-home"
export TEXMFSYSVAR="$TEXMFVAR"
export TEXMFSYSCONFIG="$TEXMFCONFIG"
export XDG_CACHE_HOME="$BUILD/cache"
export VARTEXFONTS="$TEXMFVAR/fonts"
export TEXMFOUTPUT="$BUILD"
export TEXMF="{$TEXMFCONFIG,$TEXMFVAR,$TEXMFHOME,/etc/texmf,/usr/share/texmf,/usr/share/texlive/texmf-dist}"
# Installed ls-R databases point to missing /var/lib/texmf. Do not use !!.
export TEXFORMATS="$TEXMFVAR/web2c//:"
export MKTEXFMT=0
mkdir -p "$TEXMFVAR/web2c/xetex" "$TEXMFCONFIG" "$TEXMFHOME" "$XDG_CACHE_HOME" "$VARTEXFONTS" "$BASE/output"
if [[ ! -s "$TEXMFVAR/web2c/xetex/xelatex.fmt" ]]; then
  (
    cd "$TEXMFVAR/web2c/xetex"
    xetex -ini -etex -no-shell-escape -interaction=nonstopmode -halt-on-error \
      -jobname=xelatex /usr/share/texlive/texmf-dist/tex/latex/tex-ini-files/xelatex.ini
  ) > "$BUILD/format-build.log" 2>&1
fi
pandoc "$INPUT" \
  --from=markdown+tex_math_single_backslash+tex_math_dollars+raw_tex+autolink_bare_uris \
  --to=latex --standalone --table-of-contents --toc-depth=2 \
  --lua-filter="$BUILD/render_filter.lua" \
  --top-level-division=chapter \
  -V documentclass=report -V fontsize=11pt -V papersize=letter \
  -V geometry:margin=0.85in \
  -V mainfont='Latin Modern Roman' -V sansfont='Latin Modern Sans' \
  -V monofont='DejaVu Sans Mono' -V mathfont='Latin Modern Math' \
  -V colorlinks=true -V linkcolor=blue -V urlcolor=blue \
  --include-in-header="$BUILD/format.tex" \
  --output="$BUILD/$STEM.tex" > "$BUILD/pandoc.log" 2>&1
for PASS in 1 2 3; do
  xelatex -no-shell-escape -interaction=nonstopmode -halt-on-error \
    -file-line-error -output-directory="$BUILD" "$BUILD/$STEM.tex" \
    > "$BUILD/xelatex-pass-$PASS.log" 2>&1 || {
      tail -70 "$BUILD/xelatex-pass-$PASS.log" >&2
      exit 1
    }
done
cp "$BUILD/$STEM.pdf" "$BASE/output/$STEM.pdf"
cp "$BUILD/$STEM.log" "$BUILD/compile.log"
python - "$BUILD/compile.log" "$BUILD/layout-warnings.txt" <<'PY'
import sys
from pathlib import Path
log=Path(sys.argv[1]).read_text(errors='replace').splitlines()
keys=('Overfull', 'Underfull', 'Warning:', 'Missing character', 'undefined references', 'multiply defined')
selected=[]
for i,line in enumerate(log):
    if any(k in line for k in keys):
        selected.append('\n'.join(log[i:min(i+4,len(log))]))
Path(sys.argv[2]).write_text('\n\n'.join(selected)+'\n')
print(f'Compiled PDF. {len(selected)} warning/box messages; see {sys.argv[2]}.')
PY
pdfinfo "$BASE/output/$STEM.pdf" | head -20
printf '\nPDF: %s\n' "$BASE/output/$STEM.pdf"
