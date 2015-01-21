__author__ = 'caynan'

import unittest
from DataStructures.src.binary_search_tree import BTNode
from DataStructures.src.binary_search_tree import BST


class BSTTest(unittest.TestCase):
    def setUp(self):
        self.bst = BST()

    def test_insert(self):
        self.bst.insert(41)
        self.assertEqual(self.bst.root.data, 41)

    def test_right_child(self):
        root_right = self.bst.root.right
        self.bst.insert(41) # root
        self.bst.insert(43) # root.right
        self.bst.insert(45) # root.right.right

        self.assertEqual(root_right.data, 43)
        self.assertEqual(root_right.right.data, 45)

    def test_left_child(self):
        root_left = self.bst.root.left
        self.bst.insert(41) # root
        self.bst.insert(39) # root.left
        self.bst.insert(37) # root.left.left

        self.assertEqual(root_left.data, 39)
        # self.assertEqual(root_left.left.data, 37)

    # def test_both_child(self):

if __name__ == '__main__':
    unittest.main()
