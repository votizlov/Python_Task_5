def bread(func):
    def wrapper():
        print()
        func()

    print("<\______/>")
    return wrapper


def ingredients(func):
    def wrapper():
        print("#помидоры#")
        func()

    print("~салат~")

    return wrapper


def sandwich(food="--ветчина--"):
    print(food)


sandwich()
sandwich = bread(ingredients(sandwich))
sandwich()
