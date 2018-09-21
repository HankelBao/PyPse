from enum import Enum, auto


class ValueType(Enum):
    BOOLEAN = auto()
    INT = auto()
    REAL = auto()
    STRING = auto()
    ARRAY = auto()
    ENUM = auto()
    NONE = auto()
    FUNCTION_DEFINITION = auto()

def get_ValueType_by_name(valuetype_str: str) -> ValueType:
    valuetype_str = valuetype_str.strip()
    if valuetype_str == "REAL":
        return ValueType.REAL
    if valuetype_str == "STRING":
        return ValueType.STRING
    if valuetype_str == "INT":
        return ValueType.INT
    if "ARRAY" in valuetype_str:
        return ValueType.ARRAY

class Value():
    def __init__(self, value_type: ValueType):
        self.value_type = value_type
        self.value_in_python = None

    def init_array(self, item_value_type: ValueType, lower_limit, upper_limit):
        if self.value_type == ValueType.ARRAY:
            self.value_in_python = [Value(item_value_type) for i in range(lower_limit, upper_limit+1)]

    def array_value(self, index):
        array_values = self.value_in_python
        return array_values[index]

    def first_assigned(self):
        return False if not self.value_in_python else True

    def assign_value_in_python(self, value_in_python):
        self.value_in_python = value_in_python

    def assign_value(self, value):
        if self.value_type == value.value_type:
            self.value_in_python = value.value_in_python

    def __repr__(self):
        return f"Value in python: {self.value_in_python}, ValueType: {self.value_type.name}"

def is_number(s: str) -> bool:
    try:
        float(s)
        return True
    except ValueError:
        return False 

def is_type(s: str, python_type) -> bool:
    try:
       python_type(s)
       return True
    except ValueError:
        return False
