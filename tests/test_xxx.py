# assignment_2_tests.py

import os
import csv
import json
import shutil
from pathlib import Path
from datetime import datetime, timedelta

# Import classes from your implementation
# Uncomment these lines when you have implemented the classes
from src.employee import Employee
from src.schedule import Schedule
from src.data_manager import DataManager
from src.reports import Reports

# Test data
TEST_EMPLOYEE_DATA = {
    "employee_id": "E001",
    "first_name": "John",
    "last_name": "Doe",
    "position": "Baker",
    "start_date": "2024-01-15"
}

TEST_WAGE_RATES = {
    "Head Baker": {"base_rate": 18.50, "weekend_rate": 22.00},
    "Baker": {"base_rate": 16.00, "weekend_rate": 19.00},
    "Pastry Chef": {"base_rate": 16.50, "weekend_rate": 19.50},
    "Counter Staff": {"base_rate": 14.00, "weekend_rate": 16.50},
    "Kitchen Assistant": {"base_rate": 13.50, "weekend_rate": 16.00}
}

TEST_SCHEDULE_DATA = {
    "schedule_id": "SCH001",
    "employee_id": "E001",
    "week_start_date": "2024-02-05",
    "mon_hours": 8,
    "tue_hours": 8,
    "wed_hours": 8,
    "thu_hours": 8,
    "fri_hours": 8,
    "sat_hours": 0,
    "sun_hours": 0,
    "total_hours": 40,
    "total_pay": 740.00
}


# Helper functions
def setup_test_environment():
    """Create a clean test environment with test data files."""
    # Clear any existing test data
    if os.path.exists("test_data"):
        shutil.rmtree("test_data")
    if os.path.exists("test_reports"):
        shutil.rmtree("test_reports")

    # Create directories
    os.makedirs("test_data", exist_ok=True)
    os.makedirs("test_reports", exist_ok=True)

    # Create test employees.csv
    with open("test_data/employees.csv", "w", newline="") as file:
        writer = csv.writer(file)
        writer.writerow(["id", "last_name", "first_name", "position", "start_date"])
        writer.writerow([
            TEST_EMPLOYEE_DATA["employee_id"],
            TEST_EMPLOYEE_DATA["last_name"],
            TEST_EMPLOYEE_DATA["first_name"],
            TEST_EMPLOYEE_DATA["position"],
            TEST_EMPLOYEE_DATA["start_date"]
        ])

    # Create test wage_rates.json
    with open("test_data/wage_rates.json", "w") as file:
        json.dump(TEST_WAGE_RATES, file, indent=4)

    # Create test schedules.csv
    with open("test_data/schedules.csv", "w", newline="") as file:
        writer = csv.writer(file)
        writer.writerow([
            "schedule_id", "employee_id", "week_start_date",
            "mon_hours", "tue_hours", "wed_hours", "thu_hours",
            "fri_hours", "sat_hours", "sun_hours",
            "total_hours", "total_pay"
        ])
        writer.writerow([
            TEST_SCHEDULE_DATA["schedule_id"],
            TEST_SCHEDULE_DATA["employee_id"],
            TEST_SCHEDULE_DATA["week_start_date"],
            TEST_SCHEDULE_DATA["mon_hours"],
            TEST_SCHEDULE_DATA["tue_hours"],
            TEST_SCHEDULE_DATA["wed_hours"],
            TEST_SCHEDULE_DATA["thu_hours"],
            TEST_SCHEDULE_DATA["fri_hours"],
            TEST_SCHEDULE_DATA["sat_hours"],
            TEST_SCHEDULE_DATA["sun_hours"],
            TEST_SCHEDULE_DATA["total_hours"],
            TEST_SCHEDULE_DATA["total_pay"]
        ])


def cleanup_test_environment():
    """Clean up the test environment."""
    if os.path.exists("test_data"):
        shutil.rmtree("test_data")
    if os.path.exists("test_reports"):
        shutil.rmtree("test_reports")


def run_test(test_func):
    """Run a test function and print the result."""
    try:
        setup_test_environment()
        result = test_func()
        if result:
            print(f"✅ {test_func.__name__} passed!")
        else:
            print(f"❌ {test_func.__name__} failed.")
        return result
    except Exception as e:
        print(f"❌ {test_func.__name__} failed with error: {str(e)}")
        return False
    finally:
        cleanup_test_environment()


# Employee class tests
def test_employee_creation():
    """Test creating an Employee instance."""
    try:
        # Uncomment this when you've implemented the Employee class
        # employee = Employee(
        #     TEST_EMPLOYEE_DATA["employee_id"],
        #     TEST_EMPLOYEE_DATA["first_name"],
        #     TEST_EMPLOYEE_DATA["last_name"],
        #     TEST_EMPLOYEE_DATA["position"],
        #     TEST_EMPLOYEE_DATA["start_date"]
        # )
        #
        # if (employee.employee_id == TEST_EMPLOYEE_DATA["employee_id"] and
        #     employee.first_name == TEST_EMPLOYEE_DATA["first_name"] and
        #     employee.last_name == TEST_EMPLOYEE_DATA["last_name"] and
        #     employee.position == TEST_EMPLOYEE_DATA["position"] and
        #     employee.start_date == TEST_EMPLOYEE_DATA["start_date"]):
        #     return True

        # For now, return False since we can't test the implementation yet
        print("Test skipped: Employee class not implemented yet.")
        return False
    except Exception as e:
        print(f"Error: {str(e)}")
        return False


def test_employee_from_dict():
    """Test creating an Employee from a dictionary."""
    try:
        # Uncomment this when you've implemented the Employee class
        # employee = Employee.from_dict(TEST_EMPLOYEE_DATA)
        #
        # if (employee.employee_id == TEST_EMPLOYEE_DATA["employee_id"] and
        #     employee.first_name == TEST_EMPLOYEE_DATA["first_name"] and
        #     employee.last_name == TEST_EMPLOYEE_DATA["last_name"] and
        #     employee.position == TEST_EMPLOYEE_DATA["position"] and
        #     employee.start_date == TEST_EMPLOYEE_DATA["start_date"]):
        #     return True

        # For now, return False since we can't test the implementation yet
        print("Test skipped: Employee class not implemented yet.")
        return False
    except Exception as e:
        print(f"Error: {str(e)}")
        return False


def test_employee_to_dict():
    """Test converting an Employee to a dictionary."""
    try:
        # Uncomment this when you've implemented the Employee class
        # employee = Employee(
        #     TEST_EMPLOYEE_DATA["employee_id"],
        #     TEST_EMPLOYEE_DATA["first_name"],
        #     TEST_EMPLOYEE_DATA["last_name"],
        #     TEST_EMPLOYEE_DATA["position"],
        #     TEST_EMPLOYEE_DATA["start_date"]
        # )
        #
        # employee_dict = employee.to_dict()
        #
        # if (employee_dict["employee_id"] == TEST_EMPLOYEE_DATA["employee_id"] and
        #     employee_dict["first_name"] == TEST_EMPLOYEE_DATA["first_name"] and
        #     employee_dict["last_name"] == TEST_EMPLOYEE_DATA["last_name"] and
        #     employee_dict["position"] == TEST_EMPLOYEE_DATA["position"] and
        #     employee_dict["start_date"] == TEST_EMPLOYEE_DATA["start_date"]):
        #     return True

        # For now, return False since we can't test the implementation yet
        print("Test skipped: Employee class not implemented yet.")
        return False
    except Exception as e:
        print(f"Error: {str(e)}")
        return False


def test_employee_validate():
    """Test employee data validation."""
    try:
        # Uncomment this when you've implemented the Employee class
        # # Valid employee
        # valid_employee = Employee(
        #     TEST_EMPLOYEE_DATA["employee_id"],
        #     TEST_EMPLOYEE_DATA["first_name"],
        #     TEST_EMPLOYEE_DATA["last_name"],
        #     TEST_EMPLOYEE_DATA["position"],
        #     TEST_EMPLOYEE_DATA["start_date"]
        # )
        # valid_result, _ = valid_employee.validate()
        #
        # # Invalid employee (empty first name)
        # invalid_employee = Employee(
        #     TEST_EMPLOYEE_DATA["employee_id"],
        #     "",
        #     TEST_EMPLOYEE_DATA["last_name"],
        #     TEST_EMPLOYEE_DATA["position"],
        #     TEST_EMPLOYEE_DATA["start_date"]
        # )
        # invalid_result, _ = invalid_employee.validate()
        #
        # return valid_result and not invalid_result

        # For now, return False since we can't test the implementation yet
        print("Test skipped: Employee class not implemented yet.")
        return False
    except Exception as e:
        print(f"Error: {str(e)}")
        return False


# Schedule class tests
def test_schedule_creation():
    """Test creating a Schedule instance."""
    try:
        # Uncomment this when you've implemented the Schedule class
        # schedule = Schedule(
        #     TEST_SCHEDULE_DATA["schedule_id"],
        #     TEST_SCHEDULE_DATA["employee_id"],
        #     TEST_SCHEDULE_DATA["week_start_date"],
        #     TEST_SCHEDULE_DATA["mon_hours"],
        #     TEST_SCHEDULE_DATA["tue_hours"],
        #     TEST_SCHEDULE_DATA["wed_hours"],
        #     TEST_SCHEDULE_DATA["thu_hours"],
        #     TEST_SCHEDULE_DATA["fri_hours"],
        #     TEST_SCHEDULE_DATA["sat_hours"],
        #     TEST_SCHEDULE_DATA["sun_hours"]
        # )
        #
        # if (schedule.schedule_id == TEST_SCHEDULE_DATA["schedule_id"] and
        #     schedule.employee_id == TEST_SCHEDULE_DATA["employee_id"] and
        #     schedule.week_start_date == TEST_SCHEDULE_DATA["week_start_date"]):
        #     return True

        # For now, return False since we can't test the implementation yet
        print("Test skipped: Schedule class not implemented yet.")
        return False
    except Exception as e:
        print(f"Error: {str(e)}")
        return False


def test_schedule_total_hours():
    """Test calculating total hours for a schedule."""
    try:
        # Uncomment this when you've implemented the Schedule class
        # schedule = Schedule(
        #     TEST_SCHEDULE_DATA["schedule_id"],
        #     TEST_SCHEDULE_DATA["employee_id"],
        #     TEST_SCHEDULE_DATA["week_start_date"],
        #     TEST_SCHEDULE_DATA["mon_hours"],
        #     TEST_SCHEDULE_DATA["tue_hours"],
        #     TEST_SCHEDULE_DATA["wed_hours"],
        #     TEST_SCHEDULE_DATA["thu_hours"],
        #     TEST_SCHEDULE_DATA["fri_hours"],
        #     TEST_SCHEDULE_DATA["sat_hours"],
        #     TEST_SCHEDULE_DATA["sun_hours"]
        # )
        #
        # total_hours = schedule.calculate_total_hours()
        # return total_hours == 40

        # For now, return False since we can't test the implementation yet
        print("Test skipped: Schedule class not implemented yet.")
        return False
    except Exception as e:
        print(f"Error: {str(e)}")
        return False


def test_schedule_calculate_pay():
    """Test calculating pay for a schedule."""
    try:
        # Uncomment this when you've implemented the Schedule class
        # schedule = Schedule(
        #     TEST_SCHEDULE_DATA["schedule_id"],
        #     TEST_SCHEDULE_DATA["employee_id"],
        #     TEST_SCHEDULE_DATA["week_start_date"],
        #     TEST_SCHEDULE_DATA["mon_hours"],
        #     TEST_SCHEDULE_DATA["tue_hours"],
        #     TEST_SCHEDULE_DATA["wed_hours"],
        #     TEST_SCHEDULE_DATA["thu_hours"],
        #     TEST_SCHEDULE_DATA["fri_hours"],
        #     TEST_SCHEDULE_DATA["sat_hours"],
        #     TEST_SCHEDULE_DATA["sun_hours"]
        # )
        #
        # success, pay, _ = schedule.calculate_pay(TEST_WAGE_RATES, "Baker")
        # # Baker: 5 weekdays * 8 hours * €16.00 = €640.00
        # # Compare with tolerance due to floating point
        # return success and abs(pay - 640.0) < 0.01

        # For now, return False since we can't test the implementation yet
        print("Test skipped: Schedule class not implemented yet.")
        return False
    except Exception as e:
        print(f"Error: {str(e)}")
        return False


# DataManager class tests
def test_data_manager_init():
    """Test initializing a DataManager instance."""
    try:
        # Uncomment this when you've implemented the DataManager class
        # data_manager = DataManager("test_data")
        #
        # # Check that the DataManager instance was created correctly
        # return (data_manager.data_dir == Path("test_data") and
        #         data_manager.employees_file == Path("test_data/employees.csv") and
        #         data_manager.schedules_file == Path("test_data/schedules.csv") and
        #         data_manager.wage_rates_file == Path("test_data/wage_rates.json"))

        # For now, return False since we can't test the implementation yet
        print("Test skipped: DataManager class not implemented yet.")
        return False
    except Exception as e:
        print(f"Error: {str(e)}")
        return False


def test_load_employees():
    """Test loading employees from CSV."""
    try:
        # Uncomment this when you've implemented the DataManager class
        # data_manager = DataManager("test_data")
        #
        # success, employees, _ = data_manager.load_employees()
        #
        # # Check that we loaded the test employee correctly
        # return (success and
        #         len(employees) == 1 and
        #         employees[0]["id"] == TEST_EMPLOYEE_DATA["employee_id"] and
        #         employees[0]["first_name"] == TEST_EMPLOYEE_DATA["first_name"] and
        #         employees[0]["last_name"] == TEST_EMPLOYEE_DATA["last_name"] and
        #         employees[0]["position"] == TEST_EMPLOYEE_DATA["position"] and
        #         employees[0]["start_date"] == TEST_EMPLOYEE_DATA["start_date"])

        # For now, return False since we can't test the implementation yet
        print("Test skipped: DataManager class not implemented yet.")
        return False
    except Exception as e:
        print(f"Error: {str(e)}")
        return False


def test_load_wage_rates():
    """Test loading wage rates from JSON."""
    try:
        # Uncomment this when you've implemented the DataManager class
        # data_manager = DataManager("test_data")
        #
        # success, wage_rates, _ = data_manager.load_wage_rates()
        #
        # # Check that we loaded the test wage rates correctly
        # return (success and
        #         "Baker" in wage_rates and
        #         wage_rates["Baker"]["base_rate"] == 16.00 and
        #         wage_rates["Baker"]["weekend_rate"] == 19.00)

        # For now, return False since we can't test the implementation yet
        print("Test skipped: DataManager class not implemented yet.")
        return False
    except Exception as e:
        print(f"Error: {str(e)}")
        return False


def test_save_employee():
    """Test saving an employee to CSV."""
    try:
        # Uncomment this when you've implemented the Employee and DataManager classes
        # data_manager = DataManager("test_data")
        #
        # # Create a new employee
        # new_employee = Employee(
        #     "E002",
        #     "Jane",
        #     "Smith",
        #     "Pastry Chef",
        #     "2024-02-01"
        # )
        #
        # # Save the employee
        # success, _ = data_manager.save_employee(new_employee)
        # if not success:
        #     return False
        #
        # # Load all employees to verify the save worked
        # success, employees, _ = data_manager.load_employees()
        # if not success:
        #     return False
        #
        # # Check that we have both the original and new employees
        # return (len(employees) == 2 and
        #         any(e["id"] == "E001" for e in employees) and
        #         any(e["id"] == "E002" for e in employees))

        # For now, return False since we can't test the implementation yet
        print("Test skipped: Employee or DataManager class not implemented yet.")
        return False
    except Exception as e:
        print(f"Error: {str(e)}")
        return False


# Reports class tests
def test_reports_init():
    """Test initializing a Reports instance."""
    try:
        # Uncomment this when you've implemented the Reports and DataManager classes
        # data_manager = DataManager("test_data")
        # reports = Reports(data_manager, "test_reports")
        #
        # # Check that the Reports instance was created correctly
        # return (reports.data_manager == data_manager and
        #         reports.reports_dir == Path("test_reports"))

        # For now, return False since we can't test the implementation yet
        print("Test skipped: Reports or DataManager class not implemented yet.")
        return False
    except Exception as e:
        print(f"Error: {str(e)}")
        return False


def test_generate_employee_list():
    """Test generating an employee list report."""
    try:
        # Uncomment this when you've implemented the Reports and DataManager classes
        # data_manager = DataManager("test_data")
        # reports = Reports(data_manager, "test_reports")
        #
        # success, employee_list, _ = reports.generate_employee_list()
        #
        # # Check that we generated the report correctly
        # return (success and
        #         len(employee_list) == 1 and
        #         employee_list[0]["id"] == TEST_EMPLOYEE_DATA["employee_id"])

        # For now, return False since we can't test the implementation yet
        print("Test skipped: Reports or DataManager class not implemented yet.")
        return False
    except Exception as e:
        print(f"Error: {str(e)}")
        return False


def test_export_report_to_csv():
    """Test exporting a report to CSV."""
    try:
        # Uncomment this when you've implemented the Reports and DataManager classes
        # data_manager = DataManager("test_data")
        # reports = Reports(data_manager, "test_reports")
        #
        # # Create some test report data
        # report_data = [
        #     {"id": "E001", "name": "John Doe", "position": "Baker"},
        #     {"id": "E002", "name": "Jane Smith", "position": "Pastry Chef"}
        # ]
        #
        # # Export the report
        # success, _ = reports.export_report_to_csv(report_data, "test_report.csv")
        # if not success:
        #     return False
        #
        # # Check that the file was created
        # report_file = Path("test_reports/test_report.csv")
        # if not report_file.exists():
        #     return False
        #
        # # Read the file and check its contents
        # with open(report_file, "r", newline="") as file:
        #     reader = csv.reader(file)
        #     rows = list(reader)
        #
        # # Check that we have a header row and two data rows
        # return (len(rows) == 3 and
        #         rows[0] == ["id", "name", "position"] and
        #         rows[1] == ["E001", "John Doe", "Baker"] and
        #         rows[2] == ["E002", "Jane Smith", "Pastry Chef"])

        # For now, return False since we can't test the implementation yet
        print("Test skipped: Reports or DataManager class not implemented yet.")
        return False
    except Exception as e:
        print(f"Error: {str(e)}")
        return False


# Run all tests
def run_all_tests():
    """Run all tests and return the overall result."""
    test_results = [
        run_test(test_employee_creation),
        run_test(test_employee_from_dict),
        run_test(test_employee_to_dict),
        run_test(test_employee_validate),
        run_test(test_schedule_creation),
        run_test(test_schedule_total_hours),
        run_test(test_schedule_calculate_pay),
        run_test(test_data_manager_init),
        run_test(test_load_employees),
        run_test(test_load_wage_rates),
        run_test(test_save_employee),
        run_test(test_reports_init),
        run_test(test_generate_employee_list),
        run_test(test_export_report_to_csv)
    ]

    passed = sum(test_results)
    total = len(test_results)

    print(f"\nTest summary: {passed}/{total} tests passed.")

    return all(test_results)


if __name__ == "__main__":
    run_all_tests()