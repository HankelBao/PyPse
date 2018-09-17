from enum import Enum
from .values import Value, ValueType


class OperationType():
    priority = 0
    identifier = ""

    @staticmethod
    def operate(value1: Value, value2: Value) -> Value:
        pass


class OperationTypeAdd(OperationType):
    priority = 3
    identifier = "+"

    @staticmethod
    def operate(value1: Value, value2: Value) -> Value:
        if value1.value_type == value2.value_type == ValueType.INT:
            sum_value = Value(ValueType.INT)
            sum_value.assign_value_in_python(int(value1.value_in_python + value2.value_in_python))
            return sum_value


class OperationTypeMinus(OperationType):
    priority = 3
    identifier = "-"

    @staticmethod
    def operate(value1: Value, value2: Value) -> Value:
        if value1.value_type == value2.value_type == ValueType.INT:
            sum_value = Value(ValueType.INT)
            sum_value.assign_value_in_python(int(value1.value_in_python - value2.value_in_python))
            return sum_value


class OperationTypeMultiply(OperationType):
    priority = 4
    identifier = "*"

    @staticmethod
    def operate(value1: Value, value2: Value) -> Value:
        if value1.value_type == value2.value_type == ValueType.INT:
            sum_value = Value(ValueType.INT)
            sum_value.assign_value_in_python(int(value1.value_in_python * value2.value_in_python))
            return sum_value


class OperationTypeDivide(OperationType):
    priority = 4
    identifier = "/"

    @staticmethod
    def operate(value1: Value, value2: Value) -> Value:
        if value1.value_type == value2.value_type == ValueType.INT:
            sum_value = Value(ValueType.INT)
            sum_value.assign_value_in_python(int(value1.value_in_python / value2.value_in_python))
            return sum_value

class OperationTypeEqual(OperationType):
    priority = 2
    identifier = "="

    @staticmethod
    def operate(value1: Value, value2: Value) -> Value:
        if value1.value_type == value2.value_type:
            sum_value = Value(ValueType.BOOLEAN)
            sum_value.assign_value_in_python(bool(value1.value_in_python == value2.value_in_python))
            return sum_value


class OperationTypeSmallerThan(OperationType):
    priority = 2
    identifier = "<"

    @staticmethod
    def operate(value1: Value, value2: Value) -> Value:
        if value1.value_type == value2.value_type:
            sum_value = Value(ValueType.BOOLEAN)
            sum_value.assign_value_in_python(bool(value1.value_in_python < value2.value_in_python))
            return sum_value


class OperationTypeLargerThan(OperationType):
    priority = 2
    identifier = ">"

    @staticmethod
    def operate(value1: Value, value2: Value) -> Value:
        if value1.value_type == value2.value_type:
            sum_value = Value(ValueType.BOOLEAN)
            sum_value.assign_value_in_python(bool(value1.value_in_python > value2.value_in_python))
            return sum_value


class OperationTypeLeftBracket(OperationType):
    priority = 10
    identifier = "("


class OperationTypeRightBracket(OperationType):
    priority = -10
    identifier = ")"


class OperationTypeStructureConjuncture(OperationType):
    identifier = "."


class OperationTypeAssign(OperationType):
    identifier = "<-"


class OperationTypeAddBy(OperationType):
    identifier = "+="

    @staticmethod
    def operate(value1: Value, value2: Value) -> Value:
        if value1.value_type == value2.value_type == ValueType.INT:
            value1.value_in_python += value2.value_in_python

class OperationTypeAddByOne(OperationType):
    @staticmethod
    def operate(value1: Value) -> Value:
        ValueOne = Value(ValueType.INT)
        ValueOne.assign_value_in_python(1)
        OperationTypeAddBy.operate(value1, ValueOne)

BasicOperationTypes = [
    OperationTypeAdd,
    OperationTypeMinus,
    OperationTypeMultiply,
    OperationTypeDivide,
    OperationTypeEqual,
    OperationTypeSmallerThan,
    OperationTypeLargerThan
]

class Operation():
    def __init__(self, OperationType):
        self.OperationType = OperationType
        self.priority = 0

    def increase_priority(self, degree: int):
        self.priority += degree

    def __repr__(self):
        return f"Identifier: {self.OperationType.identifier} Priority: {self.priority}"
