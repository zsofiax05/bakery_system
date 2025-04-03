import json
from pathlib import Path
import csv
from datetime import datetime

WAGE_RATES_FILE = Path("data/wage_rates.json")
EMPLOYEES_FILE = Path("data/employees.csv")

def add_position_rate(position: str, base_rate: float, weekend_rate: float) -> tuple[bool, str]:
    # Validate inputs
    if not position or not isinstance(position, str):
        return False, "Position must be a non-empty string"

    try:
        base_rate = float(base_rate)
        weekend_rate = float(weekend_rate)
    except (ValueError, TypeError):
        return False, "Rates must be valid numbers"

    if base_rate <= 0 or weekend_rate <= 0:
        return False, "Rates must be positive values"

    # Create file path
    file_path = Path("wage_rates.json")

    # Load existing data or create empty structure
    if file_path.exists():
        try:
            with open(file_path, 'r') as file:
                rates_data = json.load(file)
        except json.JSONDecodeError:
            rates_data = {}
    else:
        rates_data = {}

    # Check if position already exists
    if position in rates_data:
        return False, f"Position '{position}' already exists"

    # Add new position
    rates_data[position] = {
        "base_rate": base_rate,
        "weekend_rate": weekend_rate,
        "last_updated": datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    }

    # Save updated data
    try:
        with open(file_path, 'w') as file:
            json.dump(rates_data, file, indent=4)
        return True, f"Position '{position}' added successfully"
    except Exception as e:
        return False, f"Error saving data: {str(e)}"
    """
    Add new position with wage rates to wage_rates.json.
    Validates rates and ensures position doesn't already exist.

    Member 4 Name:
    Student ID:
    """
    pass


def get_position_rate(position: str) -> tuple[bool, dict | str]:
    # Validate input
    if not position or not isinstance(position, str):
        return False, "Position must be a non-empty string"

    # Create file path
    file_path = Path("wage_rates.json")

    # Check if file exists
    if not file_path.exists():
        return False, "Wage rates file does not exist"

    # Load data
    try:
        with open(file_path, 'r') as file:
            rates_data = json.load(file)
    except json.JSONDecodeError:
        return False, "Error reading wage rates file"

    # Check if position exists
    if position not in rates_data:
        return False, f"Position '{position}' not found"

    # Return position data
    return True, rates_data[position]
    """
    Get wage rates for a specific position.
    Handles JSON reading and missing position cases.

    Member 3 Name:
    Student ID:
    """
    pass


def update_position_rate(position: str, new_base_rate: float, new_weekend_rate: float) -> tuple[bool, str]:
    # Validate inputs
    if not position or not isinstance(position, str):
        return False, "Position must be a non-empty string"

    try:
        new_base_rate = float(new_base_rate)
        new_weekend_rate = float(new_weekend_rate)
    except (ValueError, TypeError):
        return False, "Rates must be valid numbers"

    if new_base_rate <= 0 or new_weekend_rate <= 0:
        return False, "Rates must be positive values"

    # Create file path
    file_path = Path("wage_rates.json")

    # Check if file exists
    if not file_path.exists():
        return False, "Wage rates file does not exist"

    # Load data
    try:
        with open(file_path, 'r') as file:
            rates_data = json.load(file)
    except json.JSONDecodeError:
        return False, "Error reading wage rates file"

    # Check if position exists
    if position not in rates_data:
        return False, f"Position '{position}' not found"

    # Update position rates
    rates_data[position]["base_rate"] = new_base_rate
    rates_data[position]["weekend_rate"] = new_weekend_rate
    rates_data[position]["last_updated"] = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    # Save updated data
    try:
        with open(file_path, 'w') as file:
            json.dump(rates_data, file, indent=4)
        return True, f"Position '{position}' updated successfully"
    except Exception as e:
        return False, f"Error saving data: {str(e)}"

    """
    Update rates for an existing position.
    Must validate new rates before updating.

    Member 2 Name:
    Student ID:
    """
    pass


def delete_position_rate(position: str) -> tuple[bool, str]:
    # Validate input
    if not position or not isinstance(position, str):
        return False, "Position must be a non-empty string"

    # Create file paths
    rates_file_path = Path("wage_rates.json")
    employees_file_path = Path("employees.csv")

    # Check if rates file exists
    if not rates_file_path.exists():
        return False, "Wage rates file does not exist"

    # Load rates data
    try:
        with open(rates_file_path, 'r') as file:
            rates_data = json.load(file)
    except json.JSONDecodeError:
        return False, "Error reading wage rates file"

    # Check if position exists
    if position not in rates_data:
        return False, f"Position '{position}' not found"

    # Check for employees with this position
    if employees_file_path.exists():
        try:
            with open(employees_file_path, 'r') as file:
                reader = csv.DictReader(file)
                for employee in reader:
                    if 'position' in employee and employee['position'] == position:
                        return False, f"Cannot delete position '{position}' as it is assigned to employees"
        except Exception as e:
            return False, f"Error checking employees: {str(e)}"

    # Delete position
    del rates_data[position]

    # Save updated data
    try:
        with open(rates_file_path, 'w') as file:
            json.dump(rates_data, file, indent=4)
        return True, f"Position '{position}' deleted successfully"
    except Exception as e:
        return False, f"Error saving data: {str(e)}"
    """
    Remove a position and its rates.
    Should check for employees in this position before deletion.

    Member 1 Name:
    Student ID:
    """
    pass