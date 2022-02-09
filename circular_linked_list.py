class Node:
    def __init__(self, data):
        self.data = data 
        self.next = None 


class CircularLinkedList:
    def __init__(self):
        self.head = None 


def __str__(self):
    ret_str = '['
    temp = self.head

    while temp is not None:
        ret_str += str(temp.data) + ', '
        temp = temp.next
        
        if temp == self.head:
            break

    ret_str = ret_str.rstrip(', ')
    ret_str += ']'
    return ret_str

CircularLinkedList.__str__ = __str__

def _get_last(self):
    if self.head is None:
        return None

    if self.head.next == self.head:
        return self.head 

    temp = self.head.next
    while temp.next != self.head:
        temp = temp.next

    return temp 

CircularLinkedList._get_last = _get_last


def insert(self, index, data):
    new_node = Node(data)
    last = self._get_last()
    
    if index == 0:
        new_node.next = self.head
        self.head = new_node

        if last is None:
            self.head.next = self.head 
        else:
            last.next = new_node
        return 

    temp = self.head 
    count = 1 
    while temp != last and count < index:
        temp = temp.next
        count += 1

    new_node.next = temp.next 
    temp.next = new_node

CircularLinkedList.insert = insert 
# Tests

cll = CircularLinkedList()
print(cll)

cll.insert(0, 100)
print(cll)
cll.insert(1, 200)
print(cll)
cll.insert(2, 300)
print(cll)
cll.insert(0, 0)
print(cll)
cll.insert(5, 500)
print(cll)
cll.insert(10, 10000)
print(cll)
