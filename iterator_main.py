from Abstract import Iterator



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


import textwrap

f = open("Input/1.txt", "r")
f1 = f.readlines()
textWith = 10
iterator = ListIterator(f1, -1)

f = open("Output/1.txt", "w+")
iterator.first()
for l in f1:
    iterator.next()
    f.write("\n" + "      " + textwrap.fill(iterator.current(), textWith))
