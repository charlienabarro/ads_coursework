from dataclasses import dataclass

@dataclass
class Node:
    """Implements a (singly) linked-list node

    For a Node n:
        n.data holds an integer value
        n.next refers to the next Node in the linked list, or None

    You must not modify this code.
    """
    data: int
    next: 'Node' = None

@dataclass
class LinkedList:
    """Implements a (singly) linked-list

    For a LinkedList ll:
        ll.head refers to a Node that is the head of the linked list, or None
        ll.size is the size of the linked list

    You must not modify this code.
    """
    head: Node = None
    size: int = 0

@dataclass
class LinkedListWithTail:
    """Implements a (singly) linked-list

    For a LinkedList ll:
        ll.head refers to a Node that is the head of the linked list, or None
        ll.tail refers to a Node that is the tail of the linked list, or None
        ll.size is the size of the linked list

    You must not modify this code.
    """
    head: Node = None
    tail: Node = None
    size: int = 0


def show(linked_list):
    """Prints values in the order they appear in the linked list.

    Each value should be separated by a newline and no other character.
    """
    current = linked_list.head
    while current:
        print(current.data)
        current = current.next

def cat(linked_list_a, linked_list_b):
    """Concatenates two linked lists.

    Returns a LinkedList which contains all the nodes of linked_list_a followed
    by all the nodes of linked_list_b.
    """
    if linked_list_a.head is None:
        return linked_list_b
    if linked_list_b.head is None:
        return linked_list_a

    current = linked_list_a.head
    while current.next:
        current = current.next
    current.next = linked_list_b.head

    linked_list_a.size += linked_list_b.size
    return linked_list_a

def smart_cat(linked_list_a, linked_list_b):
    """Concatenates two linked lists, both with tail references.

    Returns a LinkedListWithTail which contains all the nodes of linked_list_a followed
    by all the nodes of linked_list_b.
    """
    if linked_list_a.head is None:
        return linked_list_b
    if linked_list_b.head is None:
        return linked_list_a

    linked_list_a.next = linked_list_b.head
    linked_list_a.tail = linked_list_b.tail
    linked_list_a.size += linked_list_b.size
    return linked_list_a

def make_queue():
    """Creates a linked list with the required structure.

    Returns a LinkedListWithTail containing the contents of Q as described in the
    question.
    """
    linked_list = LinkedListWithTail()
    values = [4, 9, 18, 3, 21]
    for val in values:
        new_node = Node(val)
        if linked_list.head is None:
            linked_list.head = new_node
            linked_list.tail = new_node
            linked_list.size = 1
        else:
            linked_list.tail.next = new_node
            linked_list.tail = new_node
            linked_list.size += 1
    return linked_list


def enqueue(ll_queue, value):
    """Returns a linked list representing a queue, after a new value has been
    enqueued.

    Returns a LinkedListWithTail containing the contents of a queue held in the
    LinkedListWithTail ll_queue, after a new value has been enqueued.
    """
    if ll_queue.head is None:
        ll_queue.head = Node(value)
        ll_queue.tail = Node(value)
        ll_queue.size = 1
    else:

        ll_queue.tail.next = Node(value)
        ll_queue.tail = Node(value)
        ll_queue.size += 1
    return ll_queue


def convert_to_array_queue(ll_queue):
    """
    "Converts" a LinkedList to an array-backed queue.

    Given a LinkedList ll_queue containing a tuple (A, f, r) where:

    A is a list of length 10, backing the queue
    f is an int with a value facilitating access to the front of the queue
    r is an int with a value facilitating access to the rear of the queue.
    """

    f = ll_queue.head.data
    r = ll_queue.tail.data
    A = []
    for i in range(10):
        if ll_queue.head is None:
            A.append(None)
        else:
            A.append(ll_queue.head.data)
            ll_queue.head = ll_queue.head.next
    return (A, f, r)















# test data
N1 = Node(3)
N2 = Node(7)
N1.next = N2
N2.next = None
LL1 = LinkedList()
LL1.head = N1

N3 = Node(2)
N4 = Node(8)
N3.next = N4
N4.next = None
LL2 = LinkedList()
LL2.head = N3

N5 = Node(1)
N6 = Node(9)
N5.next = N2
N6.next = None
LLWT1 = LinkedListWithTail()
LLWT1.head = N5
LLWT1.tail = N6

N7 = Node(0)
N8 = Node(4)
N7.next = N4
N8.next = None
LLWT2 = LinkedListWithTail()
LLWT2.head = N7
LLWT2.tail = N8
LLWT2.size = 2




# selected simple tests
Lcat = cat(LL1, LL2)
assert(Lcat.head == N1)
assert(Lcat.head.next.next== N3)

Lsmcat = smart_cat(LLWT1, LLWT2)
assert(Lsmcat.head == N5)
assert(Lsmcat.tail == N8)

assert(make_queue().head.next.next.data == 18)

# there is no simple test for convert_to_array_queue(ll_queue)

assert(enqueue(make_queue(), 3).size > make_queue().size)

N10= Node(1)
N11= Node(2)
N12= Node(3)
N13= Node(4)
N10.next = N11
N11.next = N12
N12.next = N13
N13.next = None
LLB = LinkedListWithTail()
LLB.head = N10
LLB.tail = N13

print(LLWT2)
print(convert_to_array_queue(LLWT2))