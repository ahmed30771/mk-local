def add(*arg):
    return sum(arg)


if __name__ == "__main__":
    nums = [1, 2, 3, 4, 5]
    print(add(*nums))
