import frappe

def get_context(context):
    context.no_cach = 1
    context.vehicles = frappe.get_all("Vehicle", fields=["name","make","model","year"])
    return context
