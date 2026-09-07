# Governance profiles

## docs-only

只管理文件或研究成果。需要 business-init gate、AGENTS、contracts、tasks、Git 與寫作規則。沒有可執行程式時，不強加 Docker、service、env 或 Terraform。

## service

有可執行 service。加上 Docker lifecycle、scripts-only、service-local dependency、input gate、unit、integration 與 E2E。

## deployable

service 會部署到環境。再加 `infra/terraform/`、環境範例、release 規則、plan/apply 分離與部署後驗證。部署從 `dev` 的核准狀態開始。

選最小足夠輪廓。輪廓可以日後升級，不為可能的未來先建立空結構。
