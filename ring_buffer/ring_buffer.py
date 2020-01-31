from doubly_linked_list import DoublyLinkedList


class RingBuffer:
    def __init__(self, capacity):
        self.capacity = capacity
        self.current = None
        self.storage = DoublyLinkedList()

    def append(self, item):
        # Append needs to add something to the tail if capacity isn't full and set itself to the head.  If it is full, it needs to get rid of the head and add the new item to the tail, then move to the tail

    def get(self):
        # Note:  This is the only [] allowed
        list_buffer_contents = []

        # TODO: Your code here
        # This should let you know if the DLL is empty, and if it isn't, add the initial value to the buffer contents, then continue down the list, adding each item from the DLL to the buffer contents until it has circled back around to the start.

        return list_buffer_contents

# ----------------Stretch Goal-------------------


class ArrayRingBuffer:
    def __init__(self, capacity):
        pass

    def append(self, item):
        pass

    def get(self):
        pass
