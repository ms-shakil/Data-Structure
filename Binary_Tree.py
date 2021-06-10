class Node:
    def __init__(self,data):
        self.data = data
        self.left = None
        self.right = None
    def __repr__(self):
        return repr(self.data)    
    def add_left(self,value):
        self.left = value
    def add_right(self,value):
        self.right = value
    
def tree():
    two =Node(2)
    nine =Node(9)
    seven = Node(7)
    two.add_left(seven)
    two.add_right(nine)
    one =Node(1)
    six =Node(6)
    seven.add_left(one)
    seven.add_right(six)
    five = Node(5)
    ten = Node(10)
    six.add_left(five)
    six.add_right(ten)
    eight =Node(8)
    three =Node(3)
    four = Node(4)
    nine.add_right(eight)
    eight.add_left(three)
    eight.add_right(four)
    return two
    
if __name__ == "__main__":
    root = tree()
    print(root)    
                

             