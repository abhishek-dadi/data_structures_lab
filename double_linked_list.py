class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
        self.prev = None 

    def __repr__(self):
        return f"Node({self.data})"


class double_linked_list: 
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
            raise ValueError("Index out of range")

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
        if len(self) == 0:
            raise ValueError("Cannot delete from an empty list")
        self.del_at(len(self) - 1)


def main():
    li = double_linked_list()
    while True:
        print("\n--- Select Operation ---")
        print("1. Insert at start\n2. Insert at end\n3. Insert at index\n4. Delete at end\n5. Delete at start\n6. Delete at index\n7. Display\n8. Length\n9. Enter multiple elements\n10. Exit")

        ch = int(input("Enter your choice: "))

        match ch:
                case 1:
                    d = int(input("Enter element: "))
                    li.insert_at_index(d, 0)
                case 2:
                    d = int(input("Enter element: "))
                    li.append(d)
                case 3:
                    d = int(input("Enter element: "))
                    i = int(input("Enter index: "))
                    li.insert_at_index(d, i)
                case 4:
                    li.del_end()
                    print("Deleted element from end.")
                case 5:
                    li.del_at(0)
                    print("Deleted element from start.")
                case 6:
                    i = int(input("Enter index: "))
                    li.del_at(i)
                    print(f"Deleted element at index {i}.")
                case 7:
                    print("Current List:", li)
                case 8:
                    print("Length ==", len(li))
                case 9:
                    lis = list(map(int, input("Enter numbers separated by space: ").split()))
                    for item in lis:
                        li.append(item)
                    print(f"Added {len(lis)} elements.")
                case 10:
                    print("Exiting...")
                    break
                case _:
                    print("Invalid choice! Please select between 1 and 10.")
        print("Current List:", li)
            


if __name__ == "__main__":
    main()