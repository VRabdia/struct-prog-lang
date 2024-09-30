<<<<<<< HEAD
"""
parser.py -- implement parser for simple expressions

Accept a string of tokens, return an AST expressed as stack of dictionaries
"""
=======
# BNF
# value = 1
# value = (value)

# EBNF
# value = 1 | (value)

#
# expr = <number>
# expr = <number> + expr

#
# expr = term | term ("+" | "-") term
# term = factor | factor ("*" | "/") factor
# factor = number | (expr) | -factor

"""
parser.py -- implement parser for simple expressions

Accept a string of tokens, return an AST expressed as a stack of dictionaries
"""

>>>>>>> 575be92 (Added identifiers)
"""
    simple_expression = number | identifier | "(" expression ")" | "-" simple_expression
    factor = simple_expression
    term = factor { "*"|"/" factor }
    arithmetic_expression = term { "+"|"-" term }
<<<<<<< HEAD
    comparison_expression == arithmetic_expression [ "==" | "!=" | "<" | ">" | "<=" | ">="  arithmetic expression ]
    boolean_term == comparison_expression { "&&" comparison_expression }
    boolean_expression == boolean_term { "||" boolean_term }
    expression = boolean_expression
    print_statement = "print" "(" expression ")"
    assignment_statement = expression
    statement = print_statement |
                assignment_expression
"""

from pprint import pprint

from tokenizer import tokenize

=======
    comparison_expression = arithmetic_expression [ "==" | "!=" | "<" | ">" | "<=" | ">=" arithmetic_expression]
    boolean_term = comparison_expression {"&&" comparison_expression}
    boolean_expression = boolean_term {"||" boolean_term}
    expression = comparison_expression
    print_statement = "print" "(" expression ")"
    assignment_statement = expression
    statement = print_statement |
                assignment_statement
"""


from pprint import pprint
from tokenizer import tokenize


>>>>>>> 575be92 (Added identifiers)
def parse_simple_expression(tokens):
    """
    simple_expression = number | identifier | "(" expression ")" | "-" simple_expression
    """
    if tokens[0]["tag"] == "number":
        return tokens[0], tokens[1:]
    if tokens[0]["tag"] == "identifier":
        return tokens[0], tokens[1:]
    if tokens[0]["tag"] == "(":
<<<<<<< HEAD
        node, tokens = parse_expression(tokens[1:])
        assert tokens[0]["tag"] == ")", "Error: expected ')'"
        return node, tokens[1:]
    if tokens[0]["tag"] == "-":
        node, tokens = parse_simple_expression(tokens[1:])
        node = {"tag":"negate", "value":node}
=======
        node, tokens = parse_arithmetic_expression(tokens[1:])
        assert tokens[0]["tag"] == ")", "Error: Expected ')'"
        return node, tokens[1:]
    if tokens[0]["tag"] == "-":
        node, tokens = parse_simple_expression(tokens[1:])
        node = {"tag": "negate", "value": node}
>>>>>>> 575be92 (Added identifiers)
        return node, tokens


def test_parse_simple_expression():
    """
    simple_expression = number | identifier | "(" expression ")" | "-" simple_expression
    """
<<<<<<< HEAD
    print("testing parse_simple_expression")
=======
    print("Testing parse_simple_expression...")
    #
>>>>>>> 575be92 (Added identifiers)
    tokens = tokenize("2")
    ast, tokens = parse_simple_expression(tokens)
    assert ast["tag"] == "number"
    assert ast["value"] == 2
<<<<<<< HEAD
    tokens = tokenize("X")
    ast, tokens = parse_simple_expression(tokens)
    assert ast["tag"] == "identifier"
    assert ast["value"] == "X"
    # pprint(ast)
=======
    # pprint(ast)
    #
>>>>>>> 575be92 (Added identifiers)
    tokens = tokenize("(2)")
    ast, tokens = parse_simple_expression(tokens)
    assert ast["tag"] == "number"
    assert ast["value"] == 2
    # pprint(ast)
<<<<<<< HEAD
=======
    #
>>>>>>> 575be92 (Added identifiers)
    tokens = tokenize("-2")
    ast, tokens = parse_simple_expression(tokens)
    assert ast == {
        "tag": "negate",
        "value": {"position": 1, "tag": "number", "value": 2},
    }
    # pprint(ast)
<<<<<<< HEAD
=======
    #
>>>>>>> 575be92 (Added identifiers)
    tokens = tokenize("-(2)")
    ast, tokens = parse_simple_expression(tokens)
    assert ast == {
        "tag": "negate",
        "value": {"position": 2, "tag": "number", "value": 2},
    }
    # pprint(ast)
<<<<<<< HEAD
=======
    #
    tokens = tokenize("(-(7))")
    ast, tokens = parse_simple_expression(tokens)
    assert ast == {
        "tag": "negate",
        "value": {"position": 3, "tag": "number", "value": 7},
    }
    # pprint(ast)
    tokens = tokenize("-10")
    ast, tokens = parse_simple_expression(tokens)
    assert ast == {
        "tag": "negate",
        "value": {"position": 1, "tag": "number", "value": 10},
    }
    # pprint(ast)
    #
    tokens = tokenize("x")
    ast, tokens = parse_simple_expression(tokens)
    assert ast["tag"] == "identifier"
    assert ast["value"] == "x"
    # pprint(ast)
    #
    tokens = tokenize("X")
    ast, tokens = parse_simple_expression(tokens)
    assert ast["tag"] == "identifier"
    assert ast["value"] == "X"
    # pprint(ast)
    #
    tokens = tokenize("-(2)")
    ast, tokens = parse_simple_expression(tokens)
    # assert ast["tag"] == "identifier"
    # assert ast["value"] == "X"
    pprint(ast)
    print(tokens)

>>>>>>> 575be92 (Added identifiers)

def parse_factor(tokens):
    """
    factor = simple_expression
    """
    return parse_simple_expression(tokens)

<<<<<<< HEAD
def test_parse_factor():
    """
    factor = simple_expression
    """
    print("testing parse_factor")
    for s in ["2", "(2)", "-2"]:
=======

def test_parse_factor():
    print("Testing parse_factor...")
    for s in ["2", "(2)", "-2", "(-(5))", "-10", "20", "-9"]:
>>>>>>> 575be92 (Added identifiers)
        assert parse_factor(tokenize(s)) == parse_simple_expression(tokenize(s))


def parse_term(tokens):
    """
    term = factor { "*"|"/" factor }
    """
    node, tokens = parse_factor(tokens)
    while tokens[0]["tag"] in ["*", "/"]:
        tag = tokens[0]["tag"]
        right_node, tokens = parse_factor(tokens[1:])
        node = {"tag": tag, "left": node, "right": right_node}
    return node, tokens


def test_parse_term():
    """
    term = factor { "*"|"/" factor }
    """
<<<<<<< HEAD
    print("testing parse_term")
    tokens = tokenize("2*3")
    ast, tokens = parse_term(tokens)
    assert ast == {'left': {'position': 0, 'tag': 'number', 'value': 2},'right': {'position': 2, 'tag': 'number', 'value': 3},'tag': '*'}    
=======
    print("Testing parse_term...")
    #
    tokens = tokenize("2*3")
    ast, tokens = parse_term(tokens)
    assert ast == {
        "left": {"position": 0, "tag": "number", "value": 2},
        "right": {"position": 2, "tag": "number", "value": 3},
        "tag": "*",
    }
    #
>>>>>>> 575be92 (Added identifiers)
    tokens = tokenize("2*3/4*5")
    ast, tokens = parse_term(tokens)
    assert ast == {
        "left": {
            "left": {
                "left": {"position": 0, "tag": "number", "value": 2},
                "right": {"position": 2, "tag": "number", "value": 3},
                "tag": "*",
            },
            "right": {"position": 4, "tag": "number", "value": 4},
            "tag": "/",
        },
        "right": {"position": 6, "tag": "number", "value": 5},
        "tag": "*",
    }
<<<<<<< HEAD
=======
    # pprint(ast)
    #
    tokens = tokenize("-2*3")
    ast, tokens = parse_term(tokens)
    assert ast == {
        "left": {
            "tag": "negate",
            "value": {"position": 1, "tag": "number", "value": 2},
        },
        "right": {"position": 3, "tag": "number", "value": 3},
        "tag": "*",
    }
    # pprint(ast)
    #
    tokens = tokenize("7/3*-2*3/-5")
    ast, tokens = parse_term(tokens)
    assert ast == {
        "left": {
            "left": {
                "left": {
                    "left": {"position": 0, "tag": "number", "value": 7},
                    "right": {"position": 2, "tag": "number", "value": 3},
                    "tag": "/",
                },
                "right": {
                    "tag": "negate",
                    "value": {"position": 5, "tag": "number", "value": 2},
                },
                "tag": "*",
            },
            "right": {"position": 7, "tag": "number", "value": 3},
            "tag": "*",
        },
        "right": {
            "tag": "negate",
            "value": {"position": 10, "tag": "number", "value": 5},
        },
        "tag": "/",
    }
    # pprint(ast)
>>>>>>> 575be92 (Added identifiers)


def parse_arithmetic_expression(tokens):
    """
    arithmetic_expression = term { "+"|"-" term }
    """
    node, tokens = parse_term(tokens)
    while tokens[0]["tag"] in ["+", "-"]:
        tag = tokens[0]["tag"]
        right_node, tokens = parse_term(tokens[1:])
        node = {"tag": tag, "left": node, "right": right_node}
    return node, tokens


def test_parse_arithmetic_expression():
    """
    arithmetic_expression = term { "+"|"-" term }
    """
<<<<<<< HEAD
    print("testing parse_arithmetic_expression")
=======
    print("Testing parse_arithmetic_expression...")
    #
>>>>>>> 575be92 (Added identifiers)
    tokens = tokenize("2+3")
    ast, tokens = parse_arithmetic_expression(tokens)
    assert ast == {
        "left": {"position": 0, "tag": "number", "value": 2},
        "right": {"position": 2, "tag": "number", "value": 3},
        "tag": "+",
    }
<<<<<<< HEAD
=======
    #
>>>>>>> 575be92 (Added identifiers)
    tokens = tokenize("2+3-4+5")
    ast, tokens = parse_arithmetic_expression(tokens)
    assert ast == {
        "left": {
            "left": {
                "left": {"position": 0, "tag": "number", "value": 2},
                "right": {"position": 2, "tag": "number", "value": 3},
                "tag": "+",
            },
            "right": {"position": 4, "tag": "number", "value": 4},
            "tag": "-",
        },
        "right": {"position": 6, "tag": "number", "value": 5},
        "tag": "+",
    }
<<<<<<< HEAD
=======
    #
>>>>>>> 575be92 (Added identifiers)
    tokens = tokenize("2+3*4+5")
    ast, tokens = parse_arithmetic_expression(tokens)
    assert ast == {
        "left": {
            "left": {"position": 0, "tag": "number", "value": 2},
            "right": {
                "left": {"position": 2, "tag": "number", "value": 3},
                "right": {"position": 4, "tag": "number", "value": 4},
                "tag": "*",
            },
            "tag": "+",
        },
        "right": {"position": 6, "tag": "number", "value": 5},
        "tag": "+",
    }
<<<<<<< HEAD

def parse_comparison_expression(tokens):
    """
    comparison_expression == arithmetic_expression [ "==" | "!=" | "<" | ">" | "<=" | ">="  arithmetic expression ]
    """
    node, tokens = parse_arithmetic_expression(tokens)
    if tokens[0]["tag"] in ["==", "!=", "<=", ">=", "<", ">"]:
=======
    # pprint(ast)
    #
    tokens = tokenize("-3*5-2/7")
    ast, tokens = parse_arithmetic_expression(tokens)
    assert ast == {
        "left": {
            "left": {
                "tag": "negate",
                "value": {"position": 1, "tag": "number", "value": 3},
            },
            "right": {"position": 3, "tag": "number", "value": 5},
            "tag": "*",
        },
        "right": {
            "left": {"position": 5, "tag": "number", "value": 2},
            "right": {"position": 7, "tag": "number", "value": 7},
            "tag": "/",
        },
        "tag": "-",
    }
    # pprint(ast)
    #
    tokens = tokenize("10-8/5*4-26/45*23-5+1")
    ast, tokens = parse_arithmetic_expression(tokens)
    assert ast == {
        "left": {
            "left": {
                "left": {
                    "left": {"position": 0, "tag": "number", "value": 10},
                    "right": {
                        "left": {
                            "left": {"position": 3, "tag": "number", "value": 8},
                            "right": {"position": 5, "tag": "number", "value": 5},
                            "tag": "/",
                        },
                        "right": {"position": 7, "tag": "number", "value": 4},
                        "tag": "*",
                    },
                    "tag": "-",
                },
                "right": {
                    "left": {
                        "left": {"position": 9, "tag": "number", "value": 26},
                        "right": {"position": 12, "tag": "number", "value": 45},
                        "tag": "/",
                    },
                    "right": {"position": 15, "tag": "number", "value": 23},
                    "tag": "*",
                },
                "tag": "-",
            },
            "right": {"position": 18, "tag": "number", "value": 5},
            "tag": "-",
        },
        "right": {"position": 20, "tag": "number", "value": 1},
        "tag": "+",
    }
    # pprint(ast)


def parse_comparison_expression(tokens):
    """
    comparison_expression = arithmetic_expression [ "==" | "!=" | "<" | ">" | "<=" | ">=" arithmetic_expression]
    """
    node, tokens = parse_arithmetic_expression(tokens)
    while tokens[0]["tag"] in ["==", "!=", "<=", ">=", "<", ">"]:
>>>>>>> 575be92 (Added identifiers)
        tag = tokens[0]["tag"]
        right_node, tokens = parse_arithmetic_expression(tokens[1:])
        node = {"tag": tag, "left": node, "right": right_node}
    return node, tokens

<<<<<<< HEAD
def test_parse_comparison_expression():
    """
    comparison_expression == arithmetic_expression [ "==" | "!=" | "<" | ">" | "<=" | ">="  arithmetic expression ]
    """
    print("testing parse_comparison_expression")
    for op in ["<",">"]:
=======

def test_parse_comparison_expression():
    """
    comparison_expression = arithmetic_expression [ "==" | "!=" | "<" | ">" | "<=" | ">=" arithmetic_expression]
    """
    print("Testing parse_comparison_expression...")
    #
    for op in ["<", ">"]:
>>>>>>> 575be92 (Added identifiers)
        tokens = tokenize(f"2{op}3")
        ast, tokens = parse_comparison_expression(tokens)
        assert ast == {
            "left": {"position": 0, "tag": "number", "value": 2},
            "right": {"position": 2, "tag": "number", "value": 3},
            "tag": op,
        }
<<<<<<< HEAD
    for op in ["==", ">=", "<=", "!="]:
=======
    #
    for op in ["<=", ">=", "!=", "=="]:
>>>>>>> 575be92 (Added identifiers)
        tokens = tokenize(f"2{op}3")
        ast, tokens = parse_comparison_expression(tokens)
        assert ast == {
            "left": {"position": 0, "tag": "number", "value": 2},
            "right": {"position": 3, "tag": "number", "value": 3},
            "tag": op,
        }
<<<<<<< HEAD

def parse_boolean_term(tokens):
    """
    boolean_term == comparison_expression { "and" comparison_expression }
=======
    #
    tokens = tokenize("2<3")
    ast, tokens = parse_comparison_expression(tokens)
    assert ast == {
        "left": {"position": 0, "tag": "number", "value": 2},
        "right": {"position": 2, "tag": "number", "value": 3},
        "tag": "<",
    }
    # pprint(ast)
    #
    tokens = tokenize("2==3")
    ast, tokens = parse_comparison_expression(tokens)
    assert ast == {
        "left": {"position": 0, "tag": "number", "value": 2},
        "right": {"position": 3, "tag": "number", "value": 3},
        "tag": "==",
    }
    # pprint(ast)


def parse_boolean_term(tokens):
    """
    boolean_term = comparison_expression {"&&" comparison_expression}
>>>>>>> 575be92 (Added identifiers)
    """
    node, tokens = parse_comparison_expression(tokens)
    while tokens[0]["tag"] in ["&&"]:
        tag = tokens[0]["tag"]
        right_node, tokens = parse_comparison_expression(tokens[1:])
        node = {"tag": tag, "left": node, "right": right_node}
    return node, tokens

<<<<<<< HEAD
def test_parse_boolean_term():
    print("testing parse_boolean_term")
    for op in ["<",">"]:
=======

def test_parse_boolean_term():
    """
    boolean_term = comparison_expression {"&&" comparison_expression}
    """
    print("Testing parse_boolean_term...")
    #
    for op in ["<", ">"]:
>>>>>>> 575be92 (Added identifiers)
        tokens = tokenize(f"2{op}3")
        ast, tokens = parse_boolean_term(tokens)
        assert ast == {
            "left": {"position": 0, "tag": "number", "value": 2},
            "right": {"position": 2, "tag": "number", "value": 3},
            "tag": op,
        }
<<<<<<< HEAD
    tokens = tokenize(f"2&&3")
    ast, tokens = parse_boolean_term(tokens)
    assert ast == {
        "tag": "&&",
        "left": {"tag": "number", "value": 2, "position": 0},
        "right": {"tag": "number", "value": 3, "position": 3},
    }

def parse_boolean_expression(tokens):
    """
    boolean_expression == boolean_term { "||" boolean_term }
=======
    #
    tokens = tokenize(f"2&&3")
    ast, tokens = parse_boolean_term(tokens)
    assert ast == {
        "left": {"position": 0, "tag": "number", "value": 2},
        "right": {"position": 3, "tag": "number", "value": 3},
        "tag": "&&",
    }
    # pprint(ast)


def parse_boolean_expression(tokens):
    """
    boolean_expression = boolean_term {"||" boolean_term}
>>>>>>> 575be92 (Added identifiers)
    """
    node, tokens = parse_boolean_term(tokens)
    while tokens[0]["tag"] in ["||"]:
        tag = tokens[0]["tag"]
        right_node, tokens = parse_boolean_term(tokens[1:])
        node = {"tag": tag, "left": node, "right": right_node}
    return node, tokens


def test_parse_boolean_expression():
<<<<<<< HEAD
    print("testing parse_boolean_expression")
    for op in ["<",">"]:
=======
    """
    boolean_expression = boolean_term {"||" boolean_term}
    """
    print("Testing parse_boolean_expression...")
    #
    for op in ["<", ">"]:
>>>>>>> 575be92 (Added identifiers)
        tokens = tokenize(f"2{op}3")
        ast, tokens = parse_boolean_expression(tokens)
        assert ast == {
            "left": {"position": 0, "tag": "number", "value": 2},
            "right": {"position": 2, "tag": "number", "value": 3},
            "tag": op,
        }
<<<<<<< HEAD
    tokens = tokenize(f"2||3")
    ast, tokens = parse_boolean_expression(tokens)
    assert ast == {
        "tag": "||",
        "left": {"tag": "number", "value": 2, "position": 0},
        "right": {"tag": "number", "value": 3, "position": 3},
    }
=======
    #
    tokens = tokenize(f"2||3")
    ast, tokens = parse_boolean_expression(tokens)
    assert ast == {
        "left": {"position": 0, "tag": "number", "value": 2},
        "right": {"position": 3, "tag": "number", "value": 3},
        "tag": "||",
    }
    # pprint(ast)
>>>>>>> 575be92 (Added identifiers)


def parse_expression(tokens):
    """
    expression = boolean_expression
    """
    return parse_boolean_expression(tokens)

<<<<<<< HEAD
def test_parse_expression():
    print("testing parse_expression")
=======

def test_parse_expression():
    print("Testing parse_expression...")
>>>>>>> 575be92 (Added identifiers)
    tokens = tokenize("4>2+3||4&&5")
    ast1, _ = parse_expression(tokens)
    ast2, _ = parse_boolean_expression(tokens)
    assert ast1 == ast2

<<<<<<< HEAD
=======

>>>>>>> 575be92 (Added identifiers)
def parse_print_statement(tokens):
    """
    print_statement = "print" "(" expression ")"
    """
    assert tokens[0]["tag"] == "print"
    assert tokens[1]["tag"] == "("
    tokens = tokens[2:]
    if tokens[0]["tag"] != ")":
        expression, tokens = parse_expression(tokens)
    else:
        expression = None
    assert tokens[0]["tag"] == ")"
    node = {
<<<<<<< HEAD
        "tag":"print",
        "value":expression,
    }
    return node, tokens[1:]

=======
        "tag": "print",
        "value": expression,
    }
    return node, tokens[1:]


>>>>>>> 575be92 (Added identifiers)
def test_parse_print_statement():
    """
    print_statement = "print" "(" expression ")"
    """
<<<<<<< HEAD
    print("testing parse_print_statement")
=======
    print("Testing parse_statement...")
    #
>>>>>>> 575be92 (Added identifiers)
    tokens = tokenize("print(1)")
    ast, tokens = parse_print_statement(tokens)
    assert ast == {
        "tag": "print",
        "value": {"tag": "number", "value": 1, "position": 6},
    }
<<<<<<< HEAD
    tokens = tokenize("print()")
    ast, tokens = parse_print_statement(tokens)
    assert ast == {
        "tag": "print",
        "value": None,
    }
=======
    #
    tokens = tokenize("print()")
    ast, tokens = parse_print_statement(tokens)
    assert ast == {"tag": "print", "value": None}
    # pprint(ast)

>>>>>>> 575be92 (Added identifiers)

def parse_assignment_statement(tokens):
    """
    assignment_statement = expression
    """
<<<<<<< HEAD
    node ,tokens = parse_expression(tokens)
=======
    node, tokens = parse_expression(tokens)
>>>>>>> 575be92 (Added identifiers)
    if tokens[0]["tag"] == "=":
        tag = tokens[0]["tag"]
        value, tokens = parse_expression(tokens[1:])
        node = {"tag": tag, "target": node, "value": value}
    return node, tokens

<<<<<<< HEAD
def test_parse_assignment_statement():
    """
    assignment_statement = expression
    """
    print("testing parse_assignment_statement")
=======

def test_parse_assignment_statement():
    print("Testing parse_assignment_statement...")
    #
>>>>>>> 575be92 (Added identifiers)
    tokens = tokenize("2+3*4+5")
    ast1, _ = parse_expression(tokens)
    ast2, _ = parse_assignment_statement(tokens)
    assert ast1 == ast2
<<<<<<< HEAD
=======
    #
>>>>>>> 575be92 (Added identifiers)
    tokens = tokenize("3=4")
    ast, _ = parse_assignment_statement(tokens)
    assert ast == {
        "tag": "=",
        "target": {"tag": "number", "value": 3, "position": 0},
        "value": {"tag": "number", "value": 4, "position": 2},
    }
<<<<<<< HEAD
=======
    # pprint(ast)

>>>>>>> 575be92 (Added identifiers)

def parse_statement(tokens):
    """
    statement = print_statement |
                assignment_statement
    """
    if tokens[0]["tag"] == "print":
<<<<<<< HEAD
        return parse_print_statement(tokens) 
    return parse_assignment_statement(tokens)   

def test_parse_statement():
    print("testing parse_statement")
    tokens = tokenize("2+3*4+5")
    assert parse_statement(tokens) == parse_expression(tokens)

def parse(tokens):
    ast, tokens = parse_statement(tokens)
    return ast 

def test_parse():
    print("testing parse")
    tokens = tokenize("2+3*4+5")
    ast, _ = parse_statement(tokens)
    assert parse(tokens) == ast
    tokens = tokenize("1*2<3*4||5>6&&7")
    ast = parse(tokens)
    assert ast == {
        "tag": "||",
        "left": {
            "tag": "<",
            "left": {
                "tag": "*",
                "left": {"tag": "number", "value": 1, "position": 0},
                "right": {"tag": "number", "value": 2, "position": 2},
            },
            "right": {
                "tag": "*",
                "left": {"tag": "number", "value": 3, "position": 4},
                "right": {"tag": "number", "value": 4, "position": 6},
            },
        },
        "right": {
            "tag": "&&",
            "left": {
                "tag": ">",
                "left": {"tag": "number", "value": 5, "position": 9},
                "right": {"tag": "number", "value": 6, "position": 11},
            },
            "right": {"tag": "number", "value": 7, "position": 14},
        },
=======
        return parse_print_statement(tokens)
    return parse_assignment_statement(tokens)


def test_parse_statement():
    print("Testing parse_statement...")
    #
    tokens = tokenize("2+3*4+5")
    ast, _ = parse_statement(tokens)
    assert parse_statement(tokens) == parse_expression(tokens)
    assert parse(tokens) == ast


def parse(tokens):
    ast, tokens = parse_statement(tokens)
    return ast


def test_parse():
    print("Testing parse...")
    #
    tokens = tokenize("2+3*4+5")
    ast, _ = parse_statement(tokens)
    assert parse(tokens) == ast
    #
    tokens = tokenize("1*2<3*4||5>6&&7")
    ast = parse(tokens)
    assert ast == {
        "left": {
            "left": {
                "left": {"position": 0, "tag": "number", "value": 1},
                "right": {"position": 2, "tag": "number", "value": 2},
                "tag": "*",
            },
            "right": {
                "left": {"position": 4, "tag": "number", "value": 3},
                "right": {"position": 6, "tag": "number", "value": 4},
                "tag": "*",
            },
            "tag": "<",
        },
        "right": {
            "left": {
                "left": {"position": 9, "tag": "number", "value": 5},
                "right": {"position": 11, "tag": "number", "value": 6},
                "tag": ">",
            },
            "right": {"position": 14, "tag": "number", "value": 7},
            "tag": "&&",
        },
        "tag": "||",
>>>>>>> 575be92 (Added identifiers)
    }


if __name__ == "__main__":
    test_parse_simple_expression()
    test_parse_factor()
    test_parse_term()
    test_parse_arithmetic_expression()
    test_parse_comparison_expression()
    test_parse_boolean_term()
    test_parse_boolean_expression()
    test_parse_expression()
    test_parse_print_statement()
    test_parse_assignment_statement()
    test_parse_statement()
    test_parse()
<<<<<<< HEAD
    print("done")
=======
    print("Done.")
>>>>>>> 575be92 (Added identifiers)
