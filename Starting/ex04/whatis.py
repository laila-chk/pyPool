import sys

try:
    if len(sys.argv) < 2:
        exit()
    assert len(sys.argv) == 2, (
            "AssertionError: more than one argument is provided"
    )
    if len(sys.argv) == 2:
        try:
            n = int(sys.argv[1])
            if n % 2 == 0:
                print("I'm Even.")
            else:
                print("I'm Odd.")
        except ValueError:
            assert False, "AssertionError: argument is not an integer"

except AssertionError as e:
    print(e)
    exit()
