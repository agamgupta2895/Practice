class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class LinkedList:
    def __init__(self):
        self.head = None

    def append(self, data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
            return
        temp = self.head
        while temp.next:
            temp = temp.next

        temp.next = new_node

    def printList(self):
        temp = self.head
        print("LinkedList - \n")
        while temp:
            print(temp.data)
            temp = temp.next


if __name__ == '__main__':
    linkedList = LinkedList()
    linkedList.append(5)
    linkedList.append(6)
    linkedList.append(7)
    linkedList.append(58)
    linkedList.append(9)
    linkedList.printList()
