import random

def check_attendance():
    print("Welcome to Employee Wages Computation Program on Master Branch")
    attendance = random.choice([1, 0])
    if attendance == 1:
        print("The employee is Present")
    else:
        print("The employee is Absent")

if __name__ == "__main__":
    check_attendance()
    print("Welcome To Employee Wage Computation")
