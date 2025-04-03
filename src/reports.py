import os
from pathlib import Path
import csv
import json
from datetime import datetime
from typing import Dict, List, Tuple, Optional, Union, Any

from src.data_manager import DataManager


class ReportManager:
    def __init__(self, report_directory: str):
        # Store the report directory
        self.report_directory = report_directory
    pass

    def initialize_reports_directory(self):
        try:
            # Example: Check if the directory exists or create it
            if not os.path.exists(self.report_directory):
                os.makedirs(self.report_directory)
                return True, "Directory created successfully."
            else:
                return True, "Directory already exists."
        except Exception as e:
            # If an error occurs, return False with the error message
            return False, f"Error occurred: {str(e)}"


class Reports:
    """
    Class for generating reports from employee and schedule data.

    Attributes:
        data_manager (DataManager): DataManager instance for data access
        reports_dir (Path): Path to the reports directory
    """

    def __init__(self, data_manager: DataManager, reports_dir: str = "reports"):
        self.data_manager = data_manager
        self.reports_dir = Path(reports_dir)  # Set the reports directory

        """
        Initialize the Reports class with a DataManager instance.

        Args:
            data_manager (DataManager): DataManager instance for data access
            reports_dir (str): Path to the report's directory. Defaults to "reports"

        Member 2 Name: Abbie Akinkuolie
        Student ID: 124395016
        """
        pass

    def initialize_reports_directory(self) -> Tuple[bool, str]:
        try:
            if not os.path.exists(self.directory_path):
                os.makedirs(self.directory_path)
            return True, ""
        except Exception as e:
            return False, str(e)

    report_manager = ReportManager('reports')
    status, message = report_manager.initialize_reports_directory()
    print(status, message)

    """
    Initialize the reports directory if it doesn't exist.

    Returns:
        Tuple[bool, str]: (Success status, Error message if failed or empty string if successful)

    Member 3 Name: Megan Mallon
    Student ID: 124444416
    """
    pass


def generate_employee_list(self, sort_by: str = "last_name") -> Tuple[bool, List[Dict[str, str]], str]:
    try:
        # Get all employees from data manager
        employees = self.data_manager.get_all_employees()

        # Validate sort_by field
        valid_sort_fields = ["employee_id", "first_name", "last_name", "position", "hourly_rate"]
        if sort_by not in valid_sort_fields:
            return False, [], f"Invalid sort field: {sort_by}. Valid fields are: {', '.join(valid_sort_fields)}"

        # Sort the employees by the specified field
        sorted_employees = sorted(employees, key=lambda emp: emp[sort_by])

        return True, sorted_employees, ""
    except Exception as e:
        return False, [], f"Failed to generate employee list: {str(e)}"
    """
    Generate a sorted list of all employees.

    Args:
        sort_by (str): Field to sort by. Defaults to "last_name"

    Returns:
        Tuple[bool, List[Dict[str, str]], str]: (Success status, List of employee dictionaries, Error message if failed or empty string if successful)

    Member 4 Name: Zsofia Aradi
    Student ID: 124437146
    """
    pass


def generate_employee_schedule(self, employee_id: str, start_date: str, end_date: str) -> Tuple[
    bool, List[Dict[str, Any]], str]:
    schedules = []

    def get_schedule(self, employee_id: str, start_dt: datetime, end_dt: datetime) -> Tuple[
        bool, List[Dict[str, Any]], str]:
        try:
            if start_dt > end_dt:
                return False, [], "start_dt must be before end_dt"

            schedule = []
            with open(self.schedule_file, "r") as file:
                reader = csv.DictReader(file)

                for row in reader:
                    if row["employee_id"] == employee_id:
                        week_start = datetime.fromisoformat(row["start_date"])

                        if start_dt <= week_start <= end_dt:
                            row["total_hours"] = float(row["hours"])
                            row["total_pay"] = float(row["hours"]) * float(row["rate"])
                            for day in row["days"].split(','):
                                row[day] = float(row[day])
                            schedule.append(row)

            if not schedule:
                return False, [], "No schedules found."

            return True, schedule, ""

        except FileNotFoundError:
            return False, [], "Schedule file not found."
        except ValueError:
            return False, [], "Invalid date format, please use yyyy-mm-dd."
        except Exception as e:
            return False, [], f"Error occurred: {e}"


class ScheduleManager:
    pass


def generate_employee_schedule(self, employee_id: str, start_date: str, end_date: str) -> Tuple[bool, List[Dict[str, Any]], str]:
    try:
        # Convert start and end dates from string to datetime
        start_dt = datetime.fromisoformat(start_date)
        end_dt = datetime.fromisoformat(end_date)

        # Create an instance of ScheduleManager
        schedule_manager = ScheduleManager("path_to_schedule_file.csv")  # Update this path to your actual schedule file

        # Get the schedule from the manager
        success, schedule, error_message = schedule_manager.get_schedule(employee_id, start_dt, end_dt)

        if success:
            return True, schedule, ""
        else:
            return False, [], error_message

    except ValueError:
        return False, [], "Invalid date format, please use yyyy-mm-dd."
    except Exception as e:
        return False, [], f"Error occurred: {e}"

    """
    Generate a report of schedules for a specific employee within a date range.

    Args:
        employee_id (str): ID of the employee
        start_date (str): Start date in YYYY-MM-DD format
        end_date (str): End date in YYYY-MM-DD format

    Returns:
        Tuple[bool, List[Dict[str, Any]], str]: (Success status, List of schedule dictionaries, Error message if failed or empty string if successful)

    Member 1 Name: Grace salmon anosn
    Student ID:124450632
    """
    pass


def generate_wage_report(self, start_date: str, end_date: str) -> Tuple[bool, List[Dict[str, Any]], str]:
    try:
        wage_report = []  # List to store the wage report

        # Convert string dates to datetime objects for easy comparison
        start_date = datetime.strptime(start_date, "%Y-%m-%d")
        end_date = datetime.strptime(end_date, "%Y-%m-%d")

        # Loop through all employees and their schedules to create the wage report
        for employee in self.data_manager.employees:
            for schedule in self.data_manager.schedules:
                if schedule["emp_id"] == employee.emp_id:  # If the schedule belongs to this employee
                    schedule_date = datetime.strptime(schedule["date"], "%Y-%m-%d")

                    # If the schedule date is within the range, add it to the report
                    if start_date <= schedule_date <= end_date:
                        wage_report.append({
                            "emp_id": employee.emp_id,
                            "name": employee.name,
                            "role": employee.role,
                            "wage": employee.wage,
                            "schedule_date": schedule["date"]
                        })

        if wage_report:  # If there are wages to report
            return True, wage_report, ""
        else:
            return False, [], "No wage records found for the specified date range."

    except Exception as e:
        return False, [], f"Error generating wage report: {e}"

    # member 2 name: Abbie Akinkuolie
    # student ID: 124395016
    """
    Generate a report of wages paid to all employees within a date range.

    Args:
        start_date (str): Start date in YYYY-MM-DD format
        end_date (str): End date in YYYY-MM-DD format

    Returns:
        Tuple[bool, List[Dict[str, Any]], str]: (Success status, List of wage report dictionaries, Error message if failed or empty string if successful)

    Member 2 Name: Abbie Akinkuolie
    Student ID: 124395016
    """
    pass


def export_report_to_csv(self, report_data: List[Dict[str, Any]], filename: str) -> Tuple[bool, str]:
    try:
        if not report_data:
            return False, "No data to export"

        headers = report_data[0].keys()
        with open(filename, 'w', newline='') as file:
            writer = csv.DictWriter(file, fieldnames=headers)
            writer.writeheader()
            for row in report_data:
                writer.writerow(row)

        return True, ""
    except Exception as e:
        return False, str(e)

    report_exporter = ReportExporter()
    report_data = [{"id": 1, "name": "Alice", "sales": 500}, {"id": 2, "name": "Bob", "sales": 300}]
    status, message = report_exporter.export_report_to_csv(report_data, 'report.csv')
    print(status, message)
    """
    Export a report to a CSV file.

    Args:
        report_data (List[Dict[str, Any]]): Report data to export
        filename (str): Name of the file to export to

    Returns:
        Tuple[bool, str]: (Success status, Error message if failed or empty string if successful)

    Member 3 Name: Megan Mallon 
    Student ID: 124444416
    """
    pass


def export_report_to_text(self, report_data: List[Dict[str, Any]], filename: str, title: str) -> Tuple[bool, str]:
    try:
        if not report_data:
            return False, "No data to export"

        # Ensure filename has .txt extension
        if not filename.endswith('.txt'):
            filename += '.txt'

        filepath = self.reports / dir / filename

        with open(filepath, 'w') as textfile:
            # Write the title and current date
            textfile.write(f"{title}\n")
            textfile.write(f"Generated on: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}\n")
            textfile.write('-' * 80 + '\n\n')

            # Get headers and find the maximum width for each column
            if not report_data:
                textfile.write("No data available for this report.\n")
                return True, f"Report exported to {filepath}"

            headers = list(report_data[0].keys())
            column_widths = {header: len(header) for header in headers}

            for row in report_data:
                for header in headers:
                    width = len(str(row[header]))
                    if width > column_widths[header]:
                        column_widths[header] = width

            # Write the headers
            header_row = '  '.join(header.ljust(column_widths[header]) for header in headers)
            textfile.write(header_row + '\n')
            textfile.write('=' * len(header_row) + '\n')

            # Write the data
            for row in report_data:
                data_row = '  '.join(str(row[header]).ljust(column_widths[header]) for header in headers)
                textfile.write(data_row + '\n')

            # Write a footer
            textfile.write('\n' + '-' * 80 + '\n')
            textfile.write(f"End of report. Total records: {len(report_data)}\n")

        return True, f"Report exported to {filepath}"
    except Exception as e:
        return False, f"Failed to export report to text: {str(e)}"

    """
    Export a report to a formatted text file.

    Args:
        report_data (List[Dict[str, Any]]): Report data to export
        filename (str): Name of the file to export to
        title (str): Title for the report

    Returns:
        Tuple[bool, str]: (Success status, Error message if failed or empty string if successful)

    Member 4 Name: Zsofia Aradi
    Student ID: 124437146
    """
    pass