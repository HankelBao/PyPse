from lark import Tree
from .values import ValueType, Value
from .operators import Operator, OperatorAdd, OperatorMinus, OperatorMultiple, OperatorDivide, OperatorEqual, OperatorLargerThan, OperatorSmallerThan
from . import blocks


def token_find_data(token: Tree, name: str):
    for child_token in token.children:
        if child_token.data == name:
            return child_token


def convert_param_tokens_to_param_items(params_token: Tree):
    param_items = []
    for param_token in params_token.children:
        if param_token.data == "function_block_param":
            symbol_token = token_find_data(param_token, "symbol")
            type_token = token_find_data(param_token, "type")

            param_name = convert_symbol_token_to_symbol_name(symbol_token)
            param_type = convert_token_to_valuetype(type_token)

        param_item = {
            "param_name": param_name,
            "param_type": param_type,
        }
        param_items.append(param_item)
    return param_items


def convert_symbol_token_to_symbol_name(symbol_token):
    return str(symbol_token.children[0])


def get_symbol_name_from_key_item(key_item: Tree) -> str:
    symbol_token = token_find_data(key_item, "symbol")
    symbol_name = convert_symbol_token_to_symbol_name(symbol_token)
    return symbol_name


def get_array_index_exp_token_from_key_item(key_item: Tree):
    array_index_exp_token = token_find_data(key_item, "array_index")
    return array_index_exp_token


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
    if valuetype_str == "type_array":
        return ValueType.ARRAY
    if valuetype_str == "type_custom":
        # It's utilization of type, not declaration
        # The specific type needs to be determined by the symbols in the block
        return ValueType.CUSTOM_TYPE
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


def convert_value_in_python_to_valuetpye(value_in_python) -> ValueType:
    if type(value_in_python) == str:
        return ValueType.STRING
    if type(value_in_python) == int:
        return ValueType.INT
    if type(value_in_python) == float:
        return ValueType.REAL
    if isinstance(value_in_python, blocks.TypeBlock):
        return value_in_python


def get_custom_type_name_from_type_token(type_token: Tree) -> str:
    symbol_token = type_token.children[0].children[0]
    symbol_name = convert_symbol_token_to_symbol_name(symbol_token)
    return str(symbol_name)


def get_array_info_from_token(type_token: Tree) -> (int, int, ValueType):
    type_array_token = type_token.children[0]
    array_start_index_token = token_find_data(
        type_array_token, "type_array_start_index")
    array_start_index = int(convert_token_to_value(
        array_start_index_token).value_in_python)
    array_end_index_token = token_find_data(
        type_array_token, "type_array_end_index")
    array_end_index = int(convert_token_to_value(
        array_end_index_token).value_in_python)
    valuetype_token = token_find_data(type_array_token, "type")
    valuetype = convert_token_to_valuetype(valuetype_token)
    return array_start_index, array_end_index, valuetype


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
