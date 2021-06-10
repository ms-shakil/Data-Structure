### Doubly linked list
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
        
##### Inserting Items at the End       
 
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
            
####### Inserting Items at the started    
        
    def Prepend(self,value):
        new_node = Node(value)        
        new_node.next =self.head
        self.head.prev = new_node
        self.head = new_node
        self.size +=1
        
####### Insertign item after the value

    def Add_After_newValue(self,old,new):
        new_node = Node(new)     
        hd = self.head
        while hd is not None:
            if hd.data == old:
                new_node.next = hd.next
                hd.next.prev = new_node
                hd.next = new_node
                new_node.prev = hd
                self.size +=1
            hd =hd.next
        
### Delete item       
 
    def Delete(self,value):    
        hd = self.head
        while hd is not None:
            if hd.data == value:
                if hd.prev is None:
                    self.head =hd.next
                    
                else:
                    hd.prev.next = hd.next
                  
                if hd.next is None:
                    self.tail = hd.prev
                    
                else:    
                    hd.next.prev = hd.prev
                self.size -=1   
            hd = hd.next  
     ### Delete last node
    def Delete_LastNode(self):
        if self.tail.prev is None:
            self.tail = None
            self.head = None
            self.size -=1
            return
        if self.tail is not None:
            self.tail = self.tail.prev
            self.tail.next = None
            self.size -=1   
    #### delete first node
            
    def Delete_FirstNode(self): 
        if self.head.next is None:
            self.head = None
            self.tail  = None
            self.size  -=1
        if self.head is not None:
            self.head = self.head.next
            self.head.prev = None  
            self.size -=1         
 ######## search items 
          
    def Search(self,value) :
        hd = self.head
        while hd is not None:
            if hd.data == value:
                print("This value is =",hd.data)
                return              
        return "This is wrong data"
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
print(D.size)
