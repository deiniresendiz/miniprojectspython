class Node(object):
    "Represents a single linked node."
    def __init__(self, data, next=None):
        self.data = data
        self.next = next

class TwoWayNode(object):
    def __init__(self, data, previous=None, next=None):
        Node.__init__(data, next=next)
        self.previous = previous


# Creating 3 differents nodes 
node1 = None
node2 = Node("A", None)
node3 = Node("B", node2)

# This causes an Atribute Error
# node1.next = node3

node1 = Node("C", node3)