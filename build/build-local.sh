#!/usr/bin/env bash

## build-local.sh: build the manuscript locally on Apple Silicon without conda
## Uses a uv virtual environment (.venv) and Homebrew's pandoc + pandoc-crossref,
## because pandoc 2.x (required by pandoc-xnos in CI) has no native arm64 build.
## Prerequisites: brew install uv pandoc pandoc-crossref pango
## Usage (from the repository root):
##   bash build/build-local.sh                  # HTML + PDF
##   BUILD_PDF=false bash build/build-local.sh  # HTML only (faster)
## Extra environment variables are passed through to build/build.sh.

set -o errexit \
    -o nounset \
    -o pipefail

VENV_DIR="${VENV_DIR:-.venv}"

# Create the virtual environment on first use only
if [ ! -x "$VENV_DIR/bin/manubot" ]; then
  echo >&2 "Creating $VENV_DIR with pinned Manubot dependencies"
  uv venv --python 3.11 "$VENV_DIR"
  VIRTUAL_ENV="$VENV_DIR" uv pip install --requirement build/requirements-local.txt
fi

for cmd in pandoc pandoc-crossref; do
  command -v "$cmd" > /dev/null || { echo >&2 "Missing $cmd: brew install $cmd"; exit 1; }
done

# shellcheck disable=SC1091
source "$VENV_DIR/bin/activate"

# Swap the pandoc-xnos filters for pandoc-crossref (see build/pandoc-local)
export PANDOC_DATA_DIR=build/pandoc-local
# WeasyPrint loads pango/cairo with dlopen: point it to Homebrew's libraries
export DYLD_FALLBACK_LIBRARY_PATH="$(brew --prefix)/lib${DYLD_FALLBACK_LIBRARY_PATH:+:$DYLD_FALLBACK_LIBRARY_PATH}"
# No Docker locally: always use WeasyPrint for the PDF
export MANUBOT_USE_DOCKER=false

bash build/build.sh "$@"
