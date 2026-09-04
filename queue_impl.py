class Queue:
    def __init__(self):
        self.queue=[]
    def __len__(self):
        return len(self.queue)
    def enqueue(self,data):
        self.queue.append(data)
    def dequeue(self):
        if self.is_empty():
            raise IndexError("dequeue from an empty queue")
        return self.queue.pop(0)
    def is_empty(self):
        return self.__len__()==0
    def peek(self):
        if self.is_empty():
            raise IndexError("peek from an empty queue")
        return self.queue[0]
if __name__=='__main__':
    queue=Queue()
    print(f"is queue empty {queue.is_empty}")
    print("appending 10,20,30")
    queue.enqueue(10)
    queue.enqueue(20)
    queue.enqueue(30)
    print(f"length of queue is {queue.__len__()}")
    print("__ remove 2 items __")
    print(f"removed items are {queue.dequeue()} and {queue.dequeue()}")
    print(f"The next element in queue is {queue.peek()}")
    queue.dequeue()
    print("now  check queue is empty")
    print(f"queue is empty:  {queue.is_empty()}")
    print("==== trying remove a element from empty queue")
    try: 
        queue.dequeue()
    except IndexError as e:
        print(e)
    


