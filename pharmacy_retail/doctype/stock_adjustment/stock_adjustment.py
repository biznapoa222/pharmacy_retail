import frappe
from frappe.model.document import Document

class StockAdjustment(Document):
    def on_submit(self):
        diff = self.new_qty - self.old_qty
        if diff != 0:
            # Make Journal Entry (pseudo-code, adapt to your accounting structure)
            je = frappe.new_doc("Journal Entry")
            je.posting_date = self.date
            # Debit/credit logic
            if diff > 0:
                je.append("accounts", {
                    "account": "Stock Assets - Pharmacy",
                    "debit_in_account_currency": diff * get_item_valuation(self.item)
                })
                je.append("accounts", {
                    "account": "Stock Adjustment - Pharmacy",
                    "credit_in_account_currency": diff * get_item_valuation(self.item)
                })
            else:
                je.append("accounts", {
                    "account": "Stock Adjustment - Pharmacy",
                    "debit_in_account_currency": abs(diff) * get_item_valuation(self.item)
                })
                je.append("accounts", {
                    "account": "Stock Assets - Pharmacy",
                    "credit_in_account_currency": abs(diff) * get_item_valuation(self.item)
                })
            je.save()
            je.submit()

def get_item_valuation(item):
    # Placeholder: fetch cost price/valuation per item
    return frappe.db.get_value("Item", item, "price") or 1
