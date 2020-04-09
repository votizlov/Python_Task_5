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





import random

from student import Student


def findCourceIndex(array, student):
    for i in range(len(array)):
        if array[i][0].cource == student.cource:
            return i
    return -1


coursesWithStudents = []
f = open("Test input/1.txt", "r")
f1 = f.readlines()
for x in f1:
    line = x.split()
    stud = Student(line[0], int(line[1]), line[2], int(line[3]))
    if findCourceIndex(coursesWithStudents, stud) == -1:
        coursesWithStudents.append([stud])
    else:
        coursesWithStudents[findCourceIndex(coursesWithStudents, stud)].append(stud)

iterator = ListIterator(coursesWithStudents, 0)


def main():
    output = ""
    for cource in coursesWithStudents:
        iterator.next()
        bestMales = [Student("", "", "male", 0)]
        bestFemales = [Student("", "", "female", 0)]
        for stud in cource:
            if stud.sex == "male":
                if stud.avg > bestMales[0].avg:
                    bestMales.clear()
                    bestMales.append(stud)
                elif stud.avg == bestMales[0].avg:
                    bestMales.append(stud)
            if stud.sex == "female":
                if stud.avg > bestFemales[0].avg:
                    bestFemales.clear()
                    bestFemales.append(stud)
                elif stud.avg == bestFemales[0].avg:
                    bestFemales.append(stud)
        if bestMales[0].avg > 0 and bestFemales[0].avg > 0:
            output = output + "Курс: " + str(cource[0].cource) + " " + random.choice(
                bestFemales).name + " " + random.choice(
                bestMales).name + "\n"

    f = open("Output/1.txt", "w+")
    f.write(output)
    print(output)


main()
