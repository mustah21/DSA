class Node:
    def __init__(self, data=None, next=None):
        self.data = data
        self.next = next

    def __repr__(self):
        return f'<Node: {self.data}>'


class Stack:
    def __init__(self):
        self._top = None
        self._size = 0

    def __len__(self):
        return self._size

    def peek(self):
        """
        Returns the value of the top node without altering the stack
        """
        return self._top.data if self._top else None

    def __repr__(self):
        current_node = self._top
        values = ''
        while current_node:
            values += f', {current_node.data}'
            current_node = current_node.next
        plural = '' if self._size == 1 else 's'
        return f'<Stack ({self._size} element{plural}): [{values.lstrip(", ")}]>'

    def push(self, data):
        """
        Add an element to the stack

        Parameters:
        - 'data': Data/value being added

        Returns: None
        """
        new_node = Node(data, next=self._top)
        self._top = new_node
        self._size += 1

    def pop(self):
        """
        Remove the top node from the stack and return its content

        Parameters: None

        Returns: The content of the node or None if stack is empty
        """
        # If list is empty return None
        if not self._size:
            return None

        current_node = self._top
        self._top = self._top.next
        self._size -= 1

        return current_node.data


def check_balance(text):
    stack = Stack()
    pair = 0
    index = -1

    for i in text:
        index += 1
        if i == '(':
            stack.push(i)
        elif i == ')':
            if stack.peek() is None:
                return f'Match error at position {index}'
            y = stack.pop()
            if y != '(':
                return f'Match error at position {index}'
            pair += 1

        if i == '{':
            stack.push(i)
        elif i == '}':
            if stack.peek() is None:
                return f'Match error at position {index}'
            y = stack.pop()
            if y != '{':
                return f'Match error at position {index}'
            pair += 1
        if i == '[':
            stack.push(i)
        elif i == ']':
            if stack.peek() is None:
                return f'Match error at position {index}'
            y = stack.pop()
            if y != '[':
                return f'Match error at position {index}'
            pair += 1

    if stack.peek() is not None:
        return f'Match error at position {index}'


    return f'Ok - {pair}'


check_balance('a(b)c[d]e{f}g')
