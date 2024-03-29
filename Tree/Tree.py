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
    
def Tree():
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


############ Tree Traverse

def Pre_order(node):
    print(node.data)
    if node.left is not None:
        Pre_order(node.left)
    if node.right is not None:
        Pre_order(node.right) 
def Post_Order(node):
    if node.left is not None:
        Post_Order(node.left)
    if node.right:
        Post_Order(node.right)     
    print(node.data)   
def In_Order(node):
    if node.left :
        In_Order(node.left)
    print(node)
    if node.right:
        In_Order(node.right)   


if __name__ == "__main__":

    root = Tree()
    print("pre order data traverse:") 
    Pre_order(root)   
    print("post order data traverse:")
    Post_Order(root)
    print("In-order data traverse:")
    In_Order(root)