from pathlib import Path
import csv
from datetime import datetime

def initialize_data_directory(data_dir: str = "data") -> tuple[bool, str]:
    try:
        Path(data_dir).mkdir(parents=True, exist_ok=True)
        return True, ""
    except Exception as e:
        return False, str(e)
    """
    Initialize a directory for storing data files.
    Creates the directory if it doesn't exist.

    Args:
        data_dir (str): Name of the directory to create/check. Defaults to "data"

    Returns:
        tuple[bool, str]: (Success status, Error message if failed or empty string if successful)

    Member 1 Name:
    Student ID:
    Member 3 Name:
    Student ID:
    """
    pass

def validate_text_field(field_name: str, value: str, max_length: int = 30) -> tuple[bool, str]:
    if not value:
        return False, f"{field_name} cannot be empty."
    if len(value) > max_length:
        return False, f"{field_name} must be less than {max_length} characters."
    return True, ""
    """
    Validate a text field according to specified rules.

    Args:
        field_name (str): Name of the field being validated (for error messages)
        value (str): The text value to validate
        max_length (int): Maximum allowed length of the text. Defaults to 30

    Returns:
        tuple[bool, str]: (Validation status, Error message if invalid or empty string if valid)

    Member 2 Name:
    Student ID:
    Member 4 Name:
    Student ID:
    """
    pass

def add_employee(first_name: str, last_name: str, position: str, start_date: str) -> tuple[bool, str]:
    for field_name, value in [("First name", first_name), ("Last name", last_name), ("Position", position)]:
        is_valid, error = validate_text_field(field_name, value)
        if not is_valid:
            return False, error

    # Validate start date format
    try:
        datetime.strptime(start_date, "%Y-%m-%d")
    except ValueError:
        return False, "Start date must be in YYYY-MM-DD format."

    # Generate a unique employee ID
    employees_file = Path("data/employees.csv")
    if not employees_file.exists():
        return False, "Employees file does not exist."

    with open(employees_file, 'r') as f:
        reader = csv.reader(f)
        existing_ids = [row[0] for row in reader if row]  # Skip header and collect IDs

    new_id = f"E{len(existing_ids):03d}"  # Format as E001, E002, etc.

    # Add the new employee to the file
    try:
        with open(employees_file, 'a', newline='') as f:
            writer = csv.writer(f)
            writer.writerow([new_id, first_name, last_name, position, start_date])
        return True, ""
    except Exception as e:
        return False, str(e)
    """
    Create a new employee record in employees.csv.
    Validates input data and generates unique employee ID.

    Member 1 Name:
    Student ID:
    """
    pass


def get_employee_by_id(employee_id: str) -> tuple[bool, dict | str]:
    employees_file = Path("data/employees.csv")
    if not employees_file.exists():
        return False, "Employees file does not exist."

    with open(employees_file, 'r') as f:
        reader = csv.DictReader(f)
        for row in reader:
            if row['employee_id'] == employee_id:
                return True, row
    return False, "Employee not found."
    """
    Retrieve employee record by ID.
    Handles file reading and error cases for missing records.

    Member 2 Name:
    Student ID:
    """
    pass


def update_employee_name(employee_id: str, new_first_name: str, new_last_name: str) -> tuple[bool, str]:
    # Validate new names
    for field_name, value in [("First name", new_first_name), ("Last name", new_last_name)]:
        is_valid, error = validate_text_field(field_name, value)
        if not is_valid:
            return False, error

    employees_file = Path("data/employees.csv")
    if not employees_file.exists():
        return False, "Employees file does not exist."

    # Read all employees
    with open(employees_file, 'r') as f:
        reader = csv.DictReader(f)
        employees = list(reader)

    # Find and update the employee
    updated = False
    for employee in employees:
        if employee['employee_id'] == employee_id:
            employee['first_name'] = new_first_name
            employee['last_name'] = new_last_name
            updated = True
            break

    if not updated:
        return False, "Employee not found."

    # Write updated data back to the file
    try:
        with open(employees_file, 'w', newline='') as f:
            writer = csv.DictWriter(f,
                                    fieldnames=["employee_id", "first_name", "last_name", "position", "start_date"])
            writer.writeheader()
            writer.writerows(employees)
        return True, ""
    except Exception as e:
        return False, str(e)
    """
    Update employee's name while maintaining other data.
    Must read file, update specific record, and write back safely.

    Member 3 Name:
    Student ID:
    """
    pass


def delete_employee(employee_id: str) -> tuple[bool, str]:
    employees_file = Path("data/employees.csv")
    if not employees_file.exists():
        return False, "Employees file does not exist."

    # Read all employees
    with open(employees_file, 'r') as f:
        reader = csv.DictReader(f)
        employees = list(reader)

    # Filter out the employee to delete
    updated_employees = [emp for emp in employees if emp['employee_id'] != employee_id]

    if len(updated_employees) == len(employees):
        return False, "Employee not found."

    # Write updated data back to the file
    try:
        with open(employees_file, 'w', newline='') as f:
            writer = csv.DictWriter(f,
                                    fieldnames=["employee_id", "first_name", "last_name", "position", "start_date"])
            writer.writeheader()
            writer.writerows(updated_employees)
        return True, ""
    except Exception as e:
        return False, str(e)
    """
    Remove employee record while maintaining file integrity.
    Should verify record exists before attempting deletion.

    Member 4 Name:
    Student ID:
    """
    pass