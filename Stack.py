# Stack data structure in python
data =["shakil","payer","mainuddin","fahad"]
define = 10
top = 3
def Push(data,top):
    if top < define:
        value = input("Enter the value:")
        data.append(value)
        top = top+1
    else:
        print("no capasiti in list")
    return data
def Pop(data,top):
    if top >=0:
        return data[top]
        data.remove(data[top])
        top -= 1
    else:
        print("don't data have in this list")    
try:
        
    inp = input("what do you want:\n add: \n remove:")
    if inp == "add":
        print( Push(data,top))
    elif inp =="remove":
        print(Pop(data,top))
    else:
        print("please enter add or remove.")  
except Exception as e:
    print(e)          


