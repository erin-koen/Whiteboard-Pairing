import unittest
'''
This problem was asked by Google.

Given the root to a binary tree, implement serialize(root), which 
serializes the tree into a string, and deserialize(s), which deserializes 
the string back into the tree.

For example, given the following Node class

class Node:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
The following test should pass:

node = Node('root', Node('left', Node('left.left')), Node('right'))
assert deserialize(serialize(node)).left.left.val == 'left.left'
'''


class Node:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def serialize(root, cache=None):
    """Given a root, serialize a tree into a string"""
    # preorder traversal
    if not cache:
        cache = []

    cache.append(root.val)
    if root.left:
        serialize(root.left, cache)
    if root.right:
        serialize(root.right, cache)

    return ', '.join(cache)


def deserialize(s):
    tree = s.split(', ')
    tree_dict = {}

    # ['root', 'left', 'left.left', 'right']
    for idx, item in enumerate(tree):

        if len(tree)-1 >= (idx*2+1):
            left = tree[idx*2+1]
        if len(tree)-1 >= (idx*2+2):
            right = tree[idx*2+2]
        tree_dict[item] = (left, right)
    
    for item in tree:
        Node(item, left, right)

    return tree_dict   

class TestSerializer(unittest.TestCase):
    def test_deserialize(self):
        node = Node('root', Node('left', Node('left.left')), Node('right'))
        serialize(node)
        # assert deserialize(serialize(node)).left.left.val == 'left.left'


if __name__ == '__main__':
    node = Node('root', Node('left', Node('left.left')), Node('right'))
    test_s = serialize(node)
    test_d = deserialize(test_s)
    print(test_s)