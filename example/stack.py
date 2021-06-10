class Node:
    def __init__(self,value=None):
        self.data = value
        self.next = None
        self.previous = None
        
class Doubly_LinkedList:
    def __init__(self):
        self.head = None
        self.tail = None
        self.size = 0        
    
    def  Add(self,value):
        new_node = Node(value)
        if self.head is None:
            self.head = new_node
            self.tail = new_node
            self.size +=1
        else:
            self.tail.next =new_node
            new_node.previous = self.tail
            self.tail = new_node
            self.size +=1  
              
    def Prepend(self,value):
        new_node = Node(value)
        new_node.next = self.head
        self.head.previous = new_node
        self.head = new_node
        self.size  +=1                 
    def Add_after_item(self,old,new):
        new_node = Node(new)
        hd = self.head
        while hd is not None:
            if hd.data == old:
                new_node.next = hd.next
                hd.next.previous = new_node
                hd.next = new_node
                new_node.previous = hd
                self.size +=1
            hd =hd.next     
            
    def Delete_Node(self,value):
        hd = self.head
        while hd is not None:
            if hd.data == value:
                if  hd.previous is None:
                    self.head = hd.next
                    self.head.previous = None
       
                else:
                    hd.previous.next = hd.next
  
                    
                if hd.next is None:
                    self.tail = hd.previous
                 
                else:    
                    hd.next.previous = hd.previous
                self.size -= 1   
                
            hd = hd.next   
    def Delete_LastNode(self):
        if self.tail.previous is None:
            self.tail = None
            self.head = None
            self.size -=1
            return
        if self.tail is not None:
            self.tail = self.tail.previous
            self.tail.next = None
            self.size -=1   
            
    def Delete_FirstNode(self): 
        if self.head.next is None:
            self.head = None
            self.tail  = None
            self.size  -=1
            return
        if self.head is not None:
            self.head = self.head.next
            self.head.previous = None  
            self.size -=1             
    def __str__(self):
        hd = self.head
        ar = []
        while hd is not None:
            ar.append(hd.data)
            hd = hd.next    
        return f"{ar}"      
    

class Stack:
    def __init__(self):
        self.__list =Doubly_LinkedList()
        
    def Push(self,data):
        self.__list.Add(data)
    def Pop(self):
        self.__list.Delete_LastNode()
    def __len__(self):
        return self.__list.size    
    def __str__(self):
        hd = self.__list
        return  f"{hd}"
# mystack = Stack()
# mystack.Push("shakil")
# mystack.Push("sajjad") 
# mystack.Push("fahad")     
# mystack.Pop()  
# print(len(mystack))
# print(mystack)

class Queue:
    def __init__(self):
        self.__arr =Doubly_LinkedList()
        
    def Enqueue(self,value):
        self.__arr.Add(value)    
    
    def Dequeue(self):
        self.__arr.Delete_FirstNode()
            
    def __len__(self):
        return self.__arr.size        
    def __str__(self):
        hd = self.__arr
        return  f"{hd}"    
    

myQueue = Queue()
myQueue.Enqueue("shakil")
myQueue.Enqueue("main")    
myQueue.Enqueue("payer")
myQueue.Dequeue()
print(myQueue)