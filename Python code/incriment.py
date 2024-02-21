class Counter:
    def __init__(self, min_val, max_val):
        self.min_val = min_val
        self.max_val = max_val
        self.dir_val = 1  # Start with positive direction
        self.val = min_val

    def increment(self):
        self.val += self.dir_val

        if self.val >= self.max_val or self.val <= self.min_val:
            self.dir_val = -self.dir_val

        return self.val
