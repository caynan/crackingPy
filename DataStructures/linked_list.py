__author__ = 'caynan'


class _Node(object):
    def __init__(self, data=None, next=None):
        self.data = data
        self.next = next

    def __str__(self):
        return str(self.data)


class LinkedList(object):
    def __init__(self):
        self.length = 0
        self.head = None

    def __str__(self):
        return self._toString()

    def __len__(self):
        return self.length

    def _toString(self):
        node = self.head
        string_to_return = ''

        # while not None will print the value of the node
        while node:
            string_to_return += '%s ' % node
            node = node.next

        return string_to_return.strip()

    def add(self, data):
        if self.head is None:
            self.head = _Node(data=data)
            self.length += 1
        else:
            node = self.head

            while node:
                if node.next is None:
                    node.next = _Node(data=data)
                    self.length += 1
                    break
                else:
                    node = node.next

    def index(self, x):
        node = self.head

        for i in range(self.length):
            if node.data == x:
                return i
            else:
                node = node.next

        raise Exception('Item Not Found!')

    def remove(self, x):
        # case is empty
        if self.head is None:
            raise Exception('Trying to remove from empty list')
        # case is head
        elif self.head.data == x:
            self.head = None
            self.length -= 1
        # other cases
        else:
            node = self.head
            # while node not None
            while node:
                if node.next is None:
                    raise Exception('Element not found!')
                elif node.next.data == x:
                    node.next = node.next.next
                    self.length -= 1
                else:
                    node = node.next

    def top(self):
        if self.head is None:
            return None
        else:
            return self.head.data

    def pop(self):
        node = self.head

        if node is None:
            raise Exception('List is Empty')
        else:
            data = node.data
            self.head = self.head.next
            self.length -= 1

            return data










