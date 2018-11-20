from lark import Lark

pse_parser = Lark(r"""
    blocks: block+
    ?block: debug_block
        | declare_block
        | type_block
        | assign_block
        | decision_block
        | output_block
        | input_block
        | repeat_block
        | while_block
        | for_block
        | procedure_block
        | call_procedure_block
        | function_block
        | return_block

    debug_block: "DEBUG"

    declare_block: "DECLARE" symbol ":" type
    type_block: "TYPE" symbol blocks "ENDTYPE"
    assign_block: key "<-" expression

    output_block: "OUTPUT" expression
    input_block: "INPUT" key

    decision_block: decision_if_branch decision_else_branch? decision_endif
    decision_if_branch: "IF" expression "THEN" blocks
    decision_else_branch: "ELSE" blocks
    decision_endif: "ENDIF"

    repeat_block: "REPEAT" blocks "UNTIL" expression
    while_block: "WHILE" expression "DO" blocks "ENDWHILE"

    for_block: "FOR" key "<-" for_start_exp "TO" for_end_exp blocks "ENDFOR"
    for_start_exp: expression
    for_end_exp: expression

    function_block: "FUNCTION" symbol "(" function_block_params ")" "RETURNS" type blocks "ENDFUNCTION"
    procedure_block: "PROCEDURE" symbol "(" function_block_params ")" blocks "ENDPROCEDURE"
    function_block_params: function_block_param ("," function_block_param)*
    function_block_param: symbol ":" type

    return_block: "RETURN" expression

    call_procedure_block: "CALL" key "(" function_params ")"
    function_call: key "(" function_params ")"
    function_params: expression ("," expression)*

    key: key_item child_key_item*
    ?child_key_item: "." key_item
    key_item: symbol  ("[" array_index "]")?
    array_index: int

    expression: item operation*
    operation: operator item
    ?item: value | key | function_call | branched_expression
    ?branched_expression: "(" expression ")"

    ?operator: operator_add
        | operator_minus
        | operator_multiple
        | operator_divide
        | operator_equal
        | operator_largerthan
        | operator_largerorequalto
        | operator_smallerthan
        | operator_smallerorequalto
        operator_add: "+"
        operator_minus: "-"
        operator_multiple: "*"
        operator_divide: "/"
        operator_equal: "="
        operator_largerthan: ">"
        operator_largerorequalto: ">="
        operator_smallerthan: "<"
        operator_smallerorequalto: "<="

    symbol : CNAME

    value: int
        | real
        | string
    type: type_int
        | type_real
        | type_string
        | type_bool
        | type_array
        | type_custom
    type_int: "INT"
    type_real: "REAL"
    type_string: "STRING"
    type_bool: "BOOL"
    type_array: "ARRAY" "[" type_array_start_index ".." type_array_end_index "]" "OF" type
        type_array_start_index: int
        type_array_end_index: int
    type_custom: symbol

    string: ESCAPED_STRING
    int: [SIGNED_INT | INT]
    real: [SIGNED_FLOAT | FLOAT]
    bool: "TRUE" -> true
        | "FALSE" -> false

    %import common.CNAME
    %import common.ESCAPED_STRING
    %import common.INT
    %import common.SIGNED_INT
    %import common.FLOAT
    %import common.SIGNED_FLOAT
    %import common.NEWLINE
    %import common.WS
    %ignore WS
    """, start='blocks')


def parse_file_to_token(file):
    file_text = file.read()
    tree = pse_parser.parse(file_text)
    return tree

