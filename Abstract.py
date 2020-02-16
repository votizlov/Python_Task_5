import abc


class Aggregate(abc.ABC):

    @abc.abstractmethod
    def iterator(self):
        """
        Возвращает итератор
        """
        pass


class Iterator(abc.ABC):
    def __init__(self, collection, cursor):
        self._collection = collection
        self._cursor = cursor

    @abc.abstractmethod
    def first(self):
        """
        Возвращает итератор к началу агрегата.
        Так же называют reset
        """
        pass

    @abc.abstractmethod
    def next(self):
        """
        Переходит на следующий элемент агрегата.
        Вызывает ошибку StopIteration, если достигнут конец последовательности.
        """
        pass

    @abc.abstractmethod
    def current(self):
        """
        Возвращает текущий элемент
        """
        pass