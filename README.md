# project-arch-init

這是一套先談清楚，再動手的專案治理 skill。

它不替使用者理解業務，也不會在空白需求上憑空搭架構。目標專案必須先有使用者撰寫的 `docs/init.md`。之後，skill 才會盤點現況、提出治理提案，讓使用者反覆刪改。得到明確核准後，才把規範落到檔案。

核心立場很簡單：

- Sepia 是強制相依，也是預設回答與文件風格。
- Docker 從開發守到部署；部署以 Docker 配合 Terraform。
- 公開操作一律走 root scripts，subagent 不得自行拼命令或消耗資源。
- 測試只能依 `input → unit → integration → E2E` 前進。
- 不用 SHA、checksum 或 image digest 追治理進度；看 task、branch、diff、suite 狀態與 release tag。
- 業務先由人寫清楚，TDD 才有可靠的起點。

本 repository 是 skill 的原始碼與自我驗證工具，不是套用後的目標專案範本。詳細入口見 [SKILL.md](SKILL.md)。

## 從 GitHub 安裝

repository 發佈到 `main` 後，可以直接對 Codex 說：

> 請幫我安裝 jialiang8931/0x12F81AC 技能。

這句話代表安裝 GitHub repository 根目錄的 skill，安裝名稱取 `SKILL.md` 的 `project-arch-init`。若以官方 installer 的參數表示，來源是 `--repo jialiang8931/0x12F81AC --path . --name project-arch-init --ref main`。

安裝後從下一個 turn 開始可用。目標專案仍必須先有使用者撰寫的 `docs/init.md`；安裝成功不會越過 business-init gate。
