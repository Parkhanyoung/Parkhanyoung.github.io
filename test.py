d_1 = {'a': 1, 'b': 2, 'c': 3}
d_2 = {'d': 4, 'e': 5, 'f': 6}
result1 = {}
result = {k: v for d in [d_1, d_2] for k,v in d.items()}
print({k: v for k, v in d_1.items()})