"""
Linked List is a collection of Nodes. Everytime we are doing an operation on Linked Lists, we will be working with nodes. In order to create
a Node everytime we need one, we will create a Node Class with two fields (data and next). Data is the value to be stored in the node and next
contains the reference to the next node if any. 
"""

class Node:
    def __init__(self, data):
        self.data = data 
        self.next = None 


"""
Next, we will create a LinkedList Class with one field head and initiaze it to None as there are no nodes in the linkedlist in the beginning. 
"""
class LinkedList:
    def __init__(self):
        self.head = None 


"""
Push method is to add a new_node at the end of the linked list. There can be two cases. One, when there are no nodes in the linked list and two,
there already exist some nodes. If the list is empty that means, head is pointing to nothing. All we have to do in this case is to create a new
node and make the Linked List's head to point to our new node. 
If the list is not empty, we will traverse the list until we are at the end of the list. Once we reach the end, we will make the last node's
next field to point towards our new node. Make sure to make a temporary variable to traverse the list, we want our head field always
pointing to first node in the list. 
"""
def push(self, data):
    new_node = Node(data)

    if self.head is None: 
        self.head = new_node
        return 
    
    temp = self.head 
    while temp.next is not None:
        temp = temp.next 
    
    temp.next = new_node

LinkedList.push = push 

"""
To display the list state everytime we add or remove nodes from the list. Instead of adding a new method and call it everytime, we override
the string dunder method to call print on object itself. 
"""
def __str__(self):
    ret_str = "["
    temp = self.head 

    while temp is not None: 
        ret_str += str(temp.data) + ", " 
        temp = temp.next

    ret_str = ret_str.rstrip(", ")
    ret_str += "]"
    return ret_str

LinkedList.__str__ = __str__ 



# TESTS
ll = LinkedList()
ll.push(1)
ll.push(2)
ll.push(3)
ll.push(4)
ll.push(5)
print(ll)