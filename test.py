import numbers

class Stack:
    def __init__(self):
      self.items = []

    def push(self, item):
      self.items.append(item)
    
    def pop(self):
        return self.items.pop()

    def top(self):
        return self.items[-1]

    def is_empty(self):
        return bool(len(self.items) == 0)

    def __len__(self):
        return len(self.items)

def split_tokens(tokens):
    result = []
    val = 0
    val_processing = False
    for i in tokens:
        if i in '0123456789':
            i = int(i)
            val = val * 10 + i
            val_processing = True
        else:
            if val_processing:
                result.append(val)
                val = 0
                val_processing = False
            result.append(i)

    if val_processing:
        result.append(val)
    return result

def into_postfix(token_list):
    result = []
    opstack = Stack()
    priority = {
      '+': 1,
      '-': 1,
      '(': 1,
      '*': 2,
      '/': 2,
      ')': 3
    }

    for i in token_list:
        if isinstance(i, int):
            result.append(i)
        elif i == ')':
            while not opstack.top() == '(':
                result.append(opstack.pop())
            opstack.pop()
        else:
            if opstack.is_empty():
                opstack.push(i)
            else:
              if priority[i] < priority[opstack.top()]:
                  result.append(opstack.pop())
                  opstack.push(i)
              else:
                  opstack.push(i)
    if not opstack.is_empty():
        while not opstack.is_empty():
            result.append(opstack.pop())
    return result

def calculate(postfix):
    int_stack = Stack()
    for i in postfix:
        if isinstance(i, numbers.Number):
            int_stack.push(i)
        else:
            n1 = int_stack.pop()
            n2 = int_stack.pop()
            if i == '+':
                new_int = n1 + n2
            if i == '-':
                new_int = n1 - n2
            if i == '*':
                new_int = n1 * n2
            if i == '/':
                new_int = n2 / n1
            int_stack.push(new_int)
    return int_stack.top()

def cal_tokens(tokens):
    token_list = split_tokens(tokens)
    postfix = into_postfix(token_list)
    result = calculate(postfix)
    return result

print(cal_tokens('(3+2)*3/136'))