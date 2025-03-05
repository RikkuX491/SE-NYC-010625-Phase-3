class Tree:
    def __init__(self):
        self.root = None

        # Optional - to keep track of the length of the tree
        self.length = 0

    # Idea for an example append() method
    def append(self, new_node, node_to_add_child_to=None):
        # If we specify a node to add a child to, we'll execute the code in this if statement block
        if node_to_add_child_to != None:
            node_to_add_child_to.children.append(new_node)

        # Otherwise, we'll check if self.room is None and set the value appropriately
        elif self.root == None:
            self.root = new_node

        # Else - we add the node to the root's children list
        else:
            self.root.children.append(new_node)

        self.length += 1

    # An example use case for Tree traversal
    def traverse(self, current_node):
        if self.root == None:
            print("There are no elements in the tree.")
            return
        else:
            print(current_node.value)

            for child in current_node.children:
                self.traverse(child)

class Node:
    def __init__(self, value):
        self.value = value
        self.children = []