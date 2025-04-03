from pathlib import Path
import csv
import json
import os
from datetime import datetime
from typing import Dict, List, Tuple, Optional, Union, Any

from src.employee import Employee
from src.schedule import Schedule


class DataManager:
    """
    Class for managing data storage and retrieval operations.
    Handles file operations, data validation, and data transformations.

    Attributes:
        data_dir (Path): Path to the data directory
        employees_file (Path): Path to the employees CSV file
        schedules_file (Path): Path to the schedules CSV file
        wage_rates_file (Path): Path to the wage rates JSON file
    """

    def __init__(self, data_dir: str = "data"):
        self.data_dir = Path(data_dir)
        self.employees_file = self.data_dir / "employees.csv"
        self.schedules_file = self.data_dir / "schedules.csv"
        self.wage_rates_file = self.data_dir / "wage_rates.json"

        # Initialize data directory and files
        self.initialize_data_directory()
        """
        Initialize the DataManager with the specified data directory.

        Args:
            data_dir (str): Path to the data directory. Defaults to "data"

        Member 2 Name: Abbie Akinkuolie
        Student ID: 124395016
        """

    def initialize_data_directory(self) -> Tuple[bool, str]:
        try:
            self.data_dir.mkdir(exist_ok=True)

            # Initialize employees.csv if it doesn't exist
            if not self.employees_file.exists():
                with open(self.employees_file, 'w', newline='') as f:
                    writer = csv.writer(f)
                    writer.writerow(['employee_id', 'first_name', 'last_name', 'position', 'start_date'])

            # Initialize schedules.csv if it doesn't exist
            if not self.schedules_file.exists():
                with open(self.schedules_file, 'w', newline='') as f:
                    writer = csv.writer(f)
                    writer.writerow(
                        ['schedule_id', 'employee_id', 'week_start', 'mon', 'tue', 'wed', 'thu', 'fri', 'sat', 'sun',
                         'total_hours', 'total_pay'])

            # Initialize wage_rates.json if it doesn't exist
            if not self.wage_rates_file.exists():
                with open(self.wage_rates_file, 'w') as f:
                    json.dump({}, f)

            return True, ""
        except Exception as e:
            return False, str(e)
        """
        Initialize the data directory and create empty data files if they don't exist.

        Returns:
            Tuple[bool, str]: (Success status, Error message if failed or empty string if successful)

        Member 3 Name: Megan  Mallon 
        Student ID:   124444416
        """
        pass

    def load_employees(self) -> Tuple[bool, List[Dict[str, str]], str]:
        try:
            employees = []

            if not self.employees_file.exists():
                return True, employees, ""  # Return empty list if file doesn't exist

            with open(self.employees_file, 'r', newline='') as f:
                reader = csv.DictReader(f)
                for row in reader:
                    employees.append({
                        'employee_id': row['id'],
                        'first_name': row['first_name'],
                        'last_name': row['last_name'],
                        'position': row['position'],
                        'start_date': row['start_date']
                    })

            return True, employees, ""
        except Exception as e:
            return False, [], f"Error loading employees: {str(e)}"

        """
        Load all employees from the employees CSV file.

        Returns:
            Tuple[bool, List[Dict[str, str]], str]: (Success status, List of employee dictionaries, Error message if failed or empty string if successful)

        Member 4 Name: Zsofia Aradi
        Student ID: 124437146
        """
        pass

    def load_employee_by_id(self, employee_id: str) -> Tuple[bool, Optional[Dict[str, str]], str]:
        try:
            success, employees, error = self.load_employees()
            if not success:
                return False, None, error

            for employee in employees:
                if employee['employee_id'] == employee_id:
                    return True, employee, ""

            return False, None, f"Employee {employee_id} not found"
        except Exception as e:
            return False, None, f"Error loading employee: {str(e)}"
        """
        Load a specific employee by ID from the employees CSV file.

        Args:
            employee_id (str): ID of the employee to load

        Returns:
            Tuple[bool, Optional[Dict[str, str]], str]: (Success status, Employee dictionary or None if not found, Error message if failed or empty string if successful)

        Member 1 Name: Grace salmon anson
        Student ID: 124450632
        """
        pass

    def save_employee(self, employee: Employee) -> Tuple[bool, str]:
        try:
            with open('employees.csv', mode='a', newline='') as file:
                fieldnames = ["employee_id", "last_name", "first_name", "position", "start_date"]
                writer = csv.DictWriter(file, fieldnames=fieldnames)

                # If the file is empty, write the header
                if file.tell() == 0:
                    writer.writeheader()

                # Write the employee data
                writer.writerow({
                    "employee_id": employee.employee_id,
                    "last_name": employee.last_name,
                    "first_name": employee.first_name,
                    "position": employee.position,
                    "start_date": employee.start_date
                })
            return True, "Employee saved successfully."
        except Exception as e:
            return False, f"Error saving employee: {str(e)}"
        """
        Save an employee to the employees CSV file.

        Args:
            employee (Employee): Employee object to save

        Returns:
            Tuple[bool, str]: (Success status, Error message if failed or empty string if successful)

        Member 2 Name: Abbie Akinkuolie
        Student ID: 124395016
        """
        pass

    def update_employee(self, employee: Employee) -> Tuple[bool, str]:
        try:
            updated = False
            rows = []
            with open(self.file_path, 'r') as file:
                reader = csv.reader(file)
                for row in reader:
                    if row[0] == str(employee.employee_id):
                        rows.append([str(employee.employee_id), employee.name, employee.position, str(employee.salary)])
                        updated = True
                    else:
                        rows.append(row)

            if updated:
                with open(self.file_path, 'w', newline='') as file:
                    writer = csv.writer(file)
                    writer.writerows(rows)
                return True, ""
            return False, "Employee not found"
        except Exception as e:
            return False, str(e)

        employee_manager = EmployeeManager('employees.csv')
        employee = Employee(1, 'John Doe', 'Manager', 55000)
        status, message = employee_manager.update_employee(employee)
        print(status, message)
        """
        Update an existing employee in the employees CSV file.

        Args:
            employee (Employee): Employee object with updated data

        Returns:
            Tuple[bool, str]: (Success status, Error message if failed or empty string if successful)

        Member 3 Name: Megan Mallon 
        Student ID:   124444416
        """
        pass

    def delete_employee(self, employee_id: str) -> Tuple[bool, str]:
        try:
            # Check if employee exists
            success, existing_employee, error = self.load_employee_by_id(employee_id)
            if not success:
                return False, error

            if not existing_employee:
                return False, f"Employee with ID {employee_id} not found"

            # Load all employees
            success, employees, error = self.load_employees()
            if not success:
                return False, error

            # Filter out the employee to delete
            updated_employees = [emp for emp in employees if emp["employee_id"] != employee_id]

            # Write back to CSV
            with open(self.employees_file, 'w', newline='') as f:
                if updated_employees:
                    writer = csv.DictWriter(f, fieldnames=updated_employees[0].keys())
                    writer.writeheader()
                    writer.writerows(updated_employees)
                else:
                    writer = csv.writer(f)
                    writer.writerow(["employee_id", "first_name", "last_name", "position", "hire_date", "status"])

            return True, ""
        except Exception as e:
            return False, f"Error deleting employee: {str(e)}"
        """
        Delete an employee from the employees CSV file.

        Args:
            employee_id (str): ID of the employee to delete

        Returns:
            Tuple[bool, str]: (Success status, Error message if failed or empty string if successful)

        Member 4 Name: Zsofia Aradi
        Student ID: 124437146
        """
        pass

    def load_wage_rates(self) -> Tuple[bool, Dict[str, Dict[str, float]], str]:
        try:
            with open(self.wage_file, "r") as file:
                wages_rates = json.load(file)
                return True, wages_rates, ""
        except FileNotFoundError:
            return False, None, "Wages file not found"
        except json.JSONDecodeError as e:
            return False, None, f"Error occurred: {e}"
        """
        Load all wage rates from the wage rates JSON file.

        Returns:
            Tuple[bool, Dict[str, Dict[str, float]], str]: (Success status, Dictionary of wage rates, Error message if failed or empty string if successful)

        Member 1 Name: Grace salmon anson
        Student ID:124450632
        """
        pass

    def load_wage_rate_by_position(self, position: str) -> Tuple[bool, Optional[Dict[str, float]], str]:
        try:
            with self.wage_rates_file.open(mode="r") as file:
                wage_data = json.load(file)  # Load the data from the JSON file

            if position in wage_data:
                return True, wage_data[position], ""  # If position found, return wage rate
            else:
                return False, None, f"Wage rates for position '{position}' not found."

        except Exception as e:
            return False, None, f"Error loading wage rates: {e}"

        # member 2 name: Abbie akinkuolie
        # student ID : 124395016
        """
        Load wage rates for a specific position from the wage rates JSON file.

        Args:
            position (str): Position to load rates for

        Returns:
            Tuple[bool, Optional[Dict[str, float]], str]: (Success status, Wage rate dictionary or None if not found, Error message if failed or empty string if successful)

        Member 2 Name: Abbie Akinkuolie
        Student ID: 124395016
        """
        pass

    def save_wage_rate(self, position: str, base_rate: float, weekend_rate: float) -> Tuple[bool, str]:
        try:
            wage_data = {}
            if os.path.exists(self.file_path):
                with open(self.file_path, 'r') as file:
                    wage_data = json.load(file)

            wage_data[position] = {'base_rate': base_rate, 'weekend_rate': weekend_rate}

            with open(self.file_path, 'w') as file:
                json.dump(wage_data, file, indent=4)

            return True, ""
        except Exception as e:
            return False, str(e)

        wage_manager = WageManager('wage_rates.json')
        status, message = wage_manager.save_wage_rate('Manager', 25.5, 30.0)
        print(status, message)
        """
        Save wage rates for a position to the wage rates JSON file.

        Args:
            position (str): Position to save rates for
            base_rate (float): Base hourly rate
            weekend_rate (float): Weekend hourly rate

        Returns:
            Tuple[bool, str]: (Success status, Error message if failed or empty string if successful)

        Member 3 Name: Megan Mallon 
        Student ID: 124444416
        """
        pass

    def delete_wage_rate(self, position: str) -> Tuple[bool, str]:
        try:
            success, wage_rates, error = self.load_wage_rates()
            if not success:
                return False, error

            # Check if position exists
            if position not in wage_rates:
                return False, f"Wage rate for position '{position}' not found"

            # Remove the position
            del wage_rates[position]

            # Write back to JSON
            with open(self.wage_rates_file, 'w') as f:
                json.dump(wage_rates, f, indent=4)

            return True, ""
        except Exception as e:
            return False, f"Error deleting wage rate: {str(e)}"

        """
        Delete wage rates for a position from the wage rates JSON file.

        Args:
            position (str): Position to delete rates for

        Returns:
            Tuple[bool, str]: (Success status, Error message if failed or empty string if successful)

        Member 4 Name: Zsofia Aradi
        Student ID: 124437146
        """
        pass

    def load_schedules(self) -> Tuple[bool, List[Dict[str, Any]], str]:
        if not Path(self.SCHEDULE_FILE).exists():
            return False, [], "Schedules file not found."

        try:
            schedules = []
            with open(self.SCHEDULE_FILE, "r", newline="") as file:
                reader = csv.DictReader(file)

                # Validate required fields
                required_fields = ["total_hours", "total_pay", "mon_hours", "tue_hours",
                                   "wed_hours", "thu_hours", "fri_hours", "sat_hours", "sun_hours"]
                missing_fields = [field for field in required_fields if field not in reader.fieldnames]
                if missing_fields:
                    return False, [], f"Missing required fields: {', '.join(missing_fields)}"

                for row in reader:
                    try:
                        # Convert numeric fields to float
                        for field in required_fields:
                            row[field] = float(row[field])
                        schedules.append(row)
                    except ValueError as e:
                        return False, [], f"Invalid numeric value in row: {dict(row)}"

            return True, schedules, ""

        except Exception as e:
            return False, [], f"An error occurred: {str(e)}"

        """
        Load all schedules from the schedules CSV file.

        Returns:
            Tuple[bool, List[Dict[str, Any]], str]: (Success status, List of schedule dictionaries, Error message if failed or empty string if successful)

        Member 1 Name: Grace salmon anson
        Student ID:124450632
        """
        pass

    def load_schedules_by_employee_id(self, employee_id: str) -> Tuple[bool, List[Dict[str, Any]], str]:
        try:
            schedules = []  # Initialize an empty list for schedules

            with self.schedules_file.open(mode="r", newline="") as file:
                reader = csv.DictReader(file)  # Read the CSV file as a dictionary

                for row in reader:  # Loop through each row in the file
                    if row["emp_id"] == employee_id:  # If the employee ID matches
                        schedules.append(row)  # Add this schedule to the list

            if schedules:  # If schedules are found
                return True, schedules, ""
            else:
                return False, [], f"No schedules found for employee ID '{employee_id}'."

        except Exception as e:
            return False, [], f"Error loading schedules: {e}"

        # member 2 name: Abbie Akinkuolie
        # student ID: 124395016
        """
        Load all schedules for a specific employee from the schedules CSV file.

        Args:
            employee_id (str): ID of the employee to load schedules for

        Returns:
            Tuple[bool, List[Dict[str, Any]], str]: (Success status, List of schedule dictionaries, Error message if failed or empty string if successful)

        Member 2 Name: Abbie Akinkuolie
        Student ID: 124395016
        """
        pass

    def save_schedule(self, schedule: Schedule) -> Tuple[bool, str]:
        try:
            with open(self.file_path, 'a', newline='') as file:
                writer = csv.writer(file)
                writer.writerow([schedule.employee_id, schedule.day, schedule.shift_start, schedule.shift_end])
            return True, ""
        except Exception as e:
            return False, str(e)

        """
        Save a schedule to the schedules CSV file.

        Args:
            schedule (Schedule): Schedule object to save

        Returns:
            Tuple[bool, str]: (Success status, Error message if failed or empty string if successful)

        Member 3 Name: Megan Mallon 
        Student ID: 124444416
        """
        pass

    def update_schedule(self, schedule: Schedule) -> Tuple[bool, str]:
        try:
            # Load all schedules
            success, schedules, error = self.load_schedules()
            if not success:
                return False, error

            # Check if schedule exists
            schedule_exists = False
            for s in schedules:
                if s["schedule_id"] == schedule.schedule_id:
                    schedule_exists = True
                    break

            if not schedule_exists:
                return False, f"Schedule with ID {schedule.schedule_id} not found"

            # Update schedule
            updated_schedules = []
            for s in schedules:
                if s["schedule_id"] == schedule.schedule_id:
                    updated_schedules.append(schedule.to_dict())
                else:
                    updated_schedules.append(s)

            # Write back to CSV
            with open(self.schedules_file, 'w', newline='') as f:
                if updated_schedules:
                    writer = csv.DictWriter(f, fieldnames=updated_schedules[0].keys())
                    writer.writeheader()
                    writer.writerows(updated_schedules)
                else:
                    writer = csv.writer(f)
                    writer.writerow(["schedule_id", "employee_id", "date", "start_time", "end_time", "is_weekend"])

            return True, ""
        except Exception as e:
            return False, f"Error updating schedule: {str(e)}"
        """
        Update an existing schedule in the schedules CSV file.

        Args:
            schedule (Schedule): Schedule object with updated data

        Returns:
            Tuple[bool, str]: (Success status, Error message if failed or empty string if successful)

        Member 4 Name: Zsofia Aradi
        Student ID: 124437146
        """
        pass

    def delete_schedule(self, schedule_id: str) -> Tuple[bool, str]:
        try:
            schedules = []
            found = False

            with open(self.schedule_file, "r", newline="") as file:
                reader = csv.reader(file)
                data = list(reader)  # Read all rows into a list

                if not data:  # If the file is empty
                    return False, "Schedule file is empty."

                headers = data[0]  # Extract headers
                schedules = data[1:]  # Get schedule rows

                for schedule in schedules:
                    if schedule[0] == schedule_id:
                        schedules.remove(schedule)
                        found = True
                        break

            if not found:
                return False, "schedule_id not found."

            # Write back the modified list
            with open(self.schedule_file, "w", newline="") as file:
                writer = csv.writer(file)
                writer.writerow(headers)  # Write headers
                writer.writerows(schedules)  # Write updated schedules

            return True, "Schedule deleted successfully."

        except FileNotFoundError:
            return False, "Schedule file not found."
        except Exception as e:
            return False, f"Error occurred: {e}"

        """
        Delete a schedule from the schedules CSV file.

        Args:
            schedule_id (str): ID of the schedule to delete

        Returns:
            Tuple[bool, str]: (Success status, Error message if failed or empty string if successful)

        Member 1 Name: Grace salmon anson
        Student ID: 124450632
        """
        pass