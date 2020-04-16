def ice_cream(func):
    def wrapper():
        func()

    print("СИРОП")
    return wrapper


def ingredients(func):
    def wrapper():
        print("МАРОЖЕНАЕ")
        func()

    print("СТРУЖКА")

    return wrapper


def cone(food="РОЖОК"):
    print(food)


cone()

print()
my_ice_cream = ice_cream(ingredients(cone))
my_ice_cream()
