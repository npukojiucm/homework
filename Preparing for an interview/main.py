class Stack:
    def __init__(self):
        self.stack = []

    def isEmpty(self):
        if len(self.stack) == 0:
            return True
        return False

    def push(self, item):
        self.stack.append(item)

    def pop(self):
        if len(self.stack) == 0:
            return None
        return self.stack.pop()

    def peek(self):
        return self.stack[-1]

    def size(self):
        return len(self.stack)


def string_balance(string):
    my_stack = Stack()

    brackets = '[({'
    balance_brackets = ['[]', '()', '{}']

    for item in string:
        if my_stack.size() == 0 and item not in brackets:
            return 'Несбалансированно'
        if item in brackets:
            my_stack.push(item)
        elif my_stack.peek() + item in balance_brackets:
            my_stack.pop()
        else:
            return 'Несбалансированно'
    if not my_stack.isEmpty():
        return 'Несбалансированно'
    return 'Сбалансированно'


string = '{}}}'

print(string_balance(string))
