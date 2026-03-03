class Node:
    # represent a node in a linked list
    def __init__(self, value=0, next=None):
        self.value = value
        self.next = next

class LinkedList:
    # represent a linked list worth of Nodes
    def __init__(self, head=None):
        self.head = head
    
    def sum_values(self):
        # write code:
        sum = 0

        print( f"head={ self.head }" )

        # starting point, exit condition, how you iterate to next one, how do you add to sum
        a = self.head
        while a != None:
            sum += a.value
            a = a.next

        return sum

# test ``: when l is LinkedList(), l.sum_values() should return 0
#l = LinkedList()
#print( f"test 1: { l.sum_values() }" )

# test 1: when l is LinkedList(Node(1, Node(2, Node(3))), l.sum_values() should return 6 (3+2+1)
l = LinkedList(Node(1, Node(2, Node(3))))
print( f"test 2: { l.sum_values() }" )
