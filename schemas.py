from typing import TypedDict


class Valid_Records(TypedDict):
  name: str
  age: int
  role: str
  salary: int

class Invalid_Records(TypedDict):
  line: int
  reason: str

class Summary(TypedDict):
  total_records: int
  valid_count: int
  invalid_count: int