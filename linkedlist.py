class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class linkedlist:
    def __init__(self):
        self.head = None

    def insertend(self, data):
        new_node = Node(data)
        if not self.head:
            self.head = new_node
            return
        curr = self.head
        while curr.next:
            curr = curr.next
        curr.next = new_node

    def insert_start(self, data):
        new_node = Node(data)
        new_node.next = self.head
        self.head = new_node
        self.display()

    def insert_at(self, ind, data):
        # FIX 1: Handle insertion at index 0 (start)
        if ind == 0:
            self.insert_start(data)
            return

        if not self.head:
            raise IndexError("Index out of bounds for empty list")

        new_node = Node(data)
        curr = self.head
        for _ in range(ind - 1):
            if not curr.next and _ < ind - 2:
                raise IndexError("Index out of bounds")
            curr = curr.next

        new_node.next = curr.next
        curr.next = new_node
        self.display()

    def delete_at(self, ind):
        if not self.head:
            raise IndexError("Cannot delete from an empty list")

        # Handle index 0 deletion
        if ind == 0:
            self.head = self.head.next
            return

        curr = self.head
        for _ in range(ind - 1):
            if not curr.next or not curr.next.next:
                raise IndexError("Index out of bounds")
            curr = curr.next

        curr.next = curr.next.next
        self.display()

    def delete_start(self):
        self.delete_at(0)

    def delete_end(self):
        l = self.length()
        if l == 0:
            raise IndexError("Cannot delete from an empty list")
        # FIX 2: Deleting end means index = length - 1
        self.delete_at(l - 1)
    

    def delmiddle(self):
        l = self.length()
        if l == 0:
            raise IndexError("Cannot delete from an empty list")
        self.delete_at(l // 2)
        self.display()

    def length(self):
        c = 0
        curr = self.head
        while curr:
            c += 1
            curr = curr.next
        return c
        

    def display(self):
        curr = self.head
        element = []
        while curr:
            element.append(str(curr.data))
            curr = curr.next
        print("head -->", " -> ".join(element) if element else "Empty linked List", "--> None")



def main():
    li = linkedlist()
    while(1):
        print("select operation:")
        print("1.insert_at_start \n 2.instert_at_end \n 3.insert_at_index \n 4.delete_at_end \n 5.delete_at_start \n 6.delete_at_index \n 7.display \n 8.length \n 9.enter multiple element at once \n 10.exit")

        ch=int(input(" enter your choice   :"))

        match ch:
            case 1:
                d=int(input("enter element  :"))
                li.insert_start(d)
            case 2:
                d=int(input("enter element  :"))
                li.insertend(d)
            case 3:
                d=int(input("enter element  :"))
                i=int(input("enter index    :"))
                li.insert_at(d,i)
            case 4:
                li.delete_end()
            case 5:
                li.delete_start()
            case 6:
                i=int(input("enter index    :"))
                li.delete_at(i)
            case 7:
                li.display()
            case 8:
                print("length == ",li.length())
            case 9:
                lis=list(map(int, input("Enter numbers separated by space: ").split()))
                for i in lis:
                    li.insertend(i)
            case 10:
                exit(0)
        li.display()





if __name__ == "__main__":
    main()

        
