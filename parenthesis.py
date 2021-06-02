# parentheses balance
def Parentheses(string):
    a =["(","[","{"]
    b =[")","]","}"]
    stack =[]
    for i in string:
        if i in a:
            stack.append(i)
        elif i in b:
            ind = b.index(i)
            if len(stack) > 0 and a[ind] == stack[len(stack)-1]:
                stack.pop()
        else:
            return "Unbalance"
    if len(stack) == 0:
        return "Balance"
    else:
        return "Unbalance"                    

inp = input("Enter input:")
print(Parentheses(inp))