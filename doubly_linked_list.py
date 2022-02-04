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


"""
In doubly linked list, we perform an insert operation by first creating a new node. If the index is 0, there can be two cases:
    1) The list is empty and inserting a node at 0 makes it the first element in the list. In this case, we just make the head point towards our new node. New 
    node's next and prev element will remain None, so we don't have to do anything about them.
    2) What if there already exists one or more elements in the list. In that case, we have to take care of prev and next connection as well. We first make the new 
    node's next point to where the head is pointing that is the previous zeroth element. Then we make the prev of that element point towards our new node. Once this
    connect between previous zeroth element and our new node is made. We just move the head pointer to point towards our new node. 
If the index to be insert is not zero, then we traverse the list until we reach the end of the list or upto that index. We keep track of last and second last element
along the way. We then make the new node point towards temp, our new node has to come before new node. We set the previous and next accordingly, if temp is None, we 
dont bother about prev. 
"""
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


"""
Remove operation removes the node with the given value. If list is empty raise an exception. If data is at the zeroth index, just move the head pointer to the next element. 
Otherwise, iterate over the list, if the node with the value found. Make the prev.next point towards current.next, jumping over the current element in the process. If the current.next is not None, make the prev of current's next point towards prev. If the data is not found in the list, just return from the function.
"""
def remove(self, val):
    if self.head is None:
        raise Exception("List is empty")

    temp = self.head 
    if temp.data == val:
        self.head = temp.next
        temp.next.prev = None
        return 

    temp = self.head
    while temp is not None: 
        if temp.data == val:
            break
        prev = temp
        temp = temp.next
    
    if temp is None:
        return 

    prev.next = temp.next
    if temp.next is not None:
        temp.next.prev = prev

DoublyLinkedList.remove = remove
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

dll.remove(0)
print(dll)
dll.remove(2)
print(dll)
dll.remove(50)
print(dll)
dll.remove(99)
print(dll)
