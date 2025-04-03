import json
from datetime import datetime
from employee import Employee
from schedule import Schedule
from data_manager import DataManager
from reports import Reports


def main():
    # Initialize DataManager with correct path
    data_manager = DataManager("data")
    success, message = data_manager.initialize_data_directory()
    if not success:
        print(f"Failed to initialize data directory: {message}")
        return

    # Initialize Reports
    bakery_reports = Reports(data_manager)

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

            # Generate employee ID using initials and timestamp
            employee_id = f"{first_name[0]}{last_name[0]}{int(datetime.now().timestamp())}"

            # Create and save employee
            employee = Employee(employee_id, first_name, last_name, position, start_date)
            success, message = data_manager.save_employee(employee)
            print(message if message else "Employee added successfully")

        elif choice == "2":
            success, employees, message = data_manager.load_employees()
            if success and employees:
                print("\nEmployee Records:")
                print("ID | Last Name | First Name | Position | Start Date")
                print("-" * 60)
                for emp in employees:
                    print(
                        f"{emp['employee_id']} | {emp['last_name']} | {emp['first_name']} | {emp['position']} | {emp['start_date']}")
            else:
                print("No employees found" if not message else message)

        elif choice == "3":
            employee_id = input("Enter Employee ID: ")
            success, employee_data, message = data_manager.load_employee_by_id(employee_id)

            if success and employee_data:
                new_first_name = input("Enter New First Name: ")
                new_last_name = input("Enter New Last Name: ")

                # Create employee object with updated data
                updated_employee = Employee(
                    employee_id,
                    new_first_name,
                    new_last_name,
                    employee_data['position'],
                    employee_data['start_date']
                )

                success, message = data_manager.update_employee(updated_employee)
                print(message if message else "Employee updated successfully")
            else:
                print(message if message else "Employee not found")

        elif choice == "4":
            employee_id = input("Enter Employee ID: ")
            success, message = data_manager.delete_employee(employee_id)
            print(message if message else "Employee deleted successfully")

        elif choice == "5":
            success, employees, message = data_manager.load_employees()
            if success and employees:
                print("\nEmployee Report:")
                print("ID | Name | Position | Start Date")
                print("-" * 50)
                for emp in employees:
                    print(
                        f"{emp['employee_id']} | {emp['first_name']} {emp['last_name']} | {emp['position']} | {emp['start_date']}")
            else:
                print("No data available for report" if not message else message)

        elif choice == "6":
            print("Exiting system. Goodbye!")
            break

        else:
            print("Invalid choice. Please try again.")


if __name__ == "__main__":
    main()