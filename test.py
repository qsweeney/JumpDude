
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

# Example usage:
min_value = 1
max_value = 5
counter_instance = Counter(min_value, max_value)

while True:
    print(counter_instance.increment())