# def breadth_first_traversal(self):
#     values = []
#     # Use a queue to store nodes to traverse
#     queue = Queue()
#
#     # Start by enqueuing the Root node
#     queue.enqueue(self._root_node)
#
#     # Continue while there is a node in the queue
#     while node := queue.dequeue():
#         # Save the value of the node
#         values.append(node.data)
#
#         # Enqueue the left child
#         if node._left_child:
#         queue.enqueue(node._left_child)
#
#         # Enqueue the right child
#         if node._right_child:
#             queue.enqueue(node._right_child)
#
#     # Return values
#     return values


# this file is purely for my use this code is incomplete

def depth_first_in_order(self, root_node=None, values=[]):
    """
    Traverse the tree in Depth-first in-order
    Parameters:
    - 'start_node': Optional. Where to start the traversal
    - 'values': Optional. A list of already visited nodes. For internal use only.
    Returns: A list of visited nodes in Depth-first in-order

    In-order: Left child to parent to right child
    Pre-order: Parent to left child to right child
    Post-order: Left child to right child to Parent

    To change from in order to pre-order simply add this line before the if statements
    To change from in-order to post-order simply add this line after the if statements

    """


    # If no start node, start from the Root node
    if start_node is None:
        current = self._root_node
    else:
        current = start_node

    # Visit left child, if exists
    if current._left_child:
     self.depth_first_in_order(current._left_child, values)

    # Add current node value
    values.append(current.data)

    # Visit right child, if exists
    if current._right_child:
        self.depth_first_in_order(current._right_child, values)

    # Return list of visited nodes
    return values


