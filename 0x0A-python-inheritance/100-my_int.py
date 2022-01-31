#!/usr/bin/python3

class MyInt(int):
    """
    MyInt is a rebel. MyInt has == and != operators inverted
    """
    def __eq__(self, other):
        """
        eq method altered
        """
        return False

    def __ne__(self, other):
        """
        ne method altered
        """
        return True
