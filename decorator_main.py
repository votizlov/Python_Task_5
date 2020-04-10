def cone(func):
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


def ice_cream(food="--ветчина--"):
    print(food)


ice_cream()
my_ice_cream = cone(ingredients(ice_cream))
my_ice_cream()
