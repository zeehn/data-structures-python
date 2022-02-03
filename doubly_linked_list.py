"""
Node class to create new nodes. We have to three fields (data, prev, and next). In doubly linked lists, unlike singly linked list we can go both direction forward and backward.
"""
class Node:
    def __init__(self, data):
        self.data = data
        self.prev = None 
        self.next = None



class DoublyLinkedList:
    def __init__(self):
        self.head = None

"""String dunder method we have overridden to display the current content of the list when we call print on the list object
"""
def __str__(self):
    ret_str = '['
    temp = self.head 
    
    while temp is not None:
        ret_str += str(temp.data) + ', '
        temp = temp.next

    ret_str = ret_str.rstrip(', ')
    ret_str += ']'
    return ret_str

DoublyLinkedList.__str__ = __str__ 


"""
Push method adds a node at the end of the list. We can have two cases:
1) When the list is empty, that means self.head is None. In that case, we just make the self.head point to our new node.
2) When the list is not empty, in this case; we traverse the list until we reach the last node. From the last node, we make the next reference of last node point towards our new node and new node's prev reference towards last node. 
"""
def push(self, data):
    new_node = Node(data) 

    temp = self.head 
    if temp is None: 
        self.head = new_node 
        return 

    while temp.next is not None:
        temp = temp.next

    temp.next = new_node 
    new_node.prev = temp 

DoublyLinkedList.push = push 


# TEST CASES:

dll = DoublyLinkedList()


dll.push(1)

print(dll)

dll.push(2)

print(dll)
