class Jar:
    def __init__(self, capacity=12):
        self.capacity = capacity
        self.size = 0

    def __str__(self):
        return "🍪" * self.size

    def deposit(self, n):
        if n + self.size > self.capacity:
            raise ValueError("Amount is too high")
        self.size += n

    def withdraw(self, n):
        if self.size - n < 0:
            raise ValueError("Amount is too high")
        self.size -= n

    @property
    def capacity(self):
        return self._capacity

    @capacity.setter
    def capacity(self, capacity):
        if capacity < 0:
            raise ValueError("Invalid Capacity")
        self._capacity = int(capacity)  # Check for float still due

    @property
    def size(self):
        return self._size

    @size.setter
    def size(self, size):
        self._size = size


def main():
    jar = Jar()
    jar.deposit(1)
    print(jar)
    print(jar.capacity)


if __name__ == "__main__":
    main()
