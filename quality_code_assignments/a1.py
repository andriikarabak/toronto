def num_buses(n):
    """ (int) -> int

    Precondition: n >= 0

    Return the minimum number of buses required to transport n people.
    Each bus can hold 50 people.

    >>> num_buses(101)
    3
    >>> num_buses(0)
    0
    >>> num_buses(50)
    1
    """

    if n < 0:
        raise ValueError('Number of people has to be higher or equal to zero.')
    else:
        return n // 50 + int(bool(n % 50))

def stock_price_summary(price_changes):
    """ (list of number) -> (number, number) tuple

    price_changes contains a list of stock price changes. Return a 2-item
    tuple where the first item is the sum of the gains in price_changes and
    the second is the sum of the losses in price_changes.

    >>> stock_price_summary([0.01, 0.03, -0.02, -0.14, 0, 0, 0.10, -0.01])
    (0.14, -0.17)
    >>> stock_price_summary([0, 0])
    (0.0, 0.0)
    >>> stock_price_summary([0.01, -0.01, 0.02, -0.02, 0.1, -0.1])
    (0.13, -0.13)
    """

    gains = 0.0
    losses = 0.0

    if len(price_changes) == 0:
        return ()
    else:
        for number in price_changes:
            if number > 0:
                gains += number
            elif number < 0:
                losses += number
        return (gains, losses)

def swap_k(L, k):
    """ (list, int) -> NoneType

    Precondtion: 0 <= k <= len(L) // 2

    Swap the first k items of L with the last k items of L.

    >>> nums = [1, 2, 3, 4, 5, 6]
    >>> swap_k(nums, 2)
    >>> nums
    [5, 6, 3, 4, 1, 2]
    >>> nums = [1, 2, 3, 4, 5, 6]
    >>> swap_k(nums, 0)
    >>> nums
    [1, 2, 3, 4, 5, 6]
    >>> nums = [1, 2, 3, 4, 5, 6, 7, 8, 9]
    >>> swap_k(nums, 4)
    >>> nums
    [6, 7, 8, 9, 5, 1, 2, 3, 4]
    """

    L_length = len(L)

    if k < 0 or k > L_length // 2:
        raise ValueError('k parameter has to satisfy precondition: 0 <= k <= len(L) // 2.')
    else:
        L[:] = L[L_length - k:] + L[k: L_length - k] + L[: k]


if __name__ == '__main__':
    import doctest
    doctest.testmod()