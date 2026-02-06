#!/usr/bin/env python3
"""Python class inheritance script"""


class SwimMixin:
    """A class that defines creatures that swim"""

    def swim(self):
        print("The creature swims!")


class FlyMixin:
    """A class that defines creatures that fly"""

    def fly(self):
        print("The creature flies!")


class Dragon(SwimMixin, FlyMixin):
    """A class that defines a dragon"""

    def roar(self):
        print("The dragon roars!")
