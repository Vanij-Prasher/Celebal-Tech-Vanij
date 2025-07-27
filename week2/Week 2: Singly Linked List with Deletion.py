# ✅ Week 2: Singly Linked List with Deletion

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None

    def add(self, data):
        new_node = Node(data)
        if not self.head:
            self.head = new_node
        else:
            temp = self.head
            while temp.next:
                temp = temp.next
            temp.next = new_node

    def delete_nth(self, n):
        if not self.head:
            raise Exception("List is empty")
        if n == 1:
            self.head = self.head.next
            return
        temp = self.head
        for _ in range(n - 2):
            if not temp.next:
                raise Exception("Index out of range")
            temp = temp.next
        if not temp.next:
            raise Exception("Index out of range")
        temp.next = temp.next.next

    def display(self):
        temp = self.head
        while temp:
            print(temp.data, end=" -> ")
            temp = temp.next
        print("None")

ll = LinkedList()
for val in [10, 20, 30, 40]:
    ll.add(val)
ll.display()
ll.delete_nth(3)
ll.display()
