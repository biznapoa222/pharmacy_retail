frappe.ready(function() {
    $("#clock-in-btn").on("click", function() {
        frappe.call({
            method: "pharmacy_retail.api.hrm.clock_in",
            callback: function(r) {
                frappe.msgprint(r.message);
            }
        });
    });
    $("#clock-out-btn").on("click", function() {
        frappe.call({
            method: "pharmacy_retail.api.hrm.clock_out",
            callback: function(r) {
                frappe.msgprint(r.message);
            }
        });
    });
});
