from lark import Tree
from .symbols import Symbol, convert_token_to_symbol_name
from .values import convert_token_to_valuetype


def token_find_data(token: Tree, name: str):
    for child_token in token.children:
        if child_token.data == name:
            return child_token


def convert_param_tokens_to_symbols(params_token: Tree):
    symbols = []
    for param_token in params_token.children:
        if param_token.data == "function_block_param":
            symbol_token = token_find_data(param_token, "symbol")
            type_token = token_find_data(param_token, "type")

            param_name = convert_token_to_symbol_name(symbol_token)
            param_type = convert_token_to_valuetype(type_token)

            symbol = Symbol(param_name, param_type)
            symbols.append(symbol)
    return symbols
