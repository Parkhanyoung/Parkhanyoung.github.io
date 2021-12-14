class Stack:
    def __init__(self):
      self.items = []

    def push(self, item):
      self.items.append(item)
    
    def pop(self):
      try:
        return self.items.pop()
      except IndexError:
        print('Stack is empty')

    def top(self):
      try:
        return self.items[-1]
      except IndexError:
        print('Stack is empty')
        return False

    def __len__(self):
      return len(self.items)

# infix > postfix > 연산
# 피연산자: top stack
# +-*/: opstack / (): opstack / 
def to_postfix(formula):
    topstack = []
    opstack = Stack()
    for i in formula:
        if i.isnumeric():
            topstack.append(i)
        elif i == '+' or i ==  '-':
            if opstack.top() == '*' or opstack.top() == '/':
                topstack.append(opstack.pop())
            opstack.push(i)
        elif i == '(':
            opstack.push(i)
        elif i == '*' or i == '/':
            opstack.push(i)
        elif i == ')':
            while True:
                a = opstack.pop()
                if a == '(':
                    break
                topstack.append(a)
    while opstack.top():
        topstack.append(opstack.pop())
    return topstack

