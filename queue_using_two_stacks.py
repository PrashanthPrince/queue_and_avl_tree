""" 
Author: Prashanth Prince
Date: 15 Dec 2020
Description: Implementation of a Queue using two stacks.

"""


class Queue: 
    def __init__(self): 
        self.stack1 = [] 
        self.stack2 = [] 
  
    # EnQueue item to the queue 
    def enQueue_operation(self, element): 
        self.stack1.append(element) 
  
    # DeQueue item from the queue 
    def deQueue_operation(self): 
  
        # if both the stacks are empty, then print "the Queue is empty"
        if len(self.stack1) == 0 and len(self.stack2) == 0: 
            print("The Queue is Empty") 
            return
  
        # if the stack2 is empty and stack1 has elements, then transfer all the elements from stack1 to stack2. And pop the element from stack2.
        elif len(self.stack2) == 0 and len(self.stack1) > 0: 
            while len(self.stack1): 
                #temp = self.stack1.pop() 
                self.stack2.append(self.stack1.pop()) 
            return self.stack2.pop() 
  
        else: 
            return self.stack2.pop() 
  
 
if __name__ == '__main__': 
    q = Queue() 

    q.enQueue_operation(1) 
    q.enQueue_operation(2) 
    q.enQueue_operation(3) 
  
    print(q.deQueue_operation())

    q.enQueue_operation(4) 
    q.enQueue_operation(5)
    
    print(q.deQueue_operation()) 
    print(q.deQueue_operation())
    
    q.enQueue_operation(6)
    
    print(q.deQueue_operation())
    print(q.deQueue_operation())
    print(q.deQueue_operation())

    print(q.deQueue_operation())