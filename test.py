list1 = [3, 2, 4, 4, 2, 5, 2, 5, 5]
only_one = []
first_emerge = []

for i in list1:
    if (not i in only_one) and (not i in first_emerge):
        only_one.append(i)
        first_emerge.append(i)
    elif i in only_one:
        only_one.remove(i)

def cal_count(ele):
    return list1.count(ele)

for i in only_one:
    first_emerge.remove(i)

result = list(map(cal_count, first_emerge))
result = result if 0 < len(result) else [-1]

print(result)
