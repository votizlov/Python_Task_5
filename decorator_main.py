def C(func):
    def wrapper():
        #print()
        func()

    print("C")
    return wrapper


def B(func):
    def wrapper():
        print("B2")
        func()

    print("B1")

    return wrapper


def A(food="A"):
    print(food)


A()
notA = C(B(A))
notA()
