def all_thing_is_obj(object: any) -> int:
    if object.__class__ is list:
        print("List : ", type(object))
    elif object.__class__ is tuple:
        print("Tuple : ", type(object))
    elif object.__class__ is set:
        print("Set : ", type(object))
    elif object.__class__ is dict:
        print("Dict : ", type(object))
    elif object.__class__ is str:
        print(f"{object} is in the kitchen : ", type(object))
    else:
        print("Type not found")
    return 42
