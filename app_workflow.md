# Workflow

## Journal Entry / Payment Entry

```
User Creates Document
    ↓
Validate Event Triggered
    ↓
Check custom_internal_id
    ↓
If empty:
    └─ Set custom_internal_id = doc.name
```

## Task Weight Validation

```
User Saves Task
    ↓
Before Validate Triggered
    ↓
Check if linked to project/parent_task
    ↓
Calculate total weight of all tasks
    ↓
Validate: total_weight ≤ 100%
    ↓
If exceeds:
    └─ Throw error
Else:
    └─ Continue save
```

## Leave Application Notification

```
User Submits Leave Application
    ↓
After Insert Triggered
    ↓
Create Notification Log
    ├─ For: leave_approver
    ├─ Type: Alert
    └─ Message: Leave request details
```

