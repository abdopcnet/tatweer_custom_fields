# API Tree

## Document Events

### Journal Entry

- `set_custom_internal_id(doc, method)`
  - Trigger: validate
  - Logic: Set custom_internal_id = doc.name if empty

### Payment Entry

- `set_custom_internal_id(doc, method)`
  - Trigger: validate
  - Logic: Set custom_internal_id = doc.name if empty

## Server Scripts

### Task Weight Validation

- `task_wight100`
  - Trigger: Before Validate
  - Logic: Validate total task weight ≤ 100% for project/parent task

### Leave Application Notification

- `Leave Application system notification`
  - Trigger: After Insert
  - Logic: Create notification log for leave approver

