class Node:
    def __init__(self, data=None):
        self.data = data
        self.next = None
        print("the currente value upgrade: %s " % self.data)


class LinkedList:
    def __init__(self):
        self.head = None

    def printing(self):
        print_value = self.head
        while print_value is not None:
            print(print_value.data)
            print_value = print_value.next



x = LinkedList()
x.head = Node("rmachado")
data2 = Node("truck")
data3 = Node("driver")
data4 = Node("shipper")

# todo, :: multiple instances :: beautifull .
x.head.next = data2
data2.next = data3
data3.next = data4


x.printing()