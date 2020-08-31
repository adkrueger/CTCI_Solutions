from node import Node

class Linked_List(object):

    def __init__(self, head=None):
        self.head = head
    
    # insert a new node at the beginning of the list, pushing others down towards the end of the list
    def insert(self, data):
        new_node = Node(data)
        new_node.set_next(self.head)
        self.head = new_node

    # return the size of the Linked List
    def size(self):
        count = 0
        curr_node = self.head
        while curr_node:
            count += 1
            curr_node = curr_node.get_next()
        return count

    # remove the first instance of a node with the given data
    def remove(self, data):
        curr_node = self.head
        prev = None
        while curr_node:
            # if we've found the right node
            if curr_node.get_data() == data:
                # if we're not on the head node
                if prev:   
                    prev.set_next(curr_node.get_next())
                else:
                    self.head = curr_node.get_next()
                return curr_node
            prev = curr_node
            curr_node = curr_node.get_next()
        
        return None
    
    # return the first instance of a node with the given data
    def search(self, data):
        curr_node = self.head
        while curr_node:
            if data == curr_node.get_data():
                return curr_node
            curr_node = curr_node.get_next()
        return None