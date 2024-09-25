# tokenizer

""" 
break character stream into tokens, provide a token stream 
"""

import re

patterns = [
    ["\\(", "("],
    ["\\)", ")"],
    ["\\+", "+"],
    ["\\-", "-"],
    ["\\*", "*"],
    ["\\/", "/"],
    ["==", "=="],
    ["!=", "!="],
    ["<=", "<="],
    [">=", ">="],
    ["<", "<"],
    [">", ">"],
    ["=", "="],
<<<<<<< HEAD
    ["print", "print"],
    ["while", "while"],
    ["do", "do"],
    ["if", "if"],
    ["else", "else"],
    ["function", "function"],
    ["return", "return"],
    ["(\\d+\\.\\d*)|(\\d*\\.\\d+)|(\\d+)", "number"],
    ["[A-Za-z_][A-Za-z0-9_]*","identifier"],
=======
    ["print","print"],
    ["while","while"],
    ["do","do"],
    ["if","if"],
    ["else","else"],
    ["function","function"],
    ["return","return"],
    ["(\\d+\\.\\d*)|(\\d*\\.\\d+)|(\\d+)", "number"],
    ["[A-Za-z_][A-Za-z0-9_]*", "identifier"],
>>>>>>> 575be92 (Added identifiers)
    ["\\&\\&", "&&"],
    ["\\|\\|", "||"],
    ["!", "!"],
]

for pattern in patterns:
    pattern[0] = re.compile(pattern[0])


def tokenize(characters):
    tokens = []
    position = 0
    while position < len(characters):
        for pattern, tag in patterns:
            match = pattern.match(characters, position)
            if match:
                break
<<<<<<< HEAD
        assert match, f"Did not find a match for {characters[position:]}"
=======
        assert match
>>>>>>> 575be92 (Added identifiers)
        token = {
            "tag": tag,
            "value": match.group(0),
            "position": position,
        }
        tokens.append(token)
        position = match.end()
    for token in tokens:
        if token["tag"] == "number":
            if "." in token["value"]:
                token["value"] = float(token["value"])
            else:
                token["value"] = int(token["value"])
    token = {
<<<<<<< HEAD
            "tag": None,
            "value": None,
            "position": position,
        }
=======
        "tag": None,
        "value": None,
        "position": position,
    }
>>>>>>> 575be92 (Added identifiers)
    tokens.append(token)
    return tokens


def test_simple_tokens():
    print("testing simple tokens")
<<<<<<< HEAD
    assert tokenize("+") == [{'tag': '+', 'value': '+', 'position': 0}, {'tag': None, 'value': None, 'position': 1}]
    assert tokenize("-") == [{"tag": "-", "value": "-", "position": 0}, {'tag': None, 'value': None, 'position': 1} ]
=======
    assert tokenize("+") == [
        {"tag": "+", "value": "+", "position": 0},
        {"tag": None, "value": None, "position": 1},
    ]
    assert tokenize("-") == [
        {"tag": "-", "value": "-", "position": 0},
        {"tag": None, "value": None, "position": 1},
    ]
>>>>>>> 575be92 (Added identifiers)
    i = 0
    for char in "+-*/()":
        tokens = tokenize(char)
        assert tokens[0]["tag"] == char
        assert tokens[0]["value"] == char
        assert tokens[0]["position"] == i
<<<<<<< HEAD
    for characters in ["(",")","+", "-", "*", "/", "==","!=","<",">","<=", ">=","=","||","&&","!","print"]:
        tokens = tokenize(characters)
        assert (
            tokens[0]["tag"] == characters
        ), f"Expecting {characters}, got {tokens[0]["tag"]}"
=======
    for characters in ["(", ")", "+", "-", "*", "/", "==", "!=", "<", ">", "<=", ">=", "=" , "||", "&&", "!", "print"]:
        tokens = tokenize(characters)
        assert tokens[0]["tag"] == characters, f"EXPECTING: {characters}, got {tokens[0]["tag"]}"
>>>>>>> 575be92 (Added identifiers)
        assert tokens[0]["value"] == characters
    for number in ["123.45", "1.", ".1", "123"]:
        tokens = tokenize(number)
        assert tokens[0]["tag"] == "number"
        assert tokens[0]["value"] == float(number)

<<<<<<< HEAD
def test_identifier_tokens():
    print("testing identifer tokens")
=======
def test_identifiers_tokens():
    print("Testing identifiers_tokens...")
>>>>>>> 575be92 (Added identifiers)
    for s in ["x", "_", "X"]:
        tokens = tokenize(s)
        assert tokens[0]["tag"] == "identifier"
        assert tokens[0]["value"] == s
<<<<<<< HEAD
=======
        # print([tokens])

>>>>>>> 575be92 (Added identifiers)


if __name__ == "__main__":
    test_simple_tokens()
<<<<<<< HEAD
    test_identifier_tokens()
=======
    # tokens = tokenize("123.45*+1234*/123*()***34235****")
    # print(tokens)
    test_identifiers_tokens()
>>>>>>> 575be92 (Added identifiers)
    print("done.")
