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
    Pre_order(root)
    print("space")
    Post_Order(root)
    print("No space")
    In_Order(root)
                
#### Another Binary Tree Programme !
class Queue:
    def __init__(self):
        self.arr =[]
        
    def Enqueue(self,data):
        self.arr.append(data)    
    
    def Dequeue(self):
        return self.arr.pop(0)
    def is_empty(self):
        if self.arr ==[]:
            return True
        return False      
        
class TreeNode:
    def __init__(self,data = None):
        self.data= data
        self.left = None
        self.right = None
                     
class BinaryTree:
    def __init__(self):
        self.root = None
    
    def insert(self,value):
        if self.root is None:
            self.root = TreeNode(value)
        else:
            nodes = Queue()
            nodes.Enqueue(self.root)
            while True:
                chacking_node = nodes.Dequeue()
                if chacking_node.left is None:
                    chacking_node.left = TreeNode(value)
                    return
                elif chacking_node.right is None:
                    chacking_node.right = TreeNode(value)
                    return
                else:
                    nodes.Enqueue(chacking_node.left)
                    nodes.Enqueue(chacking_node.right)    
                                               

my_tree = BinaryTree()
my_tree.insert("a")
my_tree.insert("b")
my_tree.insert("c")
my_tree.insert("d")                                               