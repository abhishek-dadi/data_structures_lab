class Node:
    def __init__(self,data):
        self.data=data
        self.next=None
class linkedlist:
    def __init__(self):
        self.head=None
    def insertend(self,data):
        new_node=Node(data)
        if not self.head:
            self.head=new_node
            return
        curr=self.head
        while curr.next:
            curr=curr.next
        curr.next=new_node
    def display(self):
        curr=self.head
        element=[]
        while curr:
            element.append(str(curr.data))
            curr=curr.next
        print("head -->"," -> ".join(element) if element else "Empty linked List","-->None")
def slove1():

    original=linkedlist()
    line1=linkedlist()
    line2=linkedlist()
    numbers = list(map(int, input("Enter numbers separated by spaces: ").split()))
    for i in numbers:
        original.insertend(i)
    curr=original.head
    while curr.next:
        line1.insertend(curr.data)
        curr=curr.next
        if curr.next:
            line2.insertend(curr.data)
            curr=curr.next
    print("queue 1:")
    line1.display()
    print("queue 2:")
    line2.display()

def slove2():
    original=linkedlist()
    line1=linkedlist()
    line2=linkedlist()
    numbers = list(map(int, input("Enter numbers separated by spaces: ").split()))
    for i in numbers:
        original.insertend(i)
    curr=original.head
    for _ in range(len(numbers)//2):
        line1.insertend(curr.data)
        curr=curr.next
    while curr:
        line2.insertend(curr.data)
        curr=curr.next
    line1.display()
    line2.display()
    

def main():
    ch=int(input("1. slove in method 1 \n 2. solve in method 2"))
    if ch==1:
        slove1()
    else:
        slove2()
if __name__ == "__main__":
    main()

    

