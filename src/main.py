import json
from employee import Employee
from schedule import Schedule
from data_manager import DataManager
from reports import Reports
from datetime import datetime
import os
import sys
import employee_data
import wage_data
import reports


def main():
    data_manager = DataManager()
    reports = Reports(data_manager)

    print("Welcome to Murphy's Bakery Employee Management System")

    while True:
        print("\nMain Menu:")
        print("1. Add Employee")
        print("2. View Employees")
        print("3. Update Employee Name")
        print("4. Delete Employee")
        print("5. Generate Employee Report")
        print("6. Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            first_name = input("Enter First Name: ")
            last_name = input("Enter Last Name: ")
            position = input("Enter Position: ")
            start_date = input("Enter Start Date (YYYY-MM-DD): ")

            employee_id = f"{first_name[0]}{last_name[0]}{int(datetime.now().timestamp())}"

            employee = Employee(employee_id, first_name, last_name, position, start_date)
            success, message = data_manager.save_employee(employee)
            print(message)

            def get_wage(position):
                with open("data/wage_rates.json", "r") as file:
                    wage_data = json.load(file)
                return wage_data.get(position, {}).get("base_rate", 0)



        elif choice == "2":
            success, employees, message = data_manager.load_employees()
            if success:
                print("\nEmployee Records:")
                print("id,last_name,first_name,position,start_date")
                for emp in employees:
                    print(
                        f"{emp['employee_id']},{emp['last_name']},{emp['first_name']},{emp['position']},{emp['start_date']}")
            else:
                print(message)

        elif choice == "3":
            employee_id = input("Enter Employee ID: ")
            new_first_name = input("Enter New First Name: ")
            new_last_name = input("Enter New Last Name: ")

            success, employee_data, message = data_manager.load_employee_by_id(employee_id)
            if success:
                employee = Employee.from_dict(employee_data)
                success, message = employee.update_name(new_first_name, new_last_name)
                if success:
                    data_manager.update_employee(employee)
                print(message)
            else:
                print(message)

        elif choice == "4":
            employee_id = input("Enter Employee ID: ")
            success, message = data_manager.delete_employee(employee_id)
            print(message)

        elif choice == "5":
            success, report, message = reports.generate_employee_list()
            if success:
                print("\nGenerated Employee Report:")
                for emp in report:
                    print(
                        f"{emp['employee_id']},{emp['last_name']},{emp['first_name']},{emp['position']},{emp['start_date']}")
            else:
                print(message)

        elif choice == "6":
            print("Exiting system. Goodbye!")
            break

        else:
            print("Invalid choice. Please try again.")


if __name__ == "__main__":
    main()
