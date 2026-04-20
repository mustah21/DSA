from asyncio import current_task


class ListNode:
    def __init__(self, data=None, next=None, prev=None):
        self.data = data
        self.next = next

    def __repr__(self):
        return f'<ListNode: {self.data}>'

    def __str__(self):
        return str(self.data)

class Queue:
    def __init__(self):
        self._head = self._tail = None
        self._size = 0


    def __repr__(self):
        current_node = self._head
        values = ''
        while current_node:
            values += f', {current_node.data}'
            current_node = current_node.next
        plural = '' if self._size == 1 else 's'
        return f'<Queue ({self._size} element{plural}): [{", ".join(reversed(values.lstrip(", ").split(", ")))}]>'

    def enqueue(self, data):
        new_node = ListNode(data=data, next=None, prev=None)
        # If list is empty, update head and tail pointers
        if self._head is None:
            self._head = self._tail = new_node
        else:
            temp = self._tail
            temp.next = new_node
            self._tail = new_node

        self._size += 1

    def dequeue(self):
        if self._size == 0:
            return None
        else:
            temp = self._head
            self._head = self._head.next
            self._size -= 1
            return temp.data


def get_pairs(numbers):
    even = Queue()
    odd = Queue()
    result = []
    for i in numbers:
        if i % 2 == 1:
            if even._size ==  0:
                odd.enqueue(i)
            else:
                x = even.dequeue()
                pair = (x, i)
                result.append(pair)
        if i % 2 == 0:
            if odd._size == 0:
                even.enqueue(i)
            else:
                x = odd.dequeue()
                pair = (i, x)
                result.append(pair)

    return result


print(get_pairs([74, 21, 18, 22, 71, 77, 82, 16, 77, 32, 90, 37, 98, 31, 59, 37, 99, 46, 28, 65]))