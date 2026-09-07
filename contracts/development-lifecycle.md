# Development lifecycle contract

每項功能沿著同一條路走：

```text
BDD → Docker → TDD → Implement → Test → Integration → E2E → Release
```

## Stage gates

| Stage | 必要結果 | 禁止事項 |
|---|---|---|
| BDD | 使用者擁有的 `docs/init.md` 已核准範圍、規則與行為情境 | AI 不代寫業務，也不先建技術解法 |
| Docker | 固定版本的開發與驗證環境可由核准 script 建置；mount、network、user、secrets 與 writable path 已限制 | 不在宿主機執行 project code 或安裝 project dependency |
| TDD | Test Designer 在 implementation 前固定 cases、oracle、input/schema、fixture 與 acceptance；適用時保存可解釋的 red state | 不看 implementation 後補答案；characterization 不硬造失敗 |
| Implement | 只完成讓 frozen cases 通過的最小 production 變更，狀態標為 `COMPLETE_PENDING_TEST` | 不改 oracle、threshold 或 BDD 來迎合程式 |
| Test | 在 Docker 內先跑 input/schema，再跑 unit/contract；全部必須 `PASSED` | 不跳過低層測試，也不把 Integration 當 unit |
| Integration | 驗證真實 adapter、service 邊界、儲存或外部協定的協作 | 不用 mock-only 結果宣稱整合通過 |
| E2E | 驗證已核准的使用者旅程與可觀察結果 | 不用 E2E 反向發明底層規則 |
| Release | 從乾淨、已通過前述 gate 的 `dev` 狀態，以 Docker 與 Terraform 完成部署和 release tag | 不從 task branch、dirty tree 或未核准 plan 發佈 |

前一階段沒有完成，後一階段一律是 `NOT_EXECUTED`。`NOT_APPLICABLE` 必須在 BDD 或 TDD 時說明理由，不能在失敗後補填。
