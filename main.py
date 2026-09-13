# from csv import raw_data

# simulated CSV as list of strings
raw_data: list[str] = [
       "john,25,developer,45000",
       "jane,30,designer,55000",
       "bob,invalid_age,manager,60000",
       "alice,28,developer,",
       "charlie,35,ceo,150000",
       "david,22,intern,25000"
   ]

ROLES = ("developer", "designer", "manager", "ceo", "intern")

class ValidationError(Exception):
    pass

def validate_record(line: str) -> dict[str,str|int] | None:
    """Parse and validate single line & return (name,age,role,salary)"""
    try:
      (name,age,role,salary) = line.split(",",3)

      valid_age = int(age)

      valid_salary = int(salary)

      if valid_age < 18 or valid_salary <= 0:
        raise ValidationError("Not a valid age or valid salary")

      if role not in ROLES:
        raise ValidationError("Not a valid Role")

      return {
        "name":name,
        "age": valid_age,
        "role": role,
        "salary": valid_salary
      }

    except ValidationError as e:
      print(f"Validation Error: {e}")
      return


# def process_raw_data(data: list) -> tuple:
#     """Return (valid_records, errors, summary_stats)"""
#     pass

# def salary_by_role(records: list) -> dict:
#     """Group records by role"""
#     pass

# def employees_over_salary(records: list, threshold: float) -> list:
#     """Filter by salary threshold"""
#     pass


def main():

  for data in raw_data:
    validate_record(data)

main()
