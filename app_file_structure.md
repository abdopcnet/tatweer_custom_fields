# File Structure

```
tatweer_custom_fields/
├── hooks.py
├── journal_entry.py
├── payment_entry.py
├── tatweer_custom_fields/
│   ├── custom/          # Custom Field JSON files
│   │   ├── asset.json
│   │   ├── sales_invoice.json
│   │   ├── journal_entry.json
│   │   └── ...
│   ├── workspace/       # Workspace JSON files
│   │   ├── قسم_الحسابات/
│   │   ├── إدارة_المشتريات/
│   │   └── ...
│   ├── fixtures/
│   │   ├── server_script.json
│   │   └── client_script.json
│   └── server_script/
│       └── task_wight100/
└── templates/
    └── pages/
```

## Key Files

- `hooks.py` - App hooks (doc_events for Journal Entry, Payment Entry)
- `journal_entry.py` - Journal Entry validation (set custom_internal_id)
- `payment_entry.py` - Payment Entry validation (set custom_internal_id)
- `custom/` - Custom field definitions
- `workspace/` - Workspace configurations
- `fixtures/` - Server/client scripts

