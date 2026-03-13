

import streamlit as st

# Define base and derived classes
class Person:
    def __init__(self, name):
        self.name = name

    def get_role_description(self):
        return "Generic person role"


class Employee(Person): 
    def __init__(self, name, employee_id):
        super().__init__(name)
        self.employee_id = employee_id

    def get_role_description(self):
        return f"Employee {self.name} (ID: {self.employee_id}) works in the store."


class Manager(Employee):
    def get_role_description(self):
        return f"Manager {self.name} (ID: {self.employee_id}) manages store operations and staff."


class Cashier(Employee):
    def get_role_description(self):
        return f"Cashier {self.name} (ID: {self.employee_id}) handles customer transactions."


class Salesperson(Employee):
    def get_role_description(self):
        return f"Salesperson {self.name} (ID: {self.employee_id}) assists customers with purchases."


class Customer(Person):
    def __init__(self, name):
        super().__init__(name)


class RegularCustomer(Customer):
    def get_role_description(self):
        return f"Customer {self.name} makes regular purchases."


class VIPCustomer(Customer):
    def get_role_description(self):
        return f"VIP Customer {self.name} receives special discounts and perks."


class Supplier(Person):
    def get_role_description(self):
        return f"Supplier {self.name} supplies products to the store."


# Streamlit UI
st.title("Store Role Description App")

# Role selection
role = st.selectbox("Select a role", [
    "Manager", "Cashier", "Salesperson",
    "RegularCustomer", "VIPCustomer", "Supplier"
])

# Name input
name = st.text_input("Enter your name")

# Only show ID input if role is an employee
employee_roles = ["Manager", "Cashier", "Salesperson"]
employee_id = None

if role in employee_roles:
    employee_id = st.text_input("Enter your employee ID")

# Button to submit and display role description
if st.button("Get Role Description"):
    if not name:
        st.warning("Please enter your name.")
    elif role in employee_roles and not employee_id:
        st.warning("Please enter your employee ID.")
    else:
        # Instantiate the selected class
        if role == "Manager":
            person = Manager(name, employee_id)
        elif role == "Cashier":
            person = Cashier(name, employee_id)
        elif role == "Salesperson":
            person = Salesperson(name, employee_id)
        elif role == "RegularCustomer":
            person = RegularCustomer(name)
        elif role == "VIPCustomer":
            person = VIPCustomer(name)
        elif role == "Supplier":
            person = Supplier(name)
        else:
            person = Person(name)

        # Display the description
        st.success(person.get_role_description())

st.markdown('-----')

st.caption('Developed by Muhammed niyaz👨‍💻 | Demostrating Python Inheritance in Streamlit')        
