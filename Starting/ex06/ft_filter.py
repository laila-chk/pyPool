def ft_filter(function, iterable):
    """filter(function or None, iterable) --> filter object
    Return an iterator yielding those items of iterable for which function(item)
    is true. If function is None, return the items that are true."""
    if function is None:
        return [elm for elm in iterable if elm ]
    return [elm for elm in iterable if function(elm)]



# def is_even(n):
#     return n % 2 == 0

# numbers = [1, 2, 3, 4, 5, 6]

# even_numbers = ft_filter(is_even, numbers)
# print(list(even_numbers))  
# data = ["apple", "", "banana", "", "cherry"]
# non_empty = ft_filter(None, data)
# print(list(non_empty))
