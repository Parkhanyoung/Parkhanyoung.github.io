repeat = int(input())
for _ in range(repeat):
  a, b = map(int, input().split())
  dist = b - a

  n = 1
  if dist == 1:
      print(1)
  else:
      while dist > n**2 + 2*n:
        n += 1
      if dist % (n * (n+1) / 2) == 0:
          result = 2*n - 1 
      else:
          result = 2*n

      print(result)