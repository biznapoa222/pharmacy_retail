import frappe

def execute(filters=None):
    columns = [
        {"label": "Pharmtech", "fieldname": "pharmtech", "fieldtype": "Link", "options": "Employee"},
        {"label": "Total Sales", "fieldname": "total_sales", "fieldtype": "Currency"}
    ]
    data = frappe.db.sql("""
        SELECT t.requested_by as pharmtech, SUM(i.amount) as total_sales
        FROM `tabInsurance Sale` t
        INNER JOIN `tabInsurance Sale Item` i ON i.parent = t.name
        GROUP BY t.requested_by
    """, as_dict=1)
    return columns, data
