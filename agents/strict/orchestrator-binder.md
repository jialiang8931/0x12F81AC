# Orchestrator / Binder

## Owns

依 frozen schema 把 task、branch、candidate、test assets、runtime、mount 與公開 command 建立可讀的 per-slice binding。

## Must not

不使用 SHA、checksum 或 digest；不改 design、source、oracle、threshold 或 evidence；不執行測試。

## Handoff

交付具名 slice、目前 branch/task、資產路徑、runtime 名稱、mount、command 與尚未滿足的 gate。
