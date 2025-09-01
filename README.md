# Pharmacy Retail (Frappe App)

A minimal Frappe app for multi-branch pharmacy management with POS, inventory, accounts, HRM (employees, attendance, shifts).

## Features

- Manage pharmacy branches, items, employees.
- Clock in/out for attendance.
- Easily extensible for POS, inventory, accounting, and advanced HRM.

## Getting Started

```
bash
# Clone into your bench apps directory
cd ~/frappe-bench/apps
git clone https://github.com/biznapoa222/pharmacy_retail.git

# Install on your site
cd ~/frappe-bench
bench --site <your-site-name> install-app pharmacy_retail
bench --site <your-site-name> migrate
```

## Development

- Add DocTypes via Frappe UI or by extending the JSON/Python files.
- Add client scripts in `public/js`.
- Add custom API in `api/`.