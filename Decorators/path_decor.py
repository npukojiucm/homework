from logger import path_file


@path_file('C:/Users/Александр/Desktop/homework/Decorators/log/logs.txt')
def FlIterator(list_):
    for item in list_:
        if not isinstance(item, list):
            yield item
        else:
            for item1 in FlIterator(item):
                yield item1


nested_list1 = [
    ['a', [1, 2, None], 'b', ['a', [1, 2, [1, 2, None], None], 'b', 'c'], 'c'],
    ['d', 'e', [1, 2, None], 'f', 'h', False],
    [1, 2, ['f', 'h', False], None],
]

FlIterator(nested_list1)
