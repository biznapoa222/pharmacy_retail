import frappe

def execute(filters=None):
    columns = [
        {"label": "Employee", "fieldname": "employee", "fieldtype": "Link", "options": "Employee"},
        {"label": "Date", "fieldname": "attendance_date", "fieldtype": "Date"},
        {"label": "Clock In", "fieldname": "clock_in", "fieldtype": "Time"},
        {"label": "Clock Out", "fieldname": "clock_out", "fieldtype": "Time"},
        {"label": "Status", "fieldname": "status", "fieldtype": "Data"}
    ]
    data = frappe.get_all(
        "Attendance",
        fields=["employee", "attendance_date", "clock_in", "clock_out", "status"],
        order_by="attendance_date desc"
    )
    return columns, data
