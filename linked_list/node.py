class Node:
    def __init__(self, data_value=None):
        self._data_value = data_value
        self._next_value = None


class LinkedList:
    def __init__(self):
        self.head_value = None

    def printing(self):
        print_value = self.head_value
        while print_value is not None:
            if print_value._data_value ==  "hello_world":
                print(print_value._data_value)
                print_value = print_value._next_value
            print_value = print_value._next_value




x = LinkedList()
x.head_value = Node("hello_world!")
data = Node("go truck!")
data2 = Node("go go truckpad!")
data3 = Node("go go go truck!")
x.head_value._next_value = data2
data2._next_value = data3

x.printing()