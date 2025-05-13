import sys


def counter(text: str):
    """function to count characters of each type and print their amount """
    upper, lower, ponct, spc, dig = 0, 0, 0, 0, 0
    for c in text:
        if c.isupper():
            upper += 1
        elif c.islower():
            lower += 1
        elif c.isdigit():
            dig += 1
        elif c.isspace():
            spc += 1
        elif c in "!\"#$%&'()*+,-./:;<=>?@[]]\\^_`{|}~":
            ponct += 1
    print("The text contains", len(text), " characters:")
    print(upper, " upper letters")
    print(lower, " lower letters")
    print(ponct, " punctuation marks")
    print(spc, "spaces")
    print(dig, "digits")


def main():
    """ the main function that takes input from the user and calls
        counter to do the counting"""
    try:
        assert len(sys.argv) <= 2, (
                "AssertionError: more than one argument is provided"
                )
        if len(sys.argv) < 2:
            print("what is the text to count?")
            text = sys.stdin.read()
        else:
            text = sys.argv[1]
        counter(text)
    except AssertionError as e:
        print(e)
        exit()

if __name__ == "__main__":
    main()
