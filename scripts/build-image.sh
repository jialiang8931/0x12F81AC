#!/bin/sh
set -eu

repo_root=$(CDPATH= cd -- "$(dirname -- "$0")/.." && pwd)

exec docker build \
  --file "$repo_root/infra/docker/Dockerfile" \
  --tag project-arch-init:local \
  "$repo_root"
