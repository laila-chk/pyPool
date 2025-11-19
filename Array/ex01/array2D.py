def slice_me(family: list, start: int, end: int) -> list:
    """ prints the shape of the 1st arg, ensures that rows = cols,
        and returns a truncated version of the array based on the
        provided start and end arguments."""
    if not family or type(family) is not list:
        exit("Error the array should be 2D and n*n")
    s = len(family[0])
    for length in family:
        if len(length) is not s:
            exit("Error the array should be 2D and n*n")
    print(f"My shape is:({len(family)},{s})")
    try:
        ret = family[start:end]
    except Exception:
        exit("Error! bad args!")
    print(f"My new shape is:({len(ret)},{s})")
    return ret
