class MinHeap:
    # initialize empty storage array
    def __init__(self):
        self.storage = []

    def insert(self, value):
        self.storage.append(value)
        # need a bubble up method
        self.bubble_up(self.storage[(len(self.storage)-1)])

    def delete(self):
        # swap first and last items in list. pop off new last item. Sift down the new first item. return the item you lopped off
        # edge cases - 1 or 0 items in array
        if len(self.storage) == 0:
            return
        if len(self.storage) == 1:
            return self.storage.pop()

        # swap
        self.storage[0], self.storage[-1] = self.storage[-1], self.storage[0]

        # pop
        minItem = self.storage.pop()

        # roll (down)
        self.sift_down(self.storage[0])
        
        return minItem

    def bubble_up(self, index):

        parent = (index-1) // 2
        while index > 0:
            if self.storage[index] < self.storage[parent]:
                self.storage[index], self.storage[parent] = self.storage[parent], self.storage[index]
                index = parent
            else:  # item's in the right spot, return
                return

    def sift_down(self, index):
        # check value at index against values at each child
        left_child = (index * 2)+1
        right_child = (index * 2)+2
        while index < len(self.storage):
            if self.storage[index] > self.storage[left_child]:
                self.storage[index], self.storage[left_child] = self.storage[left_child], self.storage[index]
                index = left_child
            elif self.storage[index] > self.storage[right_child]:
                self.storage[index], self.storage[right_child] = self.storage[right_child], self.storage[index]
                index = right_child
