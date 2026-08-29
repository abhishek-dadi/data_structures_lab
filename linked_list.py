class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

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
            self.head = new_node
            return

        curr = self.head
        for _ in range(index - 1):
            curr = curr.next

        new_node.next = curr.next
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
            
        return " -> ".join(nodes) + " -> None"
    def del_at(self,index):
        if index < 0 or index >=len(self):
            raise ValueError("index out of range")
        if index==0:
            self.head=self.head.next
            return
        curr=self.head
        for _ in range(index-1):
            curr=curr.next
        curr.next=curr.next.next
    def del_end(self):
        self.del_at(len(self)-1)
def main():
    print("--- 1. Initializing Linked List ---")
    ll = linked_list()
    print("Initial List:", ll)  # Uses __repr__
    print("Initial Length:", len(ll))  # Uses __len__
    print()

    print("--- 2. Appending Elements ---")
    ll.append(10)
    ll.append(20)
    ll.append(30)
    print("List after appends:", ll)
    print("Length:", len(ll))
    print()

    print("--- 3. Inserting at Specific Indices ---")
    # Insert 5 at index 0 (Beginning)
    ll.insert_at_index(5, 0)
    print("After inserting 5 at index 0:", ll)

    # Insert 15 at index 2 (Middle)
    ll.insert_at_index(15, 2)
    print("After inserting 15 at index 2:", ll)

    # Insert 40 at index 5 (End via insert_at_index)
    ll.insert_at_index(40, len(ll))
    print("After inserting 40 at end:", ll)
    print("Current Length:", len(ll))
    print()

    print("--- 4. Deleting Elements ---")
    # Delete at index 0 (Head deletion)
    ll.del_at(0)
    print("After deleting at index 0:", ll)

    # Delete at index 2 (Middle deletion)
    ll.del_at(2)
    print("After deleting at index 2:", ll)

    # Delete end element using del_end()
    ll.del_end()
    print("After calling del_end():", ll)
    print("Final Length:", len(ll))
    print()

    print("--- 5. Handling Error Case ---")
    try:
        ll.del_at(100)  # Invalid index
    except ValueError as e:
        print("Caught expected error:", e)


if __name__ == "__main__":
    main()
    