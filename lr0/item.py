class Item:
    def __init__(self, left, right, dot_position=0):
        self.left = left
        self.right = right
        self.dot = dot_position

    def __eq__(self, other):
        return (self.left == other.left and
                self.right == other.right and
                self.dot == other.dot)

    def __hash__(self):
        return hash((self.left, tuple(self.right), self.dot))

    def __str__(self):
        right = self.right[:]
        right.insert(self.dot, "·")
        return f"{self.left} -> {' '.join(right)}"

    def next_symbol(self):
        if self.dot < len(self.right):
            return self.right[self.dot]
        return None