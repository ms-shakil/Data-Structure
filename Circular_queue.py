class Circular_Queue:
    def __init__(self,sizes):
        self.items =[0]*sizes
        self.maxsize =sizes
        self.size,self.head,self.tail =0,0,0

    def enqueue(self,item):
        if self.is_full(): 
            print("queue is full") 
            return

        self.items[self.tail]=item
        self.tail = (self.tail +1) % self.maxsize
        self.size +=1

    def dequeue(self):
        data = self.items[self.head] 
        self.head = (self.head + 1) % self.maxsize
        self.size -=1
        return data         

    def is_empty(self):
        if self.size ==0:
            return True
        return False    

    def is_full(self):
        if self.size ==self.maxsize:
            return True
        return False                



Q = Circular_Queue(4)
Q.enqueue("shakil")
Q.enqueue("mainuddin")
Q.enqueue("fahad")
Q.enqueue("payer")
print(Q.dequeue())
  
print(Q.items)
print(Q.head)
print(Q.tail)
