class Heap:
    def __init__(self):
        self._heap = []
        self._size = 0

    def _float(self):
        """
        Float the last element of the heap until the heap is in order
        """

        child_index = self._size - 1
        element_to_check = self._heap[child_index]
        parent_index = (child_index - 1) // 2

        while self._heap[parent_index] > self._heap[child_index]:
            replace = self._heap[child_index]
            self._heap[child_index] = self._heap[parent_index]
            self._heap[parent_index] = replace
            child_index = parent_index
            parent_index = (child_index - 1) // 2
            if child_index < 1:
                break

        return self._heap

    def insert(self, value):
        # Add the value to the heap
        self._heap.append(value)
        # Update size of the heap
        self._size += 1
        # And float the last element of the heap
        self._float()

    def _sink(self):
        """
        Sinks the root node of the heap until the heap is in order
        """

        parent_index = 0

        while True:

            child_left_index = (2 * parent_index) + 1
            child_right_index = (2 * parent_index) + 2
            smallest = parent_index

            if child_left_index < self._size and self._heap[child_left_index] < self._heap[smallest]:
                smallest = child_left_index

            if child_right_index < self._size and self._heap[child_right_index] < self._heap[smallest]:
                smallest = child_right_index

            if smallest == parent_index:
                break

            replace = self._heap[parent_index]
            self._heap[parent_index] = self._heap[smallest]
            self._heap[smallest] = replace
            parent_index = smallest

        return self._heap



h = Heap()
h._heap = [8, 6, 5, 9, 7]
h._size = 5
h._sink()
print(h._heap)

