import frappe
from frappe.utils import nowdate, now_time

@frappe.whitelist()
def clock_in():
    user = frappe.session.user
    employee = frappe.get_value("Employee", {"user_id": user}, "name")
    if not employee:
        return "No Employee linked to this user"
    today = nowdate()
    att = frappe.get_all("Attendance", filters={"employee": employee, "attendance_date": today})
    if att:
        return "Already clocked in today"
    doc = frappe.get_doc({
        "doctype": "Attendance",
        "employee": employee,
        "attendance_date": today,
        "clock_in": now_time(),
        "status": "Present"
    })
    doc.insert()
    return "Clocked in!"

@frappe.whitelist()
def clock_out():
    user = frappe.session.user
    employee = frappe.get_value("Employee", {"user_id": user}, "name")
    today = nowdate()
    att = frappe.get_all("Attendance", filters={"employee": employee, "attendance_date": today})
    if not att:
        return "No Attendance record for today"
    att_doc = frappe.get_doc("Attendance", att[0].name)
    if att_doc.clock_out:
        return "Already clocked out today"
    att_doc.clock_out = now_time()
    att_doc.save()
    return "Clocked out!"
