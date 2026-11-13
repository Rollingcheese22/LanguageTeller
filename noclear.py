from enum import Enum
import re


#Collection Variables
collection_pool = {}
temp_collect = {}
operation = ""

#Validators
close_par = None
open_par = None
depth = 0

#Error Variables
exit_code = 0
err_pos = 0

#Misc.
fail = False
current_line = 0
ref = None





class KWords(Enum):
    let = "D_KWB"
    fasten = "FAST_B"

class Symbol(Enum):

    WALRUS_OP = ":="
    ASSIGN_SYM = "="

    COMPARE_SYM = "=="
class Identity:
    pass




def error_handler(err_line, err, err_position):
    global exit_code
    exit_code = 1
    print("\033[31m")

    if err == "par_err":
        print(temp_collect[err_line][0:len(temp_collect[err_line]) - 3])
        print("~" * err_position, "^" * (len(temp_collect[err_line]) - 3 - err_position), sep='')
        print("=" * 29, "≠", "ERROR", "≠", "=" * 29)
        print("\nUnclosedParentheses: Unclosed Parenthesis at position:", err_position, "Line", err_line)
    elif err == "InvalidSyntax":
        print("=" * 29, "≠", "ERROR", "≠", "=" * 29)
        print("InvalidSyntax: Nuclear cannot comprehend your program.")






with open("counting.txt", "r") as nuclear:
    while line := nuclear.readline():
        current_line += 1
        temp_collect[current_line] = line + "EOL"
        for char in line:
            if char == "(":
                err_pos = line.index(char)
                close_par = err_pos
                depth += 1
            if char == ")":
                err_pos = line.index(char)
                close_par = err_pos
                depth -= 1
        if depth != 0:
            error_handler(current_line, "par_err", err_pos)
            break



while True:
    if exit_code != 0:
        break

    for line_c, code in temp_collect.items():
        for i in range(len(code.split())):
            for key in KWords:
                temp_collect[line_c] = re.sub(rf"\b{key.name}\b", key.value, temp_collect[line_c])

    for line_c, code in temp_collect.items():
        for sym in Symbol:
            temp_collect[line_c] = temp_collect[line_c].replace(sym.value, sym.name)


    for line_c, code in temp_collect.items():
        for char in code:
            if char.isspace():
                continue
            else:
                operation += char
            if operation == "D_KWB":
                operation = ""

            if operation.endswith("ASSIGN_SYM"):
                if var := operation[0:len(operation) - len("ASSIGN_SYM")]:
                    ref = var
                    var = Identity()
                    var.Id = {"value": int, "type_lock": False, "value_lock": False, "current_type": None}
                    collection_pool[ref] = var.Id
                    operation = ""

            if ref:
                if operation.startswith("str("):
                    result = code[code.index("(") + 1:code.index(")")]
                    collection_pool[ref]["current_type"] = str
                    collection_pool[ref]["value"] = result

                elif operation.startswith("int("):
                    result = code[code.index("(") + 1:code.index(")")]
                    collection_pool[ref]["current_type"] = int
                    collection_pool[ref]["value"] = int(result)
                else:
                    if operation.startswith("str") or operation.startswith("int"):
                        fail = False
                    else:
                        fail = True
    if fail:
        error_handler(0, "InvalidSyntax", 0)


        operation = ""

    print(collection_pool)
    break
if exit_code:
    print("\033[4m")
    print("Process FAILED with exit code:", exit_code)
else:
    print("\033[32m")
    print("\033[4m")
    print("Process PASSED with exit code:", exit_code, end="")









