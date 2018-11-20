from lark import Tree
from enum import Enum, auto
from copy import deepcopy
from .values import Value, ValueType
from .operators import Operator
from .debug import DebugOutput
from .keys import Key
from .converters import token_find_data, convert_token_to_operator, convert_token_to_valuetype, convert_token_to_value


class ItemType(Enum):
    VALUE = auto()
    KEY = auto()
    EXPRESSION = auto()
    FUNCTION = auto()
    CALCULATED = auto()

class Item():
    def __init__(self, token: Tree, scope_block):
        self.scope_block = scope_block
        self.value = None
        self.item_type = None

        if token.data == "value":
            self.item_type = ItemType.VALUE
            value = convert_token_to_value(token)
        if token.data == "expression":
            self.item_type = ItemType.EXPRESSION
            self.expression = Expression(token, self)
            value = self.expression.get_value()
        if token.data == "key":
            self.item_type = ItemType.KEY
            self.key = Key(token, self.scope_block)
            value = self.key.get_value()
        if token.data == "function_call":
            self.item_type = ItemType.FUNCTION
            function_name_token = token_find_data(token, "key")
            function_params_token = token_find_data(token, "function_params")
            param_exps = []
            for expression_token in function_params_token.children:
                if expression_token.data == "expression":
                    param_exp = Expression(expression_token, self)
                    param_exps.append(param_exp)

            function_key = Key(function_name_token, scope_block)
            function_block = function_key.get_value().value_in_python
            function_block.call(param_exps)
            value = function_block.return_value

        self.value = deepcopy(value)

    def get_value(self):
        if self.item_type == ItemType.KEY:
            value = self.key.get_value()
            self.value = deepcopy(value)
        if self.item_type == ItemType.EXPRESSION:
            value = self.expression.get_value()
            self.value = deepcopy(value)
        return self.value

    def set_value(self, value):
        self.item_type = ItemType.CALCULATED
        self.value.assign_value(value)

    def debug_output(self):
        DebugOutput.increase_depth()
        self.value.debug_output()
        DebugOutput.decrease_depth()


class Operation():
    def __init__(self, token: Tree, scope_block):
        if not token:
            return
        operator_str = token.children[0].data
        operator_item_token = token.children[1]
        self.operator = convert_token_to_operator(operator_str)
        self.item = Item(operator_item_token, scope_block)

    def debug_output(self):
        DebugOutput.output("operation:")
        DebugOutput.increase_depth()
        self.operator.debug_output()
        self.item.debug_output()
        DebugOutput.decrease_depth()


class Expression():
    def __init__(self, token: Tree, scope_block):
        self.operations = []
        self.convert_token_to_structure(token, scope_block)

    def convert_token_to_structure(self, token, scope_block):
        head_operation = Operation(None, None)
        head_operation.operator = Operator
        head_operation.item = Item(token.children[0], scope_block)
        self.operations.append(head_operation)

        for operation_token in token.children:
            if operation_token.data != "operation":
                continue
            operation = Operation(operation_token, scope_block)
            self.operations.append(operation)

    def calculate_once(self, operations) -> bool:
        index_of_highest_operation = 0
        highest_priority = 0
        for index, operation in enumerate(operations):
            if operation.operator.priority > highest_priority:
                highest_priority = operation.operator.priority
                index_of_highest_operation = index
        if highest_priority == 0:
            return False
        target_index = index_of_highest_operation
        remain_index = target_index-1

        value1 = operations[remain_index].item.get_value()
        value2 = operations[target_index].item.get_value()
        result_value = operations[target_index].operator.operate(value1, value2)

        operations[remain_index].item.set_value(result_value)
        del operations[target_index]
        return True

    def get_value(self):
        operations = deepcopy(self.operations)
        calculate_required = True
        while calculate_required:
            calculate_required = self.calculate_once(operations)
        return operations[0].item.get_value()

    def debug_output(self):
        DebugOutput.output_block_attr("expression")
        DebugOutput.increase_depth()
        for operation in self.operations:
            operation.debug_output()
        DebugOutput.decrease_depth()
