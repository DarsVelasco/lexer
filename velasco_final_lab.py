from sympy.logic import simplify_logic
import time, os

def lexer(expression):
    tokens = []
    position = 0
    while position < len(expression):
        current_char = expression[position]
        if current_char == " ":
            position += 1
        elif current_char.isalnum():
            tokens.append(current_char)
            position += 1
            
            # Check if the next character is an operator or end of expression
            if position < len(expression) and (expression[position] in "+|&!~)" or expression[position] == " "):
                continue
            else:
                tokens.append("&") 
        elif current_char in "()+|*&!~":
            tokens.append(current_char)
            position += 1
    return tokens



def parser(tokens):
    exp_for_simplify = []
    for token in tokens:
        if token.isalnum():
            exp_for_simplify.append(token)

        elif token == "!":
            exp_for_simplify.append("~")

        elif token == "+":
            exp_for_simplify.append("|")

        elif token == "*":
            exp_for_simplify.append("&")

        elif token == "~":
            exp_for_simplify.append(token)

        elif token == "|":
            exp_for_simplify.append(token)

        elif token == "&":
            exp_for_simplify.append(token)

        elif token == "(":
            exp_for_simplify.append(token)

        elif token == ")":
            exp_for_simplify.append(token)

    exp_for_simplify = ''.join(exp_for_simplify)
    return simplify_logic(exp_for_simplify)

if __name__ == "__main__":
    while True:
        os.system('cls')
        print("Boolean Expression Parser\n")
        expression = input("Enter Boolean Expression (Enter to Exit): ")
        if expression == "":
            print("Exiting...")
            time.sleep(1)
            break
        tokens = lexer(expression)
        simplified_express = parser(tokens)
        print(f"Simplified Expression: {simplified_express}\n")
        input("Enter to next expression... ")