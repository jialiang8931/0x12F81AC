# Deployment governance

Release 是 BDD、Docker、TDD、Implement、Test、Integration 與 E2E 全部完成後的最後階段。它從乾淨 `dev` 開始，建立 `release/YYYYMMDD-<english-feature-difference>` 名稱，再以同一名稱標記 image 與 Terraform variable。

Terraform 在固定版本 Docker toolchain 中執行。先產 plan 並交付差異；取得明確核准才 apply。部署後做 smoke 或 acceptance，再建立不可移動的 annotated release tag。失敗時保留結果並停止，不把半成品說成 release。

Git tag 會指向 commit，但流程不讀取、保存或比較 SHA。它以 branch、task、suite、release name 與 tag 描述狀態。
