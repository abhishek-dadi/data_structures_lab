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

    print("Inserting 10, 20, 30 at end:")
    li.insertend(10)
    li.insertend(20)
    li.insertend(30)
    li.display()  # Output: 10 -> 20 -> 30
    li.delmiddle()
    li.display()

    print("\nInsert 40 at start:")
    li.insert_start(40)
    li.display()  # Output: 40 -> 10 -> 20 -> 30

    print("\nInsert 50 at index 3:")
    li.insert_at(3, 50)
    li.display()  # Output: 40 -> 10 -> 20 -> 50 -> 30

    print("\nDelete at index 3:")
    li.delete_at(3)
    li.display()  # Output: 40 -> 10 -> 20 -> 30

    print("\nDelete end:")
    li.delete_end()
    li.display()  # Output: 40 -> 10 -> 20

    print("\nDelete start:")
    li.delete_start()
    li.display()  # Output: 10 -> 20


if __name__ == "__main__":
    main()

        
