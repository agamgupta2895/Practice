# Find the nth node from the end in a linked list in one scan


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
        fast = self.head
        count = n
        while count != 1:
            fast = fast.next
            count = count -1

        while fast.next:
            fast = fast.next
            temp = temp.next

        print("Nth node from end : ", temp.data)


if __name__ == '__main__':
    linkedList = LinkedList()
    linkedList.append(5)
    linkedList.append(6)
    linkedList.append(7)
    linkedList.append(58)
    linkedList.append(9)
    linkedList.findNthNode(1)
