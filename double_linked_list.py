class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
        self.prev = None 

    def __repr__(self):
        return f"Node({self.data})"


class linked_list: 
    def __init__(self):
        self.head = None

    def __len__(self):
        curr = self.head
        le = 0
        while curr:
            le += 1
            curr = curr.next
        return le

    def insert_at_index(self, data, index):
        if index < 0 or index > len(self):
            raise ValueError("Index out of range")

        new_node = Node(data)
        if index == 0:
            new_node.next = self.head
            if self.head:
                self.head.prev = new_node
            self.head = new_node
            return

        curr = self.head
        for _ in range(index - 1):
            curr = curr.next

        new_node.next = curr.next
        new_node.prev = curr

        if curr.next:  
            curr.next.prev = new_node
        curr.next = new_node

    def append(self, data):
        self.insert_at_index(data, len(self))

    def __repr__(self):
        nodes = []
        curr = self.head
        while curr:
            nodes.append(str(curr.data))
            curr = curr.next

        if not nodes:
            return "LinkedList[]"


        return "None <-> " + " <-> ".join(nodes) + " <-> None"

    def del_at(self, index):
        if index < 0 or index >= len(self):
            raise ValueError("index out of range")

    
        if index == 0:
            self.head = self.head.next
            if self.head:
                self.head.prev = None
            return

        
        curr = self.head
        for _ in range(index):  
            curr = curr.next

        curr.prev.next = curr.next
        if curr.next:  
            curr.next.prev = curr.prev

    def del_end(self):
        self.del_at(len(self) - 1)


def main():
    print("--- 1. Initializing Doubly Linked List ---")
    ll = linked_list()
    print("Initial List:", ll)  
    print("Initial Length:", len(ll)) 
    print()

    print("--- 2. Appending Elements ---")
    ll.append(10)
    ll.append(20)
    ll.append(30)
    print("List after appends:", ll)
    print("Length:", len(ll))
    print()

    print("--- 3. Inserting at Specific Indices ---")
    ll.insert_at_index(5, 0)
    print("After inserting 5 at index 0:", ll)

    ll.insert_at_index(15, 2)
    print("After inserting 15 at index 2:", ll)

    ll.insert_at_index(40, len(ll))
    print("After inserting 40 at end:", ll)
    print("Current Length:", len(ll))
    print()

    print("--- 4. Deleting Elements ---")
    ll.del_at(0)
    print("After deleting at index 0:", ll)

    ll.del_at(2)
    print("After deleting at index 2:", ll)

    ll.del_end()
    print("After calling del_end():", ll)
    print("Final Length:", len(ll))
    print()


if __name__ == "__main__":
    main()