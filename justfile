set shell := ["bash", "-euo", "pipefail", "-c"]

# List recipes
default:
    @just --list --unsorted

# Run all linters and formatters (pre-commit); CI runs this too
lint *args:
    pre-commit run --all-files {{args}}

# Definition of done: lint, type check and build
check: lint build

# Dev server with live reload
dev:
    bun run dev

# Type check and build the site into dist/
build:
    bun install --frozen-lockfile
    bun run check
    bun run build

# Remove build output
clean:
    rm -rf dist .astro
