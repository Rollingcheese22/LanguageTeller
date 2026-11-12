


error_occurred = "Process ended with return_code 0." if not True else "Process failed with return_code 1."
collection_pool = {}
ness_operation = []
line = 0

print("smthing")
class UnclosedParentheses(Exception):
    pass


with open("counting.txt") as syntax:
    while code := syntax.readline():
        line += 1

        tok = code.replace("=", " ASSIGMENT_SYM ")
        tok = tok.replace("let", " DECLARE_KWB ")
        collection_pool[str(line)] = tok.split()
        print(collection_pool)

class Tokenize:
    def __init__(self, collected):
        self.pool = collected
        self.var = None
        open_par = None
        closing_par = None
        count = 0
        hm = {}
        for num, current_line in self.pool.items():
            for i in range(len(current_line)):
                if current_line[i] == "DECLARE_KWB":
                    self.var = current_line[i + 1]
                    if current_line[i + 2] == "ASSIGMENT_SYM":
                        if current_line[i + 3][0:4] == "int(" or "str(":
                            for _ in current_line[i + 3][:]:
                                if _ == "(":
                                    open_par = current_line[i + 3][:].index(_) + 1
                                if _ == ")":
                                    closing_par = current_line[i + 3].index(_)
                            if open_par and closing_par:
                                if current_line[i + 3][0:4] == "int(":
                                    hm[self.var] = int(current_line[i + 3][open_par:closing_par])
                                else:
                                    hm[self.var] = str(current_line[i + 3][open_par:closing_par])


        print(hm)




Tokenize(collection_pool)




