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


"""
In Pop method we have three cases. First, when the list is empty, we raise an exception. Second, when there is only one element in the list, in that case, we just make the head pointer point to None. In the last case, when there are more than one node in the list, we traverse the list until we reach the last element while keeping track of both last and prev elements. Once we reach there, we make the prev's next reference point to current's next reference that is None is our case. 
"""
def pop(self):
    if self.head is None:
        raise Exception("List is empty. Nothing to pop!")

    temp = self.head 
    if temp.next is None: 
        val = temp.data
        self.head = None
        return val 

    while temp.next is not None:
        prev = temp 
        temp = temp.next

    val = temp.data 
    prev.next = temp.next 
    return val 

DoublyLinkedList.pop = pop


def insert(self, index, data):
    new_node = Node(data)
    
    if index == 0:
        new_node.next = self.head 

        if self.head is not None:
            self.head.prev = new_node

        self.head = new_node
        return 

    temp = self.head 
    count = 0
    while temp is not None and count < index:  
        prev = temp 
        temp = temp.next 
        count += 1

    new_node.next = temp
    if temp is not None:
        temp.prev = new_node 

    prev.next = new_node 
    new_node.prev = prev 

DoublyLinkedList.insert = insert 


# TEST CASES:

dll = DoublyLinkedList()


dll.push(1)
print(dll)
dll.push(2)
print(dll)
dll.push(3)
print(dll)

dll.pop()
print(dll)
dll.insert(0,10)
print(dll)
dll.insert(1,2)
print(dll)
dll.insert(0,0)
print(dll)
dll.insert(5,50)
print(dll)
