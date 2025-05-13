import sys


def ft_filter(function, iterable):
    return [elm for elm in iterable if function(elm)]


def main():
    """
        filterstring takes a string (S), and an integer (N) and outputs
        a list of words from S that have a length greater than N.
    """
    try:
        assert len(sys.argv) == 3, (
                "AssertionError: the arguments are bad"
                )
        try:
            num = int(sys.argv[2])
        except ValueError:
            raise AssertionError("AssertionError: the arguments are bad")

        words = sys.argv[1].split(' ')
        ret = ft_filter(lambda word: len(word) > num, words)
        print(ret)
    except AssertionError as e:
        print(e)
        exit()


if __name__ == "__main__":
    main()
