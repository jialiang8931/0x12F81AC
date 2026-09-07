# Git workflow contract

初始治理：從 `main` 建立 `dev`。所有開發從 `dev` 開分支，不直接在 `main` 或 `dev` 寫程式。

初始化期間，分支跟隨 `tasks/` 的核准工作，例如 `task1/initialize-governance`、`task2/add-docker-runtime`。完成該 task 的必要驗證後，以保留邊界的 merge 合回 `dev`，再把 task 標成完成。

初始化 tasks 結束後，每個新工作先請使用者指定用途前綴與目標，再從 `dev` 開分支。允許的常用前綴為 `feat`、`fix`、`docs`、`chore`、`refactor`、`styles`、`perf`、`test`、`build`、`ci`。名稱使用短而明確的英文 kebab-case。

commit 格式固定為：

```text
<type>(<scope>): <中文任務說明>
```

進度看 branch、task、diff 與測試狀態，不使用 commit SHA。skill 不自動 commit、push、刪除分支、force update 或解決衝突。
