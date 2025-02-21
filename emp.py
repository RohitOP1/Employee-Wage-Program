import random

# Constants
WAGE_PER_HOUR = 20
FULL_DAY_HOUR = 8
PART_TIME_HOUR = 4

def check_attendance():
    print("Welcome to Employee Wages Computation Program on Master Branch")
    attendance = random.choice([1, 0])  # 1 for Present, 0 for Absent
    return attendance

def emp_daily_wage():
    emp_check = check_attendance()
    
    if emp_check == 1:
        # Randomly determine if the employee is full-time or part-time
        emp_type = random.choice(["full_time", "part_time"])
        
        if emp_type == "full_time":
            daily_wage = WAGE_PER_HOUR * FULL_DAY_HOUR
            print(f"The Employee is present for full day so the daily wage is : {daily_wage}")
        elif emp_type == "part_time":
            daily_wage = WAGE_PER_HOUR * PART_TIME_HOUR
            print(f"The Employee is present for part time so the daily wage is : {daily_wage}")
    else:
        daily_wage = 0
        print(f"The Employee is absent for the day so the daily wage is : {daily_wage}")

if __name__ == "__main__":
    emp_daily_wage()

