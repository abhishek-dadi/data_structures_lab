class Stack:
    def __init__(self):
        self.stack=[]
    def push(self,data):
        self.stack.append(data)
    def pop(self):
        if self.is_empty():
            raise IndexError("pop from an empty stack")
        return self.stack.pop()
    def is_empty(self):
        if len(self.stack)==0:
            return True
        else:
            return False
    def __len__(self):
        return len(self.stack)
    def peek(self):
        if self.is_empty():
            raise IndexError("peek from an empty stack")
        return self.stack[-1]
if __name__ == "__main__":
    s = Stack()
    print(f"Is empty initially? {s.is_empty()}")
    print("\n--- Pushing Elements ---")
    s.push(10)
    s.push(20)
    s.push(30)
    print(f"Stack size: {len(s)}")         
    print(f"Top element (peek): {s.peek()}") 

  
    print("\n--- Popping Elements ---")
    print(f"Popped: {s.pop()}")             
    print(f"New top element: {s.peek()}")   
    print(f"Remaining size: {len(s)}")     

    print("\n--- Emptying Stack & Exception Handling ---")
    s.pop() 
    s.pop() 

    print(f"Is empty now? {s.is_empty()}")  

    try:
        s.pop() 
    except IndexError as e:
        print(f"Caught expected error: {e}")


    

