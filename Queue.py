### about queue data structure 
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
        
Q = Queue()
Q.Enqueue("Shakil")
Q.Enqueue("Sajjad")

print(Q.arr)
# while not Q.is_empty():
#     p = Q.Dequeue()
#     print(p)