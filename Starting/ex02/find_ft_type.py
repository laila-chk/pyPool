def all_thing_is_obj(object: any) -> int:
    if object.__class__ is list:
        print(f"List : <class 'list'>")
    elif object.__class__ is tuple:
        print(f"Tuple : <class 'tuple'>")
    elif object.__class__ is set:
        print(f"Set : <class 'set'>")
    elif object.__class__ is dict:
        print(f"Dict : <class 'dict'>")
    elif object.__class__ is str:
        print(f"{object} is in the kitchen : <class 'str'>")
    else:
        print("Type not found")
    return 42

