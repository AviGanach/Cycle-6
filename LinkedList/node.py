class Node:
    def __init__ (self, data):
        self.data = data
        self.next = None

    def __str__ (self):
        return f"the data in this node is: {self.data} >>> {self.next}" 
    
n1 = Node (40)
n1.next = Node(41)
print (n1)