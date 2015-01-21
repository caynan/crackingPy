__author__ = 'caynan'

class BTNode(object):
    def __init__(self, data=None, left=None, right=None):
        self.data = data
        self.left = left
        self.right = right

    def __str__(self):
        return str(self.data)

    def is_empty(self):
        """
        Check if node is empty.

        :return: Boolean value, True if node is empty false otherwise.
        """
        return self.data is None

    def insert(self, data):
        # Base Case
        if self.is_empty():
            self.data = data
            # create empty nodes for childes
            self.left = BTNode()
            self.right = BTNode()
            return self
        elif self.data >= data:
            return self.left.insert(data)
        else:
            return self.right.insert(data)


class BST(object):
    def __init__(self):
        """
        A Binary Search Tree (BST) Implementation.

        :type root: BTNode
        """
        # initialize empty nodes as childs
        left = BTNode()
        right = BTNode()

        self.root = BTNode(left=left, right=right)


    def insert(self, data):
        return self.root.insert(data)
