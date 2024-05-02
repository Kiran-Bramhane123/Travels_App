import frappe
from frappe.utils import today, add_days

def send_insurance_reminder():
    three_days_ahead = add_days(today(), 3)
    insurance_renewals = frappe.get_all("Vehicle", filters={"date_of_insurance_expiry": three_days_ahead}, fields=["name", "make"])

    for vehicle in insurance_renewals:
        frappe.sendmail(
            recipients=["kiranbramhane22@navgurukul.org"],
            subject=_("Insurance Renewal Reminder"),
            message=_("Insurance for {0} expires on {1}").format(vehicle.make, three_days_ahead)
        )
