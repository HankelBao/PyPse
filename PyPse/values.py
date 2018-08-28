from enum import Enum, auto


class ValueType(Enum):
    INT = auto()
    REAL = auto()
    STRING = auto()
    ARRAY = auto()
    TYPE = auto()


class Value():
    def __init__(self, vtype: ValueType):
        self.vtype = vtype
        self.value = None

    def first_assigned(self):
        return False if self.value is None else True

    def assign(self, value):
        self.value = value
