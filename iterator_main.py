from Abstract import Iterator

f = open("Input/1.txt", "r")
f1 = f.readlines()


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


iterator = ListIterator(f1, 0)


def reverse_text(lines):
    res = ""
    for i in range(lines.__len__()):
        resLine = ""
        line = iterator.current().split()
        for j in line:
            resLine += (j[::-1])
            resLine += " "
        res += resLine
        res += "\n"
    return str(res)


print(reverse_text(f1))
f = open("Output/1.txt", "w+")
f.write(reverse_text(f1))
