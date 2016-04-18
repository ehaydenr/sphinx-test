"""My Library Functions"""

def calculateTip(total, percentage):
    """Compute Tip

    Calculates ``total * percentage``
    
    :param total: The sum to calculate the tip with
    :param percentage: The percentage to tip
    :returns: Amount to tip

    Examples

    >>> from test import mylib
    >>> mylib.calculateTip(80, 15)
    12.0
    """

    return total * percentage / 100

def sayHello():
    """Say Hello to the user.

    Prints \"Hello\" to stdout.

    Examples

    >>> from test import mylib
    >>> mylib.sayHello()
    Hello
    """

    print("Hello")

def factorial(n):
    """Compute Factorial

    Calculates factorial of n.

    :param n: Number to compute factorial of
    :returns: Value of factorial evaluated

    Examples

    >>> from test import mylib
    >>> mylib.factorial(5)
    120
    """

    if n == 0 or n == 1:
        return 1
    return n  * factorial(n-1)
