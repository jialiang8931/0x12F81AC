# Environment-file contract

每個 service 可以提交：

```text
env/<service>/.env.example
env/<service>/.env.dev.example
env/<service>/.env.staging.example
env/<service>/.env.production.example
```

範例只放 key、格式、安全假值與必要說明，不含秘密或真實端點憑證。真實 `.env` 一律忽略；production 值由部署環境的 secret mechanism 注入。未知 key、缺少必要 key、空白秘密與環境名稱不符都必須在 input gate 失敗。
