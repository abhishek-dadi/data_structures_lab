import linkedlist
class Queue:
    def __init__(self):
        self.queue=linkedlist.linkedlist()
    def enqueue(self,data):
        self.queue.insertend(data)
        self.queue.display()
    def dequeue(self):
        if self.__len__()==0:
            raise IndexError("Queue is empty")
        data =self.queue.head.data
        self.queue.head = self.queue.head.next
        self.queue.display()
        return data
    def __len__(self):
        return self.queue.length()
    def display(self):
        self.queue.display()
    def peek(self):
        if self.__len__()==0:
            raise IndexError("Queue is empty")
        return self.queue.head
    def is_empty(self):
        return self.__len__()==0
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
