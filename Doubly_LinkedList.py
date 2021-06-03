class Node:
    def __init__(self,data):
        self.data = data
        self.next = None
        self.prev = None
        
class DoublyLinkedList:
    def __init__(self) :
        self.head = None
        self.size = 0
        self.tail = None
    def Add(self,value):
        new_node =Node(value)
        if self.head is None:
            self.head = new_node
            self.tail = new_node
            self.size +=1
        else:
            self.tail.next = new_node
            new_node.prev = self.tail
            self.tail = new_node
            self.size +=1
    def Prepend(self,value):
        new_node = Node(value)        
        new_node.next =self.head
        self.head.prev = new_node
        self.head = new_node
        
    def Delete(self,value):    
        hd = self.head
        while hd is not None:
            if hd.data == value:
                if hd.prev is None:
                    self.head =hd.next
                    self.size -=1
                else:
                    hd.prev.next = hd.next
                    self.size -=1
                if hd.next is None:
                    self.tail = hd.prev
                    self.size-=1
                    
                else:    
                    hd.next.prev = hd.prev
                
           
                
                   
            hd = hd.next  
                
        
    def __str__(self):
        arr =[]
        hd = self.head
        while hd is not None:
            arr.append(hd.data)
            hd = hd.next
        return f"{arr}"    
                        
                
D = DoublyLinkedList()
D.Add("Shakil") 
D.Add("Main")
D.Add("payer") 
D.Add("Sajjad")     


print(D)


D.Delete("Shakil")
D.Delete("payer")

D.Delete("Sajjad")
print(D.size)
print(D)