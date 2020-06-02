def create_an_iterator():
    """This function can pass as argument in any iterator
    constructor like list and you'll get an iterator.

    Example:
      list(create_an_iterator())
      >>> [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
    """
    for a in range(10):
        yield a


if __name__ == "__main__":
    c = list(create_an_iterator())

    print(c)
