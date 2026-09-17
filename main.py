from schemas import Invalid_Records, Summary, Valid_Records

# from csv import raw_data

# simulated CSV as list of strings
raw_data: list[str] = [
       "john,25,developer,45000",
       "jane,30,designer,55000",
       "bob,invalid_age,manager,60000",
       "alice,28,developer,",
       "charlie,35,ceo,150000",
       "david,22,intern,25000",
       "bob,invalid_age,invalid_role,invalid_salary",
       "levi,37,designer,50000",
   ]

ROLES = ("developer", "designer", "manager", "ceo", "intern")


class ValidationError(Exception):
    pass

def validate_record(line: str,line_num:int) -> Valid_Records | Invalid_Records:
    """Parse and validate single line & return (name,age,role,salary)"""
    try:
      (name,age,role,salary) = line.split(",",3)

      valid_age = int(age)

      valid_salary = int(salary)

      if valid_age < 18 or valid_age > 80:
        return {
          "line": line_num + 1,
          "reason": "Invalid age"
        }

      if valid_salary <= 0:
        return {
          "line": line_num + 1,
          "reason": "Invalid salary"
        }

      if role not in ROLES:
        return {
          "line": line_num + 1,
          "reason": "Invalid role"
        }

      return {
        "name":name,
        "age": valid_age,
        "role": role,
        "salary": valid_salary
      }

    except ValueError:
      return {
        "line": line_num + 1,
        "reason": "Invalid age"
      }

def process_raw_data(raw_data: list[str]):
    """Return (valid_records, errors, summary_stats)"""
    valid_records: list[Valid_Records] = []
    invalid_records:list[Invalid_Records] = []

    for idx,data in enumerate(raw_data):
      val = validate_record(data,idx)

      if "line" in val and "reason" in val:
        invalid_records.append(val)
      else:
        valid_records.append(val)

    try:
      if(len(invalid_records) / len(raw_data) > 0.5):
        raise ValidationError("More than 50% or records has error")

      summary:Summary = {
        "total_records": len(raw_data),
        "valid_count": len(valid_records),
        "invalid_count": len(invalid_records)
      }

      return (valid_records,invalid_records,summary)

    except ValidationError as e:
      print(e)

def salary_by_role(records: list[Valid_Records]):
    """Group records by role"""
    filtered_records: dict[str,list[Valid_Records]] = {}

    for val in records:
      role = val["role"]

      if role in filtered_records:
        filtered_records[role].append(val)
      else:
        filtered_records[role] = [val]

    return filtered_records


def employees_over_salary(records: list[Valid_Records], threshold: float):
    """Filter by salary threshold"""
    filtered_records:list[Valid_Records] = []

    for val in records:
      salary = val.get("salary")

      if( salary <= threshold):
        filtered_records.append(val)

    return filtered_records


def main():
  result = process_raw_data(raw_data)

  if(result is not None):
    valid_records, invalid_records, summary = result

    print("\n=== Valid Records ===")
    print(valid_records)

    print("\n=== Invalid Records ===")
    print(invalid_records)

    print("\n=== Summary ===")
    print(summary)

    print("\n=== Salary By Role ===")
    print(salary_by_role(valid_records))

    print("\n=== Employees Under Salary Threshold ===")
    print(employees_over_salary(valid_records, 60000))


if __name__ == "__main__":
  main()
