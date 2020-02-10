class Node:
    def __init__(self, dataval=None):
        self.dataval = dataval
        self.nextval = None

class SLinkedList:
    def __init__(self):
        self.headval = None

# Function to add node
    def in_between(self,middle_node,newdata):
        if middle_node is None:
            print("The mentioned node is absent")
            return

        new_node = Node(newdata)
        new_node.nextval = middle_node.nextval
        middle_node.nextval = new_node

# Print the linked list
    def listprint(self):
        printval = self.headval
        while printval is not None:
            print (printval.dataval)
            printval = printval.nextval


list = SLinkedList()
list.headval = Node("Mon")
e2 = Node("Tue")
e3 = Node("Thu")
list.headval.nextval = e2
e2.nextval = e3
list.in_between(list.headval.nextval,"Fri")
list.listprint()