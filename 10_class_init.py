"""
Exercise 1

Create a class called Counter with two methods:
  * increment -> increments an internal counter
  * print_counter -> print the counter value
"""


class Counter:
    def __init__(self):
        self._value = 0
        name = input("How do you want to name your counter? \n")
        self._name = name

    def increment(self):
        self._value += 1

    def print_counter(self):
        print(self._name, "is equal to:", self._value)


"""
Exercise 2

Create a class called MyList with a constructor taking the list name and two methods:
  * add_elt -> add an element to the internal list
  * clear -> clear the internal list
  * print_list -> print the name of the list followed by the elements of the list
"""


class MyList:
    def __init__(self, name):
        self._name = name
        self._list = []

    def add_elt(self, elt):
        self._list.append(elt)

    def clear(self):
        self._list.clear()

    def print_list(self):
        print(self._name, "contains:")
        for elt in self._list:
            print(elt)


if __name__ == '__main__':
    aCounter = Counter()
    aCounter.increment()
    aCounter.increment()
    aCounter.increment()
    aCounter.print_counter()

    firstList = MyList("First")
    firstList.add_elt(10)
    firstList.add_elt("List!!")
    firstList.add_elt(888)
    firstList.print_list()
    firstList.clear()
    firstList.print_list()

