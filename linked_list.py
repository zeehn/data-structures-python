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


"""
The pop method can have one of the three cases:
1) List is empty. In that case, we can't pop an item. Hence, raised an exception
2) List has only one node that head is pointing to. In that case, we just return the value and point the head to None.
3) List has more than one element. In such a scenario, we need both previous and next element. We traverse the entire list while keeping
track of both prev and current node reference. Once we the reach the end of the list, where temp.next is None, we return the temp.data and
point the next reference of prev node to None or to the next reference of current node which is again None because we are at the last element
in the list. 
"""

def pop(self):
    #case 1
    if self.head is None:
        raise Exception("Cannot pop! No value.")

    # case 2
    if self.head.next is None:
        val = self.head.data
        self.head = self.head.next
        return val
    
    # case 3
    temp = self.head
    while temp.next is not None:
        prev = temp  
        temp = temp.next
    
    val = temp.data
    prev.next = temp.next
    return val 

LinkedList.pop = pop 

"""
Insert method takes index and data as a parameter. The operation is to insert the given data at the given index. 
If the index is 0, that means we have to insert the element at the very beginning of the list. First, we create a new node by creating an
instance from the Node class. Then, we make the new node's next reference point to where head is pointing to right now, that is towards the
0th element right now that will become first element once we complete our operation. Next up, we make the head point to the new_node and we 
are done if index was 0.

For all other cases, we have to traverse the list until we either reach the end of the list or reach the given index. This also covers out of 
bound index. For example, if we have 3 nodes and we have an index to insert at 5, since we are traversing either we reach the end of the list or
less than index, we will only insert it at the end if the index is out of bound.  

"""


def insert(self, index, data):
    new_node = Node(data)

    if index == 0:
        new_node.next = self.head
        self.head = new_node
        return 
    
    temp = self.head
    count = 0
    while temp is not None and count < index: 
        prev = temp 
        temp = temp.next
        count += 1

    new_node.next = temp 
    prev.next = new_node



LinkedList.insert = insert

"""


"""
def remove_by_index(self, index):
    if self.head is None:
        raise Exception("List is empty!")

    temp = self.head
    
    if index == 0:
        val = temp.data
        self.head = temp.next
        return val

    count = 0
    while temp is not None and count < index: 
        prev = temp
        temp = temp.next
        count += 1

    if temp is None:
        raise Exception("Position does not exist.")

    val = temp.data
    prev.next = temp.next
    return val

LinkedList.remove_by_index = remove_by_index 


"""

"""

#TESTS
ll = LinkedList()
ll.push(1)
ll.push(2)
ll.push(3)
ll.push(4)
ll.push(5)
print(ll)

ll.pop()
print(ll)
ll.pop()
print(ll)
ll.pop()
print(ll)
ll.insert(0, 0)
print(ll)

ll.insert(3, 5)
print(ll)
ll.insert(3, 4)
print(ll)

ll.remove_by_index(2)
print(ll)

ll.remove_by_index(0)
print(ll)

ll.remove_by_index(2)
print(ll)

ll.remove_by_index(3)
print(ll)

ll.remove_by_index(0)
print(ll)

ll.remove_by_index(0)
