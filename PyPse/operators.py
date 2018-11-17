from lark import Tree
from .values import Value, ValueType
from .debug import DebugOutput


class Operator():
    priority = 0

    def operate(value1: Value, value2: Value) -> Value:
        pass

    def debug_output():
        DebugOutput.output("anonymous operator")


class OperatorAdd(Operator):
    priority = 2

    def operate(value1: Value, value2: Value) -> Value:
        if value1.value_type == ValueType.INT and value2.value_type == ValueType.INT:
            value = Value(ValueType.INT)
            value_in_python = int(value1.value_in_python + value2.value_in_python)
            value.assign_value_in_python(value_in_python)
            return value
        return None

    def debug_output():
        DebugOutput.output("+")


class OperatorMinus(Operator):
    priority = 2

    def operate(value1: Value, value2: Value) -> Value:
        value = Value(value1.value_type)
        value_in_python = value1.value_in_python - value2.value_in_python
        value.assign_value_in_python(value_in_python)
        return value

    def debug_output():
        DebugOutput.output("-")


class OperatorMultiple(Operator):
    priority = 3

    def operate(value1: Value, value2: Value) -> Value:
        value = Value(value1.value_type)
        value_in_python = value1.value_in_python * value2.value_in_python
        value.assign_value_in_python(value_in_python)
        return value

    def debug_output():
        DebugOutput.output("*")


class OperatorDivide(Operator):
    priority = 3

    def operate(value1: Value, value2: Value) -> Value:
        value = Value(value1.value_type)
        value_in_python = value1.value_in_python / value2.value_in_python
        value.assign_value_in_python(value_in_python)
        return value

    def debug_output():
        DebugOutput.output("/")


class OperatorEqual(Operator):
    priority = 1

    def operate(value1: Value, value2: Value) -> Value:
        if value1.value_type == value2.value_type:
            value_in_python = value1.value_in_python == value2.value_in_python
            value = Value(ValueType.BOOL)
            value.assign_value_in_python(value_in_python)
            return value
        return None

    def debug_output():
        DebugOutput.output("=")


class OperatorLargerThan(Operator):
    priority = 1

    def operate(value1: Value, value2: Value) -> Value:
        if value1.value_type == value2.value_type:
            value_in_python = value1.value_in_python > value2.value_in_python
            value = Value(ValueType.BOOL)
            value.assign_value_in_python(value_in_python)
            return value
        return None

    def debug_output():
        DebugOutput.output(">")

class OperatorSmallerThan(Operator):
    priority = 1

    def operate(value1: Value, value2: Value) -> Value:
        if value1.value_type == value2.value_type:
            value_in_python = value1.value_in_python < value2.value_in_python
            value = Value(ValueType.BOOL)
            value.assign_value_in_python(value_in_python)
            return value
        return None

    def debug_output():
        DebugOutput.output("<")


def convert_token_to_operator(operator_token: Tree) -> Operator:
    if operator_token == "operator_add":
        return OperatorAdd
    if operator_token == "operator_minus":
        return OperatorMinus
    if operator_token == "operator_multiple":
        return OperatorMultiple
    if operator_token == "operator_divide":
        return OperatorDivide
    if operator_token == "operator_equal":
        return OperatorEqual
    if operator_token == "operator_largerthan":
        return OperatorLargerThan
    if operator_token == "operator_smallerthan":
        return OperatorSmallerThan
    return Operator
