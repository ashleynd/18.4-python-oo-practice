"""Python serial number generator."""
from random import randrange

class SerialGenerator:
    """Machine to create unique incrementing serial numbers.
    
    >>> serial = SerialGenerator(start=100)

    >>> serial.generate()
    100

    >>> serial.generate()
    101

    >>> serial.generate()
    102

    >>> serial.reset()

    >>> serial.generate()
    100
    """

    # def __init__(self,a,b,c):
    #     self.a = a
    #     self.b = b
    #     self.c = c

    # def get_number(self):
    #     return randrange(self.a, self.b, self.c)
    #     # return randrange(100, 200, 1)

    def __init__(self, start=0):
        """Make a new generator, starting at start."""

        self.start = self.next = start

    def __repr__(self):
        """Show representation."""

        return f"<SerialGenerator start={self.start} next={self.next}>"

    def generate(self):
        """Return next serial."""

        self.next += 1
        return self.next - 1

    def reset(self):
        """Reset number to original start."""

        self.next = self.start
