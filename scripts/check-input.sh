#!/bin/sh
set -eu

repo_root=$(CDPATH= cd -- "$(dirname -- "$0")/.." && pwd)
evidence_dir="$repo_root/generated/test-evidence"
mkdir -p "$evidence_dir/input" "$evidence_dir/unit" "$evidence_dir/integration" "$evidence_dir/e2e"
printf '%s\n' NOT_EXECUTED > "$evidence_dir/unit/latest.status"
printf '%s\n' NOT_EXECUTED > "$evidence_dir/integration/latest.status"
printf '%s\n' NOT_EXECUTED > "$evidence_dir/e2e/latest.status"

log_path="$evidence_dir/input/latest.log"
if docker run --rm --network none --read-only --tmpfs /tmp:rw,noexec,nosuid,size=16m \
  --entrypoint python3 \
  --mount "type=bind,src=$repo_root,dst=/workspace,readonly" \
  --workdir /workspace \
  project-arch-init:local \
  -m unittest discover -s tests/input -v > "$log_path" 2>&1; then
  cat "$log_path"
  printf '%s\n' PASSED > "$evidence_dir/input/latest.status"
else
  cat "$log_path"
  printf '%s\n' FAILED > "$evidence_dir/input/latest.status"
  exit 1
fi
