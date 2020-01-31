from doubly_linked_list import DoublyLinkedList


class RingBuffer:
    def __init__(self, capacity):
        self.capacity = capacity
        self.current = None
        self.storage = DoublyLinkedList()

    def append(self, item):
        # Append needs to add something to the tail if capacity isn't full and set itself to the head.  If it is full, it needs to get rid of the head and add the new item to the tail, then move to the tail

        # If not at capacity,
        if self.storage.length < self.capacity:
        # add an item to the tail
            self.storage.add_to_tail(item)
        # and update current
            self.current = self.storage.head
        # If capacity reached,
        elif self.storage.length == self.capacity:
        # get rid of the head to free up space
            drop_head = self.storage.head
            self.storage.remove_from_head()
        # and add item to the tail
            self.storage.add_to_tail(item)
        # if current is still set to drop the head, move it to the tail
            if drop_head == self.current:
                self.current = self.storage.tail

    def get(self):
        # Note:  This is the only [] allowed
        list_buffer_contents = []

        # TODO: Your code here
        # This should let you know if the DLL is empty, and if it isn't, add the initial value to the buffer contents, then continue down the list, adding each item from the DLL to the buffer contents until it has circled back around to the start.

        # check to see if the DLL is empty, and inform user if it is
        # if it is not empty,
        # add the initial value to the l_b_c
        # then check if there are more nodes to traverse
        # if there are, move to the next node
        # if there aren't, set the next node to head
        # if we haven't got back to the start yet
        # add the value of the next node to the l_b_c
        # if there's more nodes, continue moving down
        # otherwise set the next node back to head

        return list_buffer_contents

# ----------------Stretch Goal-------------------


class ArrayRingBuffer:
    def __init__(self, capacity):
        pass

    def append(self, item):
        pass

    def get(self):
        pass
