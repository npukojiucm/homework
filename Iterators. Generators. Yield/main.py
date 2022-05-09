def FlIterator(list_):              # Задание 2, 4
    for item in list_:
        if not isinstance(item, list):
            yield item
        else:
            for item1 in FlIterator(item):
                yield item1


class MyIter:       # Задание 1, 3
    def __init__(self, lst):
        self.lst = lst
        self.list_ = [item for item in self.FlatIterator(lst)]

    def FlatIterator(self, lst):
        for item in lst:
            if not isinstance(item, list):
                yield item
            else:
                for item1 in self.FlatIterator(item):
                    yield item1

    def __iter__(self):
        self.cursor = -1
        self.cursor2 = -1
        return self

    def __next__(self):
        self.cursor += 1
        if self.cursor == len(self.list_):
            raise StopIteration
        return self.list_[self.cursor]


nested_list = [
    ['a', 'b', 'c', 'q'],
    ['d', 'e', 'f', 'h', False],
    [1, 2, None],
]
nested_list1 = [
    ['a', [1, 2, None], 'b', ['a', [1, 2, [1, 2, None], None], 'b', 'c'], 'c'],
    ['d', 'e', [1, 2, None], 'f', 'h', False],
    [1, 2, ['f', 'h', False], None],
]

for item in FlIterator(nested_list1):  # Задание 2, 4
    print(item)
flat_list = [item for item in FlIterator(nested_list1)]  # Задание 2, 4
print(flat_list)

for item in MyIter(nested_list1):    # Задание 1, 3
    print(item)

flat = [item for item in MyIter(nested_list1)]    # Задание 1, 3
print(flat)
