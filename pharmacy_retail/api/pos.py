import frappe

@frappe.whitelist()
def get_pos_items():
    """Return only items with stock for POS."""
    return frappe.get_all(
        "Item",
        filters={"current_stock": [">", 0]},
        fields=["name", "item_name", "price", "current_stock"]
    )
