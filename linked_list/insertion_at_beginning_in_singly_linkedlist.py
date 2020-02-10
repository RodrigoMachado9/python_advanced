
# todo, value at the top of the list ( linked list )
class Node:
    def __init__(self, dataval=None):
        self.dataval = dataval
        self.nextval = None

# todo ->  sun, mon, tue, wed

class SLinkedList:

    def __init__(self):
        self.headval = None

    # Print the linked list
    def list_print(self):
        printval = self.headval
        while printval is not None:
            print(printval.dataval)
            printval = printval.nextval

    def at_begining(self, newdata):
        new_node = Node(newdata)

        # It Update the new nodes next val to existing node
        new_node.nextval = self.headval
        self.headval = new_node


list = SLinkedList()
list.headval = Node("Mon")
e2 = Node("Tue")
e3 = Node("Wed")
list.headval.nextval = e2
e2.nextval = e3
list.at_begining("Sun")
list.list_print()