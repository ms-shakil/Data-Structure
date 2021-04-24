# Stack data structure in python with ourt class
data = ["shakil", "payer", "mainuddin", "fahad"]
define = 10
top = 3


def Push(data, top):
    if top < define:
        value = input("Enter the value:")
        data.append(value)
        top = top+1
    else:
        print("no capasiti in list")
    return data


def Pop(data, top):
    if top >= 0:
        return data[top]
        data.remove(data[top])
        top -= 1
    else:
        print("don't data have in this list")


try:

    inp = input("what do you want:\n add: \n remove:")
    if inp == "add":
        print(Push(data, top))
    elif inp == "remove":
        print(Pop(data, top))
    else:
        print("please enter add or remove.")
except Exception as e:
    print(e)

# stack class python


class Stack:
    def __init__(self):
        self.item = []

    def Push(self, item):
        self.item.append(item)

    def pop(self):
        return self.item.pop()

    def is_empty(self):
        if self.item == []:
            return True
        return False


if __name__ == "__main__":
    s = Stack()
    s.Push(3)
    s.Push(3)
    s.Push(5)

    while not s.is_empty():
        data = s.pop()
        print(data)
