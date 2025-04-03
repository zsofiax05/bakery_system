from pathlib import Path
import csv
import json
from datetime import datetime
from typing import Dict, List, Tuple, Optional, Union, Any

class Employee:
    """
    Class representing an employee at Murphy's Bakery.
    Handles employee data operations and validation.

    Attributes:
        employee_id (str): Unique identifier for the employee
        first_name (str): Employee's first name
        last_name (str): Employee's last name
        position (str): Employee's position in the bakery
        start_date (str): Employee's start date in YYYY-MM-DD format
    """


    def __init__(self, employee_id: str, first_name: str, last_name: str, position: str, start_date: str,wage=None):
        self.employee_id = employee_id
        self.total_pay = 0.0
        self.total_hours = 0
        self.first_name = first_name
        self.last_name = last_name
        self.name = f"{first_name} {last_name}"
        self.role = position
        self.wage = wage
        self.position = position
        self.start_date = start_date

    #Memeber 1 Name:Grace salmon anson
    #Student ID:124450632

    @classmethod
    def from_dict(cls, employee_data: Dict[str, str]) -> 'Employee':
        return cls(
            employee_id=employee_data["employee_id"],
            first_name=employee_data["first_name"],
            last_name=employee_data["last_name"],
            position=employee_data["position"],
            start_date=employee_data["start_date"],
            wage=float(employee_data.get("wage", 0.0))
        )

        """
        Create an Employee object from a dictionary.

        Args:
            employee_data (Dict[str, str]): Dictionary containing employee data

        Returns:
            Employee: A new Employee object

        Member 2 Name: Abbie Akinkuolie
        Student ID: 124395016
        """
        pass

    def to_dict(self) -> Dict[str, str]:
        return {
            "employee_id": self.employee_id,
            "employee_name": f"{self.employee.first_name} {self.employee.last_name}",
            "position": self.employee.position,
            "start_date": self.employee.start_date,
            "hours": self.hours, # dictionary of hours worked per day
            "role": self.role,
            "total_hours": self.total_hours,
            "total_pay": self.total_pay,

        }

        """
        Convert Employee object to a dictionary.

        Returns:
            Dict[str, str]: Dictionary representation of the employee

        Member 3 Name: Megan Mallon 
        Student ID: 124444416
        """
        pass

    def validate(self) -> Tuple[bool, str]:
        if not self.employee_id or not self.first_name or not self.last_name or not self.position or not self.start_date:
            return False, "All fields are required."
        if len(self.first_name) > 30 or len(self.last_name) > 30:
            return False, "First and last names must be less than 30 characters."
        try:
            datetime.strptime(self.start_date, "%Y-%m-%d")
        except ValueError:
            return False, "Start date must be in YYYY-MM-DD format."
        return True, ""

        """
        Validate employee data according to business rules.

        Returns:
            Tuple[bool, str]: (Validation status, Error message if invalid or empty string if valid)

        Member 4 Name: Zsofia Aradi
        Student ID: 124437146
        """
        pass

    def update_name(self, new_first_name: str, new_last_name: str) -> Tuple[bool, str]:
        if len(new_first_name) > 30 or len(new_last_name) > 30:
            return False, "First and last names must be less than 30 characters."

        self.first_name = new_first_name
        self.last_name = new_last_name
        return True, ""
        """
        Update employee name with validation.

        Args:
            new_first_name (str): New first name
            new_last_name (str): New last name

        Returns:
            Tuple[bool, str]: (Success status, Error message if failed or empty string if successful)

        Member 1 Name: Grace salmon anson
        Student ID:124450632
        """
        pass

    def update_position(self, new_position: str) -> Tuple[bool, str]:
        if not new_position:
            return False, "Position cannot be empty."

        self.position = new_position
        return True, ""
        """
        Update employee position with validation.

        Args:
            new_position (str): New position

        Returns:
            Tuple[bool, str]: (Success status, Error message if failed or empty string if successful)

        Member 2 Name: Abbie Akinkuolie
        Student ID: 124395016
        """
        pass