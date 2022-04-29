def eval_loop(condition):
    ans = eval(condition)
    while(ans != "done"):
        return ans


condition = ""
string = "done"
while string not in condition:
    condition = (input("ENter the string"))
    eval_loop(condition)
