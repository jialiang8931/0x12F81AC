# Task 01 — Define delivery lifecycle

```text
owner: skill architecture
objective: 固定 BDD → Docker → TDD → Implement → Test → Integration → E2E → Release 的不可跳級生命週期
providers: 使用者明確指示、既有 skill contracts
consumers: project-arch-init 使用者、角色藍圖、validator、公開 script manifest
writable paths: SKILL.md, README.md, AGENTS.md, contracts/, references/, agents/core/, scripts/manifest.json, scripts/validate_project_arch.py, tests/, tasks/01_define_delivery_lifecycle.md
forbidden paths: .gitignore, agents/openai.yaml, agents/strict/, infra/, tag 0.0.0
verification: build-image, check-input, test-unit, test-integration, test-e2e
evidence path: generated/test-evidence/<suite>/latest.*
rollback: 放棄 task1/define-delivery-lifecycle 的未合併變更；main 與 0.0.0 保持不動
```

status: DONE
