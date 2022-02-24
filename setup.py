from setuptools import setup, find_packages

with open("requirements.txt") as f:
	install_requires = f.read().strip().split("\n")

# get version from __version__ variable in app_scanner/__init__.py
from app_scanner import __version__ as version

setup(
	name="app_scanner",
	version=version,
	description="scan custom apps for obvious problems",
	author="Ankush Menat",
	author_email="ankush@frappe.io",
	packages=find_packages(),
	zip_safe=False,
	include_package_data=True,
	install_requires=install_requires
)
