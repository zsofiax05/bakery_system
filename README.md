[This is a Markdown file (with the extension `.md`). Markdown is a simple markup language that is used for formatting plain text files. You can find its [basic syntax](https://www.markdownguide.org/basic-syntax/) at this link.]

# Bakery Employee Management System
- Group number: 25
- Member 1: [Grace salmon anson (124450632)]
- Member 2: [Abbie Akinkuolie (124395016)]
- Member 3: [Megan  Mallon (124444416)]
- Member 4: [Zsofia Aradi (124437146)]
- Last updated: [Date]


## System Description (Assignments 1 & 2)
[Write 2-3 sentences explaining what your program does and why it would be useful for a bakery. Think about what problems it solves for the bakery manager.]

This program is an Employee Management System designed for Murphy's Bakery to help the manager store, update, and retrieve employee data efficiently. The bakery previously used manual spreadsheets, which were error-prone and time-consuming. With this system, the manager can manage employees, track work schedules, and calculate wages automatically.


## How the Program Works (Assignments 1 & 2)
[Explain the main features of your program. What can users do with it? Write at least one sentence about each main feature.]

When you run the program, you can:

- Add a new employee (including first name, last name, position, and start date).
- View employee details by entering their employee ID.
- Update an employee’s name without modifying other details.
- Delete an employee from the system.
- Generate a list of all employees sorted by name or position.
- Store and update work schedules, ensuring all hours are recorded correctly.
- Calculate wages based on hours worked, position, and overtime rules.


## Data Storage (Assignments 1 & 2)
[Explain how your program stores information. Show an example of each type of file you use.]

This program stores data in CSV and JSON files, making it easy to manage and retrieve employee records.

This program uses these files:

`employees.csv` example:

employee_id,last_name,first_name,position,start_date

E001,Doe,John,Baker,2024-01-15

E002,Smith,Jane,Pastry Chef,2023-06-12


`schedules.csv` example:

schedule_id,employee_id,week_start_date,mon_hours,tue_hours,wed_hours,thu_hours,fri_hours,sat_hours,sun_hours,total_hours,total_pay

SCH001,E001,2024-02-05,8,8,8,8,8,0,0,40,740.00

SCH002,E002,2024-02-05,6,6,6,6,6,4,0,34,476.00


`wage_rates.json` example:

{
  "Head Baker": {"base_rate": 18.50, "weekend_rate": 22.00},
  "Baker": {"base_rate": 16.00, "weekend_rate": 19.00},
  "Pastry Chef": {"base_rate": 16.50, "weekend_rate": 19.50},
  "Counter Staff": {"base_rate": 14.00, "weekend_rate": 16.50},
  "Kitchen Assistant": {"base_rate": 13.50, "weekend_rate": 16.00}
}


## Reports (Assignment 3)
[Explain what reports your program can create. Show a small example of one report.]

This program creates these reports:
[List the types of reports]

Example of a daily schedule report:
[Add a small example of one of your reports]


## References and AI Statements
[Refer to the project brief for details on how to cite references and acknowledge the use of AI or state that you did not use it.]

### Assignment 1


### Assignment 2


### Assignment 3

