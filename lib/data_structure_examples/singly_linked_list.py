# The head node is going to be the very first node in our linked list, and will point to the next node once we start adding more elements.
class SinglyLinkedList:

    def __init__(self):
        self.head = None
        self.tail = None
        
        # Optional
        self.length = 0

    def append(self, node):
        # Add element to the beginning of the linked list if the linked list is empty.
        if self.head == None:
            self.head = node
            self.tail = node

        else:
            # Otherwise, add the node to the end of the linked list.
            self.tail.next_node = node

            # We also need to make sure to keep track of the new tail.
            self.tail = node

        # Optional
        self.length += 1

    def delete_tail(self):
        # There is nothing to delete if the linked list is empty.
        if self.head == None:
            return
        
        # If self.head is the only Node in the singly linked list, we set it to None, so we remove it.
        elif self.head.next_node == None:
            self.head = None
        
        else:
            # Otherwise, traverse the entire list to find the second-to-last node (prev).
            curr = self.head
            prev = None
            while curr.next_node:
                prev = curr
                curr = curr.next_node
            
            # remove the last node by removing the link between the second-to-last node and the tail.
            prev.next_node = None

        # Optional
        self.length -= 1

# Since our SinglyLinkedList class is going to contain a series of nodes linked together, we'll create a Node class.
class Node:
    def __init__(self, data, next_node=None):
        self.data = data
        self.next_node = next_node