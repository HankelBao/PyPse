from lark import Tree
from enum import Enum, auto
from .debug import DebugOutput


class ValueType(Enum):
    ANONYMOUS = auto()
    INT = auto()
    REAL = auto()
    STRING = auto()
    BOOL = auto()
    FUNCTION = auto()
    PROCEDURE = auto()


def convert_token_to_valuetype(type_token) -> ValueType:
    valuetype_str = str(type_token.children[0].data)
    if valuetype_str == "type_int":
        return ValueType.INT
    if valuetype_str == "type_real":
        return ValueType.REAL
    if valuetype_str == "type_string":
        return ValueType.STRING
    if valuetype_str == "type_bool":
        return ValueType.BOOL
    return ValueType.ANONYMOUS


def get_valuetype_from_value_token(value_token: Tree) -> ValueType:
    valuetype_str = value_token.children[0].data
    if valuetype_str == "int":
        return ValueType.INT
    if valuetype_str == "real":
        return ValueType.REAL
    if valuetype_str == "string":
        return ValueType.STRING
    if valuetype_str == "bool":
        return ValueType.BOOL
    return ValueType.ANONYMOUS


def convert_token_to_value(value_token: Tree) -> ValueType:
    valuetype_str = value_token.children[0].data
    value_type = None
    value_str = value_token.children[0].children[0]
    value_in_python = None
    if valuetype_str == "int":
        value_type = ValueType.INT
        value_in_python = int(value_str)
    if valuetype_str == "real":
        value_type = ValueType.REAL
        value_in_python = float(value_str)
    if valuetype_str == "string":
        value_type = ValueType.STRING
        value_in_python = str(value_str)
    value = Value(value_type)
    value.assign_value_in_python(value_in_python)
    return value


class Value():
    def __init__(self, value_type: ValueType):
        self.value_type = value_type
        self.value_in_python = None

    def assign_value_in_python(self, value_in_python):
        self.value_in_python = value_in_python

    def assign_value(self, value):
        # if self.value_type == value.value_type:
        self.value_in_python = value.value_in_python
        self.value_type = value.value_type

    def debug_output(self):
        output_content = f"type: {self.value_type}, "
        output_content += f"value: {self.value_in_python}"
        DebugOutput.output(output_content)
