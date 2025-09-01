from setuptools import setup, find_packages

setup(
    name='pharmacy_retail',
    version='0.0.1',
    description='Multi-branch pharmacy retail POS & HRM app for Frappe',
    author='Your Name',
    author_email='your@email.com',
    packages=find_packages(),
    include_package_data=True,
    install_requires=['frappe'],
    zip_safe=False
)
