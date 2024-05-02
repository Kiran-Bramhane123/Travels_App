# Copyright (c) 2024, Kiran Vijay Bramhane and contributors
# For license information, please see license.txt

import frappe


def execute(filters=None):
	columns, data = [], []
	columns = get_columns()
	data = get_data(filters)
	chart = get_chart(data)
	return columns, data, None,chart


def get_data(filters):
	data = frappe.db.sql("""
		SELECT v.make, SUM(r.total) as revenue
		FROM `tabRide` as r
		LEFT JOIN `tabVehicle` as v
			ON r.vehicle = v.name
		WHERE r.docstatus = 1
		GROUP BY v.make
		
		""")
	return data

def get_chart(data):
	chart = {
		"data":{
			"labels":[d[0] for d in data],
			"datasets":[
				{
					"name":"Revenue",
					"values":[d[1] for d in data]
				}
			]
		},
		"type":"bar"
	}
	return chart

def get_columns():
	return[
		{
			"lable":"Make",
			"fieldname":"make",
			"fieldtype":"data",
			"width":200
		},
		{
			"lable":"Revenue",
			"fieldname":"revenue",
			"fieldtype":"float",
			"width":200
		}
	]
