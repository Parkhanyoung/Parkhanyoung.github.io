class Stack:
  def __init__(self):
    self.items = []

  def push(self, item):
    self.items.append(item)
    return self.items
  
  def pop(self):
    item = self.items.pop()
    return item
  def __len__(self):
    return len(self.items)

def solution(str):
  stack1 = Stack()
  items = list(str)
  for i in items:
    if i == '(':
      stack1.push(i)
    elif i == ')':
      try:
        stack1.pop()
      except:
        raise Exception('올바르지 않은 괄호쌍입니다!!!')
  if len(stack1) > 0:
    raise Exception('올바르지 않은 괄호쌍입니다!!')
  print('올바른 괄호쌍입니다.')

solution(input('괄호쌍을 입력해주세요: '))
