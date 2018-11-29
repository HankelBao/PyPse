from lark import Tree
from enum import Enum, auto
from .debug import DebugOutput
from .output import Warnings


class ValueType(Enum):
    ANONYMOUS = auto()
    INT = auto()
    REAL = auto()
    STRING = auto()
    BOOL = auto()
    ARRAY = auto()
    FUNCTION = auto()
    PROCEDURE = auto()
    TYPE = auto()

    """
    Temporary Notation.
    Shouldn't be used anywhere else except for DeclareBlock
    It won't appear after the value is initiated.
    """
    CUSTOM_TYPE = auto()


class Value():
    def __init__(self, value_type: ValueType):
        self.value_type = value_type
        self.value_in_python = None

    def assign_value_in_python(self, value_in_python):
        self.value_in_python = value_in_python

    def assign_value(self, value):
        if self.value_type != value.value_type:
            Warnings.output(f"assigning unmatched type from {value.value_type} to {self.value_type}")
        self.value_in_python = value.value_in_python
        self.value_type = value.value_type

    def debug_output(self):
        output_content = f"type: {self.value_type}, "
        output_content += f"value: {self.value_in_python}"
        DebugOutput.output(output_content)

    def __repr__(self):
        return f"(type: {self.value_type}, value: {self.value_in_python})"


from .converters import token_find_data
