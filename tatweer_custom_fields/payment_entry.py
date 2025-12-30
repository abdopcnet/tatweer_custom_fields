# Copyright (c) 2025, Tatweer Custom Fields
# License: MIT

import frappe


def set_custom_internal_id(doc, method):
	"""Set custom_internal_id to doc.name if empty"""
	if not doc.get("custom_internal_id") and doc.name:
		doc.custom_internal_id = doc.name

