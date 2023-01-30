"""
Detect a cycle in a linked list. Note that the head pointer may be 'None' if the list is empty.

A Node is defined as: 
 
    class Node(object):
        def __init__(self, data = None, next_node = None):
            self.data = data
            self.next = next_node
"""


def has_cycle(head):
    # https://www.hackerrank.com/challenges/ctci-linked-list-cycle/forum/comments/202178?h_l=interview&isFullScreen=true&playlist_slugs%5B%5D=interview-preparation-kit&playlist_slugs%5B%5D=linked-lists
    if head == None:
        return False

    nodes = set()
    while head != None:
        if head in nodes:
            return True
        nodes.add(head)
        head = head.next

    return False
    