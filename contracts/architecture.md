# Architecture contract

治理採最小輪廓，不預建尚未證明的抽象。每個 service 有清楚 owner；共用 package 必須先證明有至少兩個真實 consumer。

production 採 functional core / imperative shell。業務轉換保持純粹，檔案、網路、時間、環境、資料庫與 subprocess 留在 adapter，由 composition root 注入。

目標專案的正式目錄由核准提案決定。通用候選只有 `services/`、`contracts/`、`agents/`、`tasks/`、`scripts/`、`tests/`、`env/`、`infra/docker/`、`infra/terraform/`、`generated/` 與 `tmp/`；不需要的目錄不建立。
