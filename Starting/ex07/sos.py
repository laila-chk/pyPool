import sys


def main():
    """
    Function to encode strings in Morse Code.
    """
    try:
        assert len(sys.argv) == 2, (
            "AssertionError: the arguments are bad"
        )
        s = ""
        code = {
            'a': '.-', 'b': '-...', 'c': '-.-.', 'd': '-..', 'e': '.', 'f': '..-.',
            'g': '--.', 'h': '....', 'i': '..', 'j': '.---', 'k': '-.-',
            'm': '--', 'n': '-.', 'o': '---', 'p': '.--.', 'q': '--.-', 'r': '.-.',
            's': '...', 't': '-', 'u': '..-', 'v': '...-', 'w': '.--', 'x': '-..-',
            'y': '-.--', 'z': '--..', ' ': '/', 'l': '.-..',
            '0': '-----', '1': '.----', '2': '..---', '3': '...--', '4': '....-',
            '5': '.....', '6': '-....', '7': '--...', '8': '---..', '9': '----.'}
        for c in sys.argv[1]:
                assert c.isalnum() or c == ' ', (
                    "AssertionError: the arguments are bad"
                )
                s += code[c.lower()] + ' '
        print(s)
    except AssertionError as e:
        print(e)
        exit()


if __name__ == "__main__":
    main()
