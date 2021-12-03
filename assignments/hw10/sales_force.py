"""
Name: Walker Harris
button.py

Problem: Write a class called SalesForce that encapsulates data for a sales person.

Certification of Authenticity:
I hereby certify that all work on this assignment is entirely my own.
"""

from sales_person import SalesPerson


class SalesForce:
    """this is the salesforce class"""
    def __init__(self):
        self.sales_people = []

    def add_data(self, file_name):
        with open(file_name, 'r') as file:
            for line in file:
                data = line.replace(',', '').split()
                seller = SalesPerson(float(data[0]), data[1] + " " + data[2])
                sales = data[3:]
                i = 0
                while i < len(sales):
                    seller.enter_sale(float(sales[i]))
                    i += 1
                self.sales_people.append(seller)

    def quota_report(self, quota):
        quota_list = []
        for employee in self.sales_people:
            quota_list.append([employee.get_id(), employee.get_name(),
                               employee.total_sales(), employee.met_quota(quota)])
        return quota_list

    def top_seller(self):
        seller_list = []
        for i in range(len(self.sales_people)):
            seller_list.append(self.sales_people[i].total_sales())
        highest = max(seller_list)
        top = []
        for j in range(len(self.sales_people)):
            if self.sales_people[j].total_sales() == highest:
                top.append(self.sales_people[j])
        return top

    def individual_sales(self, employee_id):
        for employee in self.sales_people:
            if employee.get_id() == employee_id:
                return employee
        return None
