# about singly linked list
class Node:
    def __init__(self,data =None,next = None):
        self.data = data
        self.next = next

class LinkedList:
    def __init__(self):
        self.head = None

    def insert(self,data):
        node = Node(data)
        if self.head is None:
            self.head = node

            return
        current_node = self.head
        while current_node.next is not None:
            current_node = current_node.next
        current_node.next = node 
    def Prepend(self,data):
        node = Node(data)
        node.next = self.head
        self.head = node            
    def search(self,item):
        hd = self.head
        while hd is not None:
            hd.data == item
            return item
            hd = hd.next
        return "don't get data" 

    def insert_after_item(self,new_data,old_data):
        hd = self.head 
        while hd is not None:
            if hd.data == old_data:
                break
            hd = hd.next

        if hd is None:
            print("item not in the list")
        else:
            new_node = Node(new_data)
            new_node.next = hd.next
            hd.next = new_node                

    def __str__(self):
        list_ =[]
        nd = self.head

        while nd is not None:
            list_.append(nd.data)
            nd = nd.next
        return f"{list_}"


L =LinkedList()

L.insert("Shakil")
L.insert("main")
L.insert("Payer")
L.Prepend("Sajjad")
L.Prepend("Fahad")
print(L.search("Payer"))
print(L)
L.insert_after_item("Asif", "Sajjad")
print(L)