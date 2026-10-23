
# The Iterator class is provided by LeetCode.
class PeekingIterator:
    def __init__(self, iterator):
        self.iterator = iterator
        self.next_value = iterator.next() if iterator.hasNext() else None
        self.has_value = self.next_value is not None

    def peek(self):
        return self.next_value

    def next(self):
        value = self.next_value

        if self.iterator.hasNext():
            self.next_value = self.iterator.next()
        else:
            self.next_value = None
            self.has_value = False

        return value

    def hasNext(self):
        return self.has_value
