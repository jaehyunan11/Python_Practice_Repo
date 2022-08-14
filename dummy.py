def test():
    print("Hello World!")


def loop():
    arr = []
    str = "This is test"
    str = str.split()
    for i in str:
        print(len(i))
        if len(i) > 3:
            arr.append(i)
    print(arr)


def main():
    test()
    loop()


if __name__ == "__main__":
    main()
