# Check if a linkedlist has a cycle or not and find the start of the loop


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

    def implementCycle(self, data):
        temp = self.head
        cycle_node = self.head
        while temp.next:
            if temp.data == data:
                cycle_node = temp
            temp = temp.next
        temp.next = cycle_node

    def detectCycleAndStartOfTheLoop(self):
        slowPtr = self.head
        fastPtr = self.head
        slowPtr = slowPtr.next
        fastPtr = fastPtr.next.next
        while slowPtr != fastPtr:
            slowPtr = slowPtr.next
            fastPtr = fastPtr.next.next

        slowPtr = self.head

        while slowPtr != fastPtr:
            slowPtr = slowPtr.next
            fastPtr = fastPtr.next

        print("Start of the loop : ", slowPtr.data)
    def printList(self):
        temp = self.head
        print("LinkedList - \n")
        while temp:
            if temp.data == 7:
                print(temp.data)
            temp = temp.next


if __name__ == '__main__':
    linkedList = LinkedList()
    linkedList.append(5)
    linkedList.append(6)
    linkedList.append(7)
    linkedList.append(100)
    linkedList.append(101)
    linkedList.append(581)
    linkedList.append(582)
    linkedList.append(583)
    linkedList.append(584)
    linkedList.append(586)
    linkedList.append(10)
    linkedList.implementCycle(581)
    # linkedList.printList()
    linkedList.detectCycleAndStartOfTheLoop()
