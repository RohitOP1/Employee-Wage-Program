import random

# Constants
WAGE_PER_HOUR = 20
FULL_DAY_HOUR = 8
PART_TIME_HOUR = 4
MAX_WORKING_DAYS = 20
MAX_WORKING_HOURS = 100

def check_attendance():
    print("Welcome to Employee Wages Computation Program on Master Branch")
    attendance = random.choice([1, 0])  # 1 for Present, 0 for Absent
    return attendance

def emp_daily_wage():
    emp_check = check_attendance()

    if emp_check == 1:
        # Randomly determine employee type: Full-time or Part-time
        emp_type = random.choice([1, 2])

        # Simulate switch case using a dictionary
        wage_calculator = {
            1: lambda: (WAGE_PER_HOUR * FULL_DAY_HOUR, FULL_DAY_HOUR),  # Full-time
            2: lambda: (WAGE_PER_HOUR * PART_TIME_HOUR, PART_TIME_HOUR)   # Part-time
        }

        # Calculate daily wage and hours worked based on employee type
        daily_wage, hours_worked = wage_calculator[emp_type]()
        print(f"The Employee is present and {'full-time' if emp_type == 1 else 'part-time'} so the daily wage is: {daily_wage}")
        return daily_wage, hours_worked
    else:
        print(f"The Employee is absent for the day so the daily wage is: 0")
        return 0, 0

def calculate_wages_till_condition():
    total_working_days = 0
    total_working_hours = 0
    total_wage = 0

    while total_working_days < MAX_WORKING_DAYS and total_working_hours < MAX_WORKING_HOURS:
        print(f"\nDay {total_working_days + 1}:")
        daily_wage, hours_worked = emp_daily_wage()

        # Ensure we don't exceed max working hours
        if total_working_hours + hours_worked > MAX_WORKING_HOURS:
            hours_worked = MAX_WORKING_HOURS - total_working_hours
            daily_wage = WAGE_PER_HOUR * hours_worked

        total_wage += daily_wage
        total_working_hours += hours_worked
        total_working_days += 1

    print(f"\nTotal working days: {total_working_days}")
    print(f"Total working hours: {total_working_hours}")
    print(f"Total wage for the month: {total_wage}")

if __name__ == "__main__":
    calculate_wages_till_condition()

