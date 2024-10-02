import sys

from pprint import pprint

from tokenizer import tokenize
from parser import parse
from evaluator import evaluate


def main():
    # check for arguments
    if len(sys.argv) > 1:
        # open the file
        with open(sys.argv[1], "r") as f:
            source_code = f.read()
        environment = {}
        tokens = tokenize(source_code)
        ast = parse(tokens)
        evaluate(ast, environment)
        exit()
    # REPL loop
    debug = False
    environment = {}
    while True:
        try:
            # read the input
            source_code = input(">> ")
            if source_code.strip() in ["exit", "quit"]:
                break
            if source_code.strip() in ["debug"]:
                debug = not (debug)
                if debug:
                    print("debugger is ON")
                    pprint(environment)
                else:
                    print("debugger is OFF")
                continue
            tokens = tokenize(source_code)
            ast = parse(tokens)
            evaluate(ast, environment)
        except Exception as e:
            print(f"ERROR: {e}")


if __name__ == "__main__":
    main()
