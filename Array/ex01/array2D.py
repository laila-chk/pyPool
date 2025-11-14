# Should we verify if end exceeding len? or let it behave exactly like the slicing method 
def slice_me(family: list, start: int, end: int) -> list:
    """ prints the shape of the 1st arg, ensures that rows = cols, and returns a
        truncated version of the array based on the provided start and end arguments."""
    if not family:
        exit("Error the array should be 2D and n*n")
    s = len(family[0])
    for l in family:
        if len(l) is not s:
            exit("Error the array should be 2D and n*n")
    print(f"My shape is:({len(family)},{s})")
    try:
        ret = family[start:end] 
    except Exception :
        exit("Error! bad args!")
    print(f"My new shape is:({len(ret)},{s})")
    return ret

# def main():
#     family = [[1.80, 1],
#         [2.15, 102.7],
#         [2.10, 98.5],
#         [1.88, 75.2]]
#     fam = [[1]]
#     print(slice_me(family, 0, 2))
#     print(slice_me(family, 1, -1))
#     print(slice_me(fam, 0, 3))

# if __name__ == "__main__":
#     main()
