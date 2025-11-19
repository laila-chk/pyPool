def give_bmi(height: list[int | float],
             weight: list[int | float]) -> list[int | float]:
    """calculates BMI values for two passed lists
        arg 1: list of heights (ints or floats)
        arg 2: list of wes (ints or floats)
        returns:
            list of BMIs (ints or floats)
    """
    if (len(height) != len(weight)):
        exit("Error! lengths of passed arguments should be the same.")
    bmi = []
    for h, w in zip(height, weight):
        if ((type(h) is not int and type(h) is not float
             ) or (type(w) is not int and type(w) is not float)):
            exit("Error! Arrays should contain ints and floats only.")
        bmi.append(w/(h*h))
    return bmi


def apply_limit(bmi: list[int | float], limit: int) -> list[bool]:
    """returns a list of booleans True if list element the is above limit,
    othrewise False"""
    lim = []
    for val in bmi:
        if (type(val) is not int and type(val) is not float):
            exit("Error! Array should contain ints and floats only.")
        if (val > limit):
            lim.append(True)
        else:
            lim.append(False)
    return lim
