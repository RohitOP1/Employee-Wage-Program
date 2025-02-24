import random

class EmployeeWageComputation:
    def __init__(self, company_name, wage_per_hour, max_working_days, max_working_hours):
        self.company_name = company_name
        self.wage_per_hour = wage_per_hour
        self.max_working_days = max_working_days
        self.max_working_hours = max_working_hours
        self.total_wage = 0

    def calculate_employee_wage(self):
        total_working_days = 0
        total_working_hours = 0

        print(f"\nCalculating wages for {self.company_name}...")
        
        while total_working_days < self.max_working_days and total_working_hours < self.max_working_hours:
            emp_check = random.choice([1, 0])  # 1 for Present, 0 for Absent

            if emp_check == 1:
                emp_type = random.choice([1, 2])  # 1 for Full-time, 2 for Part-time
                if emp_type == 1:
                    work_hours = 8  # Full-time hours
                else:
                    work_hours = 4  # Part-time hours

                # Ensure we don't exceed max working hours
                if total_working_hours + work_hours > self.max_working_hours:
                    work_hours = self.max_working_hours - total_working_hours

                daily_wage = self.wage_per_hour * work_hours
                total_working_hours += work_hours
                print(f"Day {total_working_days + 1}: Employee worked {work_hours} hours. Daily wage: {daily_wage}")
            else:
                daily_wage = 0
                print(f"Day {total_working_days + 1}: Employee was absent. Daily wage: {daily_wage}")

            total_working_days += 1
            self.total_wage += daily_wage

        print(f"\nTotal wage for {self.company_name}: {self.total_wage}")
        print(f"Total working days: {total_working_days}")
        print(f"Total working hours: {total_working_hours}\n")

# Main block to calculate wages for multiple companies
if __name__ == "__main__":
    print("Welcome to Employee Wage Computation Program on Master Branch")

    # Create instances for multiple companies with different parameters
    company_a = EmployeeWageComputation("Company A", wage_per_hour=20, max_working_days=20, max_working_hours=100)
    company_b = EmployeeWageComputation("Company B", wage_per_hour=25, max_working_days=22, max_working_hours=120)

    # Calculate wages for each company
    company_a.calculate_employee_wage()
    company_b.calculate_employee_wage()

