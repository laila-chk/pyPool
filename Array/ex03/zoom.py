from load_image import ft_load

def zoom():
    print(f"The shape of image is:", end="")
    print(ft_load("animal.jpeg", False))
    print(f"New shape after slicing:", end="")
    print(ft_load("animal.jpeg", True))

def main():
    zoom()

if __name__ == "__main__":
    main()
