from tokenizer import tokenize
from parser import parse

<<<<<<< HEAD
def evaluate(ast, environment):
    if ast["tag"] == "number":
        assert type(ast["value"]) in [float, int],f"unexpected numerical type {type(ast["value"])}"
        return ast["value"], False
    if ast["tag"] == "identifier":
        identifier = ast["value"]
        assert identifier in environment, f"ERROR: Unknown Identifier: '{identifier}'"
        if identifier in environment:
            return environment[identifier], False
=======

def evaluate(ast, environment):
    if ast["tag"] == "number":
        assert type(ast["value"]) in [float, int], f"ERROR: unexpected numerical type {type(ast["value"])}"
        return ast["value"], False
    if ast["tag"] == "identifier":
        # assert type(ast["value"]) in [float, int], f"ERROR: unexpected numerical type {type(ast["value"])}"
        return 3.14159, False
>>>>>>> 575be92 (Added identifiers)
    if ast["tag"] == "+":
        left_value, _ = evaluate(ast["left"], environment)
        right_value, _ = evaluate(ast["right"], environment)
        return left_value + right_value, False
    if ast["tag"] == "-":
        left_value, _ = evaluate(ast["left"], environment)
        right_value, _ = evaluate(ast["right"], environment)
        return left_value - right_value, False
    if ast["tag"] == "*":
        left_value, _ = evaluate(ast["left"], environment)
        right_value, _ = evaluate(ast["right"], environment)
        return left_value * right_value, False
    if ast["tag"] == "/":
        left_value, _ = evaluate(ast["left"], environment)
        right_value, _ = evaluate(ast["right"], environment)
<<<<<<< HEAD
        assert right_value != 0, "Division by zero"
        return left_value / right_value, False
    if ast["tag"] == "negate":
        value, _ = evaluate(ast["value"], environment)
=======
        assert right_value != 0, "ERROR: Division by Zero"
        return left_value / right_value, False
    if ast["tag"] == "negate":
        value, _ = evaluate(ast["value"],environment)
>>>>>>> 575be92 (Added identifiers)
        return -value, False
    if ast["tag"] == "&&":
        left_value, _ = evaluate(ast["left"], environment)
        right_value, _ = evaluate(ast["right"], environment)
        return left_value and right_value, False
    if ast["tag"] == "||":
        left_value, _ = evaluate(ast["left"], environment)
        right_value, _ = evaluate(ast["right"], environment)
        return left_value or right_value, False
    if ast["tag"] == "!":
        value, _ = evaluate(ast["value"], environment)
        return not value, False
    if ast["tag"] == "<":
        left_value, _ = evaluate(ast["left"], environment)
        right_value, _ = evaluate(ast["right"], environment)
        return left_value < right_value, False
    if ast["tag"] == ">":
        left_value, _ = evaluate(ast["left"], environment)
        right_value, _ = evaluate(ast["right"], environment)
        return left_value > right_value, False
    if ast["tag"] == "<=":
        left_value, _ = evaluate(ast["left"], environment)
        right_value, _ = evaluate(ast["right"], environment)
        return left_value <= right_value, False
    if ast["tag"] == ">=":
        left_value, _ = evaluate(ast["left"], environment)
        right_value, _ = evaluate(ast["right"], environment)
        return left_value >= right_value, False
    if ast["tag"] == "==":
        left_value, _ = evaluate(ast["left"], environment)
        right_value, _ = evaluate(ast["right"], environment)
        return left_value == right_value, False
    if ast["tag"] == "!=":
        left_value, _ = evaluate(ast["left"], environment)
        right_value, _ = evaluate(ast["right"], environment)
        return left_value != right_value, False
    if ast["tag"] == "print":
        if ast["value"]:
            value, _ = evaluate(ast["value"], environment)
            print(value)
        else:
            print()
        return None, False
    assert False, "Unknown operator in AST"

<<<<<<< HEAD
def equals(code, environment, expected_result, expected_environment=None):
    result, _ = evaluate(parse(tokenize(code)), environment)
    assert (result == expected_result), f"""ERROR: When executing
    {[code]} 
    -- expected result -- 
    {[expected_result]}
    -- got --
=======

def equals(code, environment, expected_result, expected_environment=None):
    result, _ = evaluate(parse(tokenize(code)), environment)
    assert (
        result == expected_result
    ), f"""ERROR: When executing
    {[code]}
    -- expected --
    {[expected_result]}
    --got--
>>>>>>> 575be92 (Added identifiers)
    {[result]}."""
    if expected_environment != None:
        assert (
            environment == expected_environment
        ), f"""ERROR: When executing
<<<<<<< HEAD
        {[code]} 
        -- expected environment -- 
        {[expected_environment]}
        -- got --
        {[environment]}."""

def test_evaluate_single_value():
    print("test evaluate single value")
    equals("4",{},4,{})
    equals("3",{},3,{})
    equals("4.2",{}, 4.2,{})
    equals("X", {'X':1}, 1)
    equals("Y", {'X':1, 'Y':2}, 2)
    equals("X+Y", {'X':1, 'Y':2}, 3)

def test_evaluate_addition():
    print("test evaluate addition")
    equals("1+1",{},2,{})
    equals("1+2+3",{},6,{})
    equals("1.2+2.3+3.4",{},6.9,{})

def test_evaluate_subtraction():
    print("test evaluate subtraction")
    equals("1-1",{},0,{})
    equals("3-2-1",{},0,{})

def test_evaluate_multiplication():
    print("test evaluate multiplication")
    equals("1*1",{},1,{})
    equals("3*2*2",{},12,{})
    equals("3+2*2",{},7,{})
    equals("(3+2)*2",{},10,{})

def test_evaluate_division():
    print("test evaluate division")
    equals("4/2",{},2,{})
    equals("8/4/2",{},1,{})

def test_evaluate_negation():
    print("test evaluate negation")
    equals("-2",{},-2,{})
    equals("--3",{},3,{})


def test_print_statement():
    print("test print statement")
=======
        {[code]}
        -- expected --
        {[expected_environment]}
        --got--
        {[environment]}."""


def test_evaluate_single_value():
    print("Testing test_evaluate_single_value...")
    equals("4", {}, 4, {})
    equals("3", {}, 3, {})
    equals("4.2",{}, 4.2,{})
    equals("x",{}, 3.14159,{})
    equals("_",{}, 3.14159,{})
    equals("X",{}, 3.14159,{})

def test_evaluate_addition():
    print("Testing test_evaluate_addition...")
    equals("1+1", {}, 2, {})
    equals("1+2+3", {}, 6, {})
    equals("1.2+2.3+3.4", {}, 6.9, {})

def test_evaluate_subtraction():
    print("Testing test_evaluate_subtraction...")
    equals("1-1", {}, 0, {})
    equals("3-2-1", {}, 0, {})

def test_evaluate_multiplication():
    print("Testing test_evaluate_multiplication...")
    equals("1*1", {}, 1, {})
    equals("3*2*1", {}, 6, {})
    equals("3*2*2", {}, 12, {})
    equals("3+2*2", {}, 7, {})
    equals("(3+2)*2", {}, 10, {})

def test_evaluate_division():
    print("Testing test_evaluate_division...")
    equals("1/1", {}, 1, {})
    equals("4/2", {}, 2, {})
    equals("8/4/2", {}, 1, {})
    equals("3/2/1", {}, 1.5, {})

def test_negation():
    print("Testing test_negation...")
    equals("-2", {}, -2, {})
    equals("--3", {}, 3, {})

def test_print_statement():
    print("Testing test_print_statement...")
>>>>>>> 575be92 (Added identifiers)
    equals("print(77)", {}, None, {})
    equals("print()", {}, None, {})
    equals("print(50+7)", {}, None, {})
    equals("print(50+8)", {}, None, {})

<<<<<<< HEAD
def test_assignment():
    print("test assignment")
    equals("X=1",{}, None, {"X":1})

=======
>>>>>>> 575be92 (Added identifiers)

if __name__ == "__main__":
    test_evaluate_single_value()
    test_evaluate_addition()
    test_evaluate_subtraction()
    test_evaluate_multiplication()
    test_evaluate_division()
<<<<<<< HEAD
    test_evaluate_negation()
    test_print_statement()
    test_assignment()
    print("done.")
=======
    test_negation()
    test_print_statement()
    print("Done.")
>>>>>>> 575be92 (Added identifiers)
