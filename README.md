# Tatweer Custom Fields

![Version](https://img.shields.io/badge/version-30.12.2025-blue)

Custom fields and enhancements for ERPNext DocTypes across accounting, HR, healthcare, and inventory modules.

## Features Preview

### Accounting
- **Payment Entry**: Custom internal ID, month tracking, reference documents, organizational sections
- **Journal Entry**: Custom internal ID, month-based naming series (`ACC-JV-.YY-.{month}.-`), field ordering, enhanced permissions
- **Journal Entry Account**: Extended reference type options

### HR & Payroll
- **Employee Advance**: Workflow state field, mode of payment filters
- **Expense Claim**: Custom field enhancements
- **Leave Application & Leave Type**: Custom field additions
- **Salary Slip & Salary Detail**: Payroll field enhancements

### Healthcare
- **Healthcare Claim & Items**: Custom field support
- **Healthcare Provider Claims & Benefits**: Provider-specific customizations

### Inventory
- **Stock Entry & Details**: Inventory tracking enhancements
- **Material Request & Items**: Procurement field customizations

### Loans
- **Loan Disbursement**: Loan management field enhancements

### Automation
- **Auto Internal ID**: Automatically sets `custom_internal_id` to document name on validation for Payment Entry and Journal Entry

## Installation

```bash
cd $PATH_TO_YOUR_BENCH
bench get-app $URL_OF_THIS_REPO --branch develop
bench --site [site_name] install-app tatweer_custom_fields
```

## Contributing

This app uses `pre-commit` for code formatting and linting. Please [install pre-commit](https://pre-commit.com/#installation) and enable it for this repository:

```bash
cd apps/tatweer_custom_fields
pre-commit install
```

Pre-commit is configured to use the following tools for checking and formatting your code:

- ruff
- eslint
- prettier
- pyupgrade

## License

MIT
