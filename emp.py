import random

WAGE_PER_HOUR = 20
FULL_DAY_HOUR = 8
PART_TIME_HOUR = 4
WORKING_DAYS_IN_MONTH = 20

def check_attendance():
    print("Welcome to Employee Wages Computation Program on Master Branch")
    attendance = random.choice([1, 0])  # 1 for Present, 0 for Absent
    return attendance

def emp_daily_wage():
    emp_check = check_attendance()

    if emp_check == 1:
        # Randomly determine employee type: 1 for Full-time, 2 for Part-time
        emp_type = random.choice([1, 2])

        # Simulate switch case using a dictionary
        wage_calculator = {
            1: lambda: WAGE_PER_HOUR * FULL_DAY_HOUR,  # Full-time
            2: lambda: WAGE_PER_HOUR * PART_TIME_HOUR   # Part-time
        }

        # Calculate daily wage based on employee type
        daily_wage = wage_calculator[emp_type]()
        print(f"The Employee is present and {'full-time' if emp_type == 1 else 'part-time'} so the daily wage is: {daily_wage}")
        return daily_wage
    else:
        print(f"The Employee is absent for the day so the daily wage is: 0")
        return 0

def calculate_monthly_wage():
    total_wage = 0

    for day in range(1, WORKING_DAYS_IN_MONTH + 1):
        print(f"\nDay {day}:")
        daily_wage = emp_daily_wage()
        total_wage += daily_wage

    print(f"\nTotal wage for the month (for {WORKING_DAYS_IN_MONTH} days): {total_wage}")

if __name__ == "__main__":
    calculate_monthly_wage()

