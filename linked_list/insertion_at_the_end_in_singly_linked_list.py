class Node:
    def __init__(self, dataval=None):
        self.dataval = dataval
        self.nextval = None

class SLinkedList:
    def __init__(self):
        self.headval = None

# Function to add newnode
    def at_end(self, newdata):
        new_node = Node(newdata)
        if self.headval is None:
            self.headval = new_node
            return
        laste = self.headval
        while(laste.nextval):
            laste = laste.nextval
        laste.nextval=new_node
# Print the linked list
    def listprint(self):
        printval = self.headval
        while printval is not None:
            print (printval.dataval)
            printval = printval.nextval


list = SLinkedList()
list.headval = Node("Mon")
e2 = Node("Tue")
e3 = Node("Wed")
list.headval.nextval = e2
e2.nextval = e3
list.at_end("Thu")
list.listprint()