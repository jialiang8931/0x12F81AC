# Deployment contract

部署只從乾淨且已通過必要 gate 的 `dev` 狀態開始，不從 task branch 或 dirty tree 部署。這不會自動把 `dev` 合入 `main`。

release 名稱使用：

```text
release/YYYYMMDD-<english-feature-difference>
```

annotated tag 訊息使用 `release: YYYYMMDD-<中文功能差異>`。Tag 指向通過部署驗證的 `dev` commit，但治理流程不保存或比較 commit SHA，也不強制移動既有 tag。

Release 是八階段生命週期的最後一步。只有 Test、Integration 與 E2E 都通過才可進入。Release 內部順序為：建置相同 release 名稱的 Docker image、由容器執行 Terraform plan、使用者明確核准、Terraform apply、部署後驗證、建立 release tag。Terraform plan 綁定 release 名稱與 environment，不使用 SHA 或 image digest。
