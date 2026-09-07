# Proposal schema

每份提案使用相同骨架：

1. **已知業務邊界**：只引用 `docs/init.md`。
2. **未知與阻擋事項**：說明誰應回答、會影響什麼。
3. **建議治理輪廓**：選擇與理由。
4. **規則差異**：保留、新增、刪減，各自說明代價。
5. **目錄與 owner**：只列真正需要的檔案。
6. **執行與測試**：BDD → Docker → TDD → Implement → Test → Integration → E2E → Release；Test 內部先 input/schema，再 unit/contract。
7. **Git 與部署**：branch、commit、release、Terraform gate。
8. **Agent 邊界**：角色、providers、writable paths、禁止事項、handoff。
9. **預計變更**：精確 writable paths 與 forbidden paths。
10. **驗證與 rollback**：命令名稱、狀態與非破壞式回復。
11. **請使用者決定**：列出可直接刪改的規則與尚未核准項。

迭代時顯示相對上一版的變更，不把沉默視為同意。
