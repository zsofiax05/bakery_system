from pathlib import Path
import csv
import json
from datetime import datetime
from turtle import position
from typing import Dict, List, Tuple, Optional, Union, Any


class Schedule:
    """
    Class representing a work schedule for an employee at Murphy's Bakery.
    Handles schedule data operations, hours calculation, and wage computation.

    Attributes:
        schedule_id (str): Unique identifier for the schedule
        employee_id (str): ID of the employee this schedule belongs to
        week_start_date (str): Start date of the work week in YYYY-MM-DD format
        hours (Dict[str, float]): Dictionary mapping days to hours worked
        total_hours (float): Total hours worked in the week
        total_pay (float): Total pay for the week
    """

    def __init__(self, schedule_id: str, employee_id: str, week_start_date: str,
                 mon_hours: float = 0, tue_hours: float = 0, wed_hours: float = 0,
                 thu_hours: float = 0, fri_hours: float = 0, sat_hours: float = 0,
                 sun_hours: float = 0):
        self.wage = None
        self.role = position
        self.emp_id = None
        self.schedule_id = schedule_id
        self.employee_id = employee_id
        self.week_start_date = week_start_date
        self.hours = {
            'Monday': mon_hours,
            'Tuesday': tue_hours,
            'Wednesday': wed_hours,
            'Thursday': thu_hours,
            'Friday': fri_hours,
            'Saturday': sat_hours,
            'Sunday': sun_hours
        }
        self.total_hours = sum(self.hours.values())
        self.total_pay = 0.0
        """
        Initialize a Schedule object with the provided attributes.

        Args:
            schedule_id (str): Unique identifier for the schedule
            employee_id (str): ID of the employee this schedule belongs to
            week_start_date (str): Start date of the work week in YYYY-MM-DD format
            mon_hours (float): Hours worked on Monday
            tue_hours (float): Hours worked on Tuesday
            wed_hours (float): Hours worked on Wednesday
            thu_hours (float): Hours worked on Thursday
            fri_hours (float): Hours worked on Friday
            sat_hours (float): Hours worked on Saturday
            sun_hours (float): Hours worked on Sunday

        Member 3 Name: Megan mallon 
        Student ID: 124444416
        """

    @classmethod
    def from_dict(cls, schedule_data: Dict[str, Any]) -> 'Schedule':
        """
        Create a Schedule object from a dictionary.

        Args:
            schedule_data (Dict[str, Any]): Dictionary containing schedule data

        Returns:
            Schedule: A new Schedule object

        Member 4 Name: Zsofia Aradi
        Student ID: 124437146
        """
        return cls(
            schedule_id=schedule_data.get('schedule_id', ''),
            employee_id=schedule_data.get('employee_id', ''),
            week_start_date=schedule_data.get('week_start_date', ''),
            mon_hours=float(schedule_data.get('mon_hours', 0)),
            tue_hours=float(schedule_data.get('tue_hours', 0)),
            wed_hours=float(schedule_data.get('wed_hours', 0)),
            thu_hours=float(schedule_data.get('thu_hours', 0)),
            fri_hours=float(schedule_data.get('fri_hours', 0)),
            sat_hours=float(schedule_data.get('sat_hours', 0)),
            sun_hours=float(schedule_data.get('sun_hours', 0))
        )

        pass

    def to_dict(self) -> Dict[str, Any]:
        """
        Convert Schedule object to a dictionary.

        Returns:
            Dict[str, Any]: Dictionary representation of the schedule

        Member 1 Name: Grace salmon anson
        Student ID:124450632
        """
        pass

    def validate(self) -> Tuple[bool, str]:
        if not self.emp_id or not self.name or not self.role:  # Check if ID, name, and role are missing
            return False, "Employee ID, name, and role are required."

        if self.wage < 0:  # Wage cannot be negative
            return False, "Wage cannot be negative."

        return True, ""  # If everything is correct

        # member 2 name: Abbie Akinkuolie
        # student ID: 124395016
        """
        Validate schedule data according to business rules.

        Returns:
            Tuple[bool, str]: (Validation status, Error message if invalid or empty string if valid)

        Member 2 Name: Abbie Akinkuolie
        Student ID: 124395016
        """
        pass

    def calculate_total_hours(self) -> float:
        self.total_hours = sum(self.hours.values())
        """
        Calculate the total hours worked in the week.

        Returns:
            float: Total hours worked

        Member 3 Name: Megan Mallon 
        Student ID: 124444416
        """
        pass

    def calculate_pay(self, position_rates: Dict[str, Dict[str, float]], position: str) -> Tuple[bool, float, str]:
        # Check if the position exists in the rates dictionary
        if position not in position_rates:
            return False, 0.0, f"Position '{position}' not found in rates"

        # Get the rates for the position
        rates = position_rates[position]

        # Check if rates contain required keys
        if 'base_rate' not in rates:
            return False, 0.0, "Missing base_rate for position"

        # Get the base hourly rate
        base_rate = rates['base_rate']

        # Calculate the regular pay (40 hours or less)
        regular_hours = min(self.total_hours, 40)
        regular_pay = regular_hours * base_rate

        # Calculate overtime pay (over 40 hours)
        overtime_hours = max(0, self.total_hours - 40)
        overtime_rate = rates.get('overtime_rate', base_rate * 1.5)  # Default to 1.5x if not specified
        overtime_pay = overtime_hours * overtime_rate

        # Calculate weekend premium if applicable
        weekend_hours = self.hours['sat'] + self.hours['sun']
        weekend_premium_rate = rates.get('weekend_premium', 0.0)
        weekend_premium = weekend_hours * weekend_premium_rate

        # Calculate total pay
        total_pay = regular_pay + overtime_pay + weekend_premium

        # Round to 2 decimal places for currency
        total_pay = round(total_pay, 2)

        # Update the total_pay attribute
        self.total_pay = total_pay

        return True, total_pay, ""
        """
        Calculate total pay for the week based on hours worked and position rates.

        Args:
            position_rates (Dict[str, Dict[str, float]]): Dictionary of position rates
            position (str): Employee position

        Returns:
            Tuple[bool, float, str]: (Success status, Total pay, Error message if failed or empty string if successful)

        Member 4 Name: Zsofia Aradi
        Student ID: 124437146
        """
        pass

    def update_hours(self, day: str, hours: float) -> Tuple[bool, str]:
        valid_days = ["monday", "tuesday", "wednesday", "thursday", "friday", "saturday", "sunday"]

        if day.lower() not in valid_days:
            return False, f"Invalid day: {day}"

        if not (0 <= hours <= self.max_daily_hours):
            return False, f"Hours must be between 0 and {self.max_daily_hours} hours"

        temp_total = sum(self.hours.values()) + hours - self.hours[day]
        if temp_total > self.max_weekly_hours:
            return False, f"Total hours cannot exceed {self.max_weekly_hours} hours per week"

        self.hours[day] = hours
        return True,
        """
        Update hours worked for a specific day.

        Args:
            day (str): Day of the week ('mon', 'tue', 'wed', 'thu', 'fri', 'sat', 'sun')
            hours (float): Hours worked

        Returns:
            Tuple[bool, str]: (Success status, Error message if failed or empty string if successful)

        Member 1 Name: Grace salmon anson
        Student ID:124450632
        """
        pass