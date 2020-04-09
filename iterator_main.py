from Abstract import Iterator
from device import Device

devices = []
f = open("Input/1.txt", "r")
f1 = f.readlines()
for x in f1:
    line = x.split()
    devices.append(Device(line[0], int(line[1]), int(line[2]), int(line[3])))


class ListIterator(Iterator):
    def __init__(self, collection, cursor):
        """
        :param collection: список
        :param cursor: индекс с которого начнется перебор коллекции.
        так же должна быть проверка -1 >= cursor < len(collection)
        """
        super().__init__(collection, cursor)

    def first(self):
        """
        Начальное значение курсора -1.
        Так как в нашей реализации сначала необходимо вызвать next
         который сдвинет курсор на 1.
        """
        self._cursor = -1

    def next(self):
        """
        Если курсор указывает на послений элемент, то вызываем StopIteration,
        иначе сдвигаем курсор на 1
        """
        if self._cursor + 1 >= len(self._collection):
            raise StopIteration()
        self._cursor += 1

    def current(self):
        """
        Возвращаяем текущий элемент
        """
        return self._collection[self._cursor]


iterator = ListIterator(devices, 0)


def main():
    names = []
    k = int(input("How many devices?"))
    m = int(input("Min memory"))
    r = int(input("Min rating"))
    priceOfAll = 0
    probableDevices = []
    for d in devices:
        iterator.next()
        if d.rate >= r and d.memo >= m:
            probableDevices.append(d)
    if not probableDevices.__len__() < k:
        for i in range(k):
            currentD = probableDevices[0]
            for d in probableDevices:
                if d.price < currentD.price:
                    currentD = d
            names.append(currentD.name)
            priceOfAll += currentD.price
            probableDevices.remove(currentD)

    f = open("Output/1.txt", "w+")
    f.write(" Price " + str(priceOfAll) + " ")
    for name in names:
        f.write(str(name) + ", ")
    print(priceOfAll)
    print(names)


main()
