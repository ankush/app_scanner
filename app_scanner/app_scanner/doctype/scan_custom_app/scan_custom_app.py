# Copyright (c) 2022, Ankush Menat and contributors
# For license information, please see license.txt

import json
import subprocess
import os

import frappe
from frappe.model.document import Document



rules = os.path.abspath(os.path.join(__file__, "../../../../rules/"))


class ScanCustomApp(Document):

	@frappe.whitelist()
	def perform_scan(self):
		if not self.directory and not os.path.isabs(self.directory):
			frappe.throw("Absolute directory path required for scanning.")
		result = call_semgrep(self.directory)

		if result:
			self._add_and_format_results(result)


	def _add_and_format_results(self, result):
		result = json.loads(result).get('results')

		self.set("results", [])
		for finding in result:
			self.append("results", {
				"rule": finding.get("check_id", "").split(".")[-1],
				"code_snippet": finding.get("extra", {}).get("lines"),
				"message": finding.get("extra", {}).get("message"),
				"file_path": finding.get("path"),
			})
		self.save()


def call_semgrep(directory):

	cmd = ["semgrep", "--json", f"--config={rules}", directory]
	return subprocess.check_output(cmd)
