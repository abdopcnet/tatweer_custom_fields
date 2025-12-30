# Tatweer Custom Fields

![Version](https://img.shields.io/badge/version-30.12.2025-blue)

Custom fields and enhancements for ERPNext accounting DocTypes.

## Features Preview

### Payment Entry Enhancements
- **Custom Internal ID**: Auto-populated internal reference field
- **Custom Month**: Hidden field for month-based tracking
- **Custom Reference Document**: Link to related documents
- **Custom Sections**: Additional organizational sections for attachments and references

### Journal Entry Enhancements
- **Custom Internal ID**: Auto-populated internal reference field (إشاري داخلي)
- **Custom Month**: Hidden field for month-based tracking
- **Auto-naming Series**: Custom naming format with month support (`ACC-JV-.YY-.{month}.-`)
- **Field Ordering**: Customized field layout and organization
- **Account Permissions**: Enhanced account field permissions

### Automation
- **Auto Internal ID**: Automatically sets `custom_internal_id` to document name on validation
- **Document Events**: Hooks on Payment Entry and Journal Entry validation

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
