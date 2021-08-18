class TreeNode:
    def __init__(self,data):
        self.data = data
        self.parent = None
        self.left = None
        self.right = None
    
    def __repr__(self):
        return repr(self.data)

    def Add_left(self,node):
        self.left = node
        if node is not None:
            node.parent = self
    def Add_right (self,node):
        self.right = node
        if node is not None:
            node.parent = self


def bst_insert(root,node):
    last_node = None
    currnet_node = root
    while currnet_node is not None:
        last_node = currnet_node
        if node.data  < currnet_node.data:
            currnet_node = currnet_node.left
        else:
            currnet_node = currnet_node.right

    if last_node is None:
        root = node
    elif  node.data < last_node.data:
        last_node.Add_left(node)
    else:
        last_node.Add_right(node)        
    
    return root


def creat_bst ():
    root = TreeNode(10)
    for item in [5,17,3,7,12,19,1,4]:
        node = TreeNode(item)
        root = bst_insert(root,node)
    return root

def Search_item(node,key):
    while node is not None:
        if node.data == key:
            return node
        if key < node.data:
            node = node.left
        else:
            node = node.right        
    return node         

if __name__ == "__main__":
    root = creat_bst()
    print(root)        
    print(Search_item(root,20))