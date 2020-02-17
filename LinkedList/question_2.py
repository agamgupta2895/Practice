# Find the nth node from the end in a linked list


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

    def findNthNode(self, n):

        temp = self.head
        length = 0
        while temp:
            length = length + 1
            temp = temp.next
        traverse_count = length - n
        temp = self.head
        while traverse_count:
            temp = temp.next
            traverse_count = traverse_count - 1
        print("Nth node from end : ", temp.data)


if __name__ == '__main__':
    linkedList = LinkedList()
    linkedList.append(5)
    linkedList.append(6)
    linkedList.append(7)
    linkedList.append(58)
    linkedList.append(9)
    linkedList.findNthNode(5)
