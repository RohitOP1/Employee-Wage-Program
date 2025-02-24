import random

class EmployeeWageComputation:
    @staticmethod
    def calculate_employee_wage(company_name, wage_per_hour, max_working_days, max_working_hours):
        total_working_days = 0
        total_working_hours = 0
        total_wage = 0

        print(f"\nCalculating wages for {company_name}...")

        while total_working_days < max_working_days and total_working_hours < max_working_hours:
            emp_check = random.choice([1, 0])  # 1 for Present, 0 for Absent

            if emp_check == 1:
                emp_type = random.choice([1, 2])  # 1 for Full-time, 2 for Part-time
                if emp_type == 1:
                    work_hours = 8  # Full-time hours
                else:
                    work_hours = 4  # Part-time hours

                # Ensure we don't exceed max working hours
                if total_working_hours + work_hours > max_working_hours:
                    work_hours = max_working_hours - total_working_hours

                daily_wage = wage_per_hour * work_hours
                total_working_hours += work_hours
                print(f"Day {total_working_days + 1}: Employee worked {work_hours} hours. Daily wage: {daily_wage}")
            else:
                daily_wage = 0
                print(f"Day {total_working_days + 1}: Employee was absent. Daily wage: {daily_wage}")

            total_working_days += 1
            total_wage += daily_wage

        print(f"\nTotal wage for {company_name}: {total_wage}")
        print(f"Total working days: {total_working_days}")
        print(f"Total working hours: {total_working_hours}\n")

if __name__ == "__main__":
    print("Welcome to Employee Wage Computation Program on Master Branch")

    # Compute wages for multiple companies using class method
    EmployeeWageComputation.calculate_employee_wage(
        company_name="Company A",
        wage_per_hour=20,
        max_working_days=20,
        max_working_hours=100
    )

    EmployeeWageComputation.calculate_employee_wage(
        company_name="Company B",
        wage_per_hour=25,
        max_working_days=22,
        max_working_hours=120
    )

