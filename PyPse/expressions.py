from .values import Value, ValueType
from .operations import Operation, BasicOperationTypes, OperationTypeLeftBracket, OperationTypeRightBracket
from .values import Value, ValueType, is_number, is_type
from .keys import Key
import copy

class Expression():
    def __init__(self, exp_str: str, block):
        self.exp_str = exp_str
        self.block = block
        exp_items = [exp_str]
        def divide_by_first_appearance(item: str, divider: str) -> (str, str):
            left_exp = item[:item.index(divider)].strip()
            right_exp = item[item.index(divider)+1:].strip()
            return left_exp, right_exp

        def replace_str_with_items(left_exp: str, operation: Operation, right_exp: str, index: int):
            def combine_replaced_items(left_exp: str, operation: Operation, right_exp: str) -> list:
                replaced_items = []
                if left_exp:
                    replaced_items.append(left_exp)
                replaced_items.append(operation)
                if right_exp:
                    replaced_items.append(right_exp)
                return replaced_items

            replaced_items = combine_replaced_items(left_exp, operation, right_exp)
            exp_items[index:index+1] = replaced_items

        # Deal with basic operations
        def divide_item_list_by_basic_operation_once() -> bool:
            for index, exp_item in enumerate(exp_items):
                if type(exp_item) == str:
                    for OperationType in BasicOperationTypes:
                        if OperationType.identifier in exp_item:
                            left_exp, right_exp = divide_by_first_appearance(exp_item, OperationType.identifier)

                            operation = Operation(OperationType)
                            operation.increase_priority(OperationType.priority)

                            replace_str_with_items(left_exp, operation, right_exp, index)
                            return True
            return False

        correction_exist = True
        while correction_exist:
            correction_exist = divide_item_list_by_basic_operation_once()

        # Deal with Brackets
        degree_increase_for_brackets = 0
        for index, exp_item in enumerate(exp_items):
            if type(exp_item) == str:
                number_of_left_operation_brackets = 0
                number_of_right_operation_brackets = 0

                for character in exp_item:
                    if character != OperationTypeLeftBracket.identifier:
                        break
                    number_of_left_operation_brackets += 1
                for character in exp_item[::-1]:
                    if character != OperationTypeRightBracket.identifier:
                        break
                    number_of_right_operation_brackets += 1

                degree_increase_for_brackets += OperationTypeLeftBracket.priority * number_of_left_operation_brackets
                degree_increase_for_brackets += OperationTypeRightBracket.priority * number_of_right_operation_brackets

                if number_of_right_operation_brackets == 0:
                    exp_items[index] = exp_item[number_of_left_operation_brackets:]
                else:
                    exp_items[index] = exp_item[number_of_left_operation_brackets: -number_of_right_operation_brackets]

            if type(exp_item) == Operation:
                exp_item.priority += degree_increase_for_brackets

        # Get Rid of the spaces
        for index, exp_item in enumerate(exp_items):
            if type(exp_item) == str:
               exp_items[index] = exp_item.strip()


        self.exp_items = exp_items

    def if_valid(self) -> bool:
        return True

    def get_value(self) -> Value:
        # Warning: When Getting Value, We shouldn't affect the origin items
        exp_items = copy.deepcopy(self.exp_items)

        # Convert the rest strings into value or variable
        for index, exp_item in enumerate(exp_items):
            if type(exp_item) == str:
                if is_number(exp_item):
                    if is_type(exp_item, int):
                        value = Value(ValueType.INT)
                        value.assign_value_in_python(int(exp_item))
                        exp_items[index] = value
                else:
                    symbol = Key(exp_item, self.block).get_symbol()
                    value = symbol.symbol_value
                    exp_items[index] = value

        def calculate_highest_operation_once():
            max_priority = 0
            max_priority_index = 0

            for index, exp_item in enumerate(exp_items):
                if type(exp_item) == Operation:
                    if exp_item.priority > max_priority:
                        max_priority_index = index
                        max_priority = exp_item.priority

            left_item = exp_items[max_priority_index-1]
            highest_priority_operation = exp_items[max_priority_index]
            right_item = exp_items[max_priority_index+1]

            result_value = highest_priority_operation.OperationType.operate(left_item, right_item)
            exp_items[max_priority_index-1: max_priority_index+2] = [result_value]

        while len(exp_items) > 1:
            calculate_highest_operation_once()

        return exp_items[0]

    def __repr__(self):
        return f"Expression Str: {self.exp_str}, Value: {self.get_value()}"
