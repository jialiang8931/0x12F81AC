#!/bin/sh
set -eu

if [ "$#" -ne 2 ]; then
  echo "usage: $0 <absolute-project-root> <docs-only|service|deployable>" >&2
  exit 64
fi

project_root=$1
profile=$2

case "$project_root" in
  /*) ;;
  *) echo "project root must be absolute" >&2; exit 64 ;;
esac

case "$profile" in
  docs-only|service|deployable) ;;
  *) echo "unknown profile: $profile" >&2; exit 64 ;;
esac

exec docker run --rm \
  --network none \
  --read-only \
  --tmpfs /tmp:rw,noexec,nosuid,size=16m \
  --mount "type=bind,src=$project_root,dst=/target,readonly" \
  project-arch-init:local \
  --project-root /target \
  --profile "$profile"
