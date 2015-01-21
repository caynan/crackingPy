__author__ = 'caynan'

import unittest

from DataStructures.src.linked_list import LinkedList


class MyTestCase(unittest.TestCase):
    def setUp(self):
        self.list = LinkedList()

    def test_create(self):
        self.assertEqual(self.list.head, None)
        self.assertEqual(len(self.list), 0)

    def test_add(self):
        self.list.add(41)
        self.assertEqual(len(self.list), 1)

        self.list.add(0)
        self.assertEqual(len(self.list), 2)

    def test_index(self):
        # test for presence
        self.list.add(100)
        self.assertEqual(self.list.index(100), 0)

        self.list.add(-100)
        self.assertEqual(self.list.index(-100), 1)
        # test for absence
        self.assertRaises(Exception, self.list.index, 999)

    def test_remove(self):
        self.list.add(123)
        self.assertEqual(self.list.index(123), 0)
        self.list.remove(123)

        self.assertEqual(len(self.list), 0)
        self.assertRaises(Exception, self.list.index, 123)

    def test_top(self):
        self.assertTrue(self.list.top() is None)

        self.list.add('hi')
        self.assertEqual(self.list.top(), 'hi')

    def test_pop(self):
        self.assertRaises(Exception, self.list.pop)

        self.list.add([1, 2, 3])
        self.assertEqual(self.list.pop(), [1, 2, 3])
        self.assertRaises(Exception, self.list.index, [1, 2, 3])
        self.assertEqual(len(self.list), 0)


if __name__ == '__main__':
    unittest.main()
