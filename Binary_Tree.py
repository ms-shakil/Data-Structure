class Node:
    def __init__(self,data):
        self.data = data
        self.left = None
        self.right = None
    # def __repr__(self):
    #     return repr(self.data)    
    def add_left(self,value):
        self.left = value
    def add_right(self,value):
        self.right = value
    
def tree():
    two =Node(2)
    two.add_left(Node(7))
    two.add_right(Node(9))
    return two
    
if __name__ == "__main__":
    root = tree()
    print(root)    
                

             