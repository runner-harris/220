"""
Name: Walker Harris
sales_person.py

Problem: Write a class for a Sales Person.

Certification of Authenticity:
I hereby certify that all work on this assignment is entirely my own.
"""


class SalesPerson:
    """This is a class for SalesPerson"""

    def __init__(self, employee_id, name):
        self.employee_id = employee_id
        self.name = name
        self.sales = []

    def get_id(self):
        return self.employee_id

    def get_name(self):
        return self.name

    def set_name(self, name):
        self.name = name

    def enter_sale(self, sale):
        self.sales.append(sale)

    def total_sales(self):
        acc = 0
        for i in range(len(self.sales)):
            acc += self.sales[i]
        return acc

    def get_sales(self):
        return self.sales

    def met_quota(self, quota):
        if self.total_sales() >= quota:
            return True
        return False

    def compare_to(self, other):
        if self.total_sales() > other.total_sales():
            return 1
        if self.total_sales() < other.total_sales():
            return -1
        return 0

    def __str__(self):
        return "{}-{}:{}".format(self.employee_id, self.name, self.total_sales())
