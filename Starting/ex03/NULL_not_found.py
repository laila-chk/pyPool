def NULL_not_found(object: any) -> int:
    if object is None:
        print("Nothing: None ", type(object))
    elif isinstance(object, float) and object != object:
        print("Cheese: ", object, type(object))
    elif not object:
        if isinstance(object, bool):
            print("Fake: ", object, type(object))
        elif isinstance(object, int):
            print("Zero: ", object, type(object))
        elif isinstance(object, str):
            print("Empty: ", object, type(object))
    else:
        print("Type not Found")
        return 1
    return 0
