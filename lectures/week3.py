# Create a dictionary
dic = {'a': 1, 'b': 2, 'c': 3}

# Create a list of (key, val) tuples called `pairs`
pairs = []
for key, value in dic.items( ):
    pairs.append((key,value))

# print(pairs)

# Some data (list of tuples)
data = [
  ('a', 1),
  ('b', 2),
  ('c', 3),
  ]

# Create a dict comprehension
dic = {k:v for k, v in data}
# Some data (list of tuples)
data = [
    ('a', 1),
    ('b', 2),
    ('c', 3),
]

# Create a dict comprehension
dic = {k: v for k, v in data}
# print(f'`dic` is {dic}')
# print(f'type(dic) is: {type(dic)}')

# Create a list comprehension
lst = [(k, v) for k, v in data]
print(f'`lst` is {lst}')
print(f'type(lst) is {type(lst)}')

# Create a set comprehension
st = {k for k, v in data}
# print(f'`st` is {st}')
# print(f'type(st) is {type(st)}')
# print(f'`dic` is {dic}')
# print(f'type(dic) is: {type(dic)}')

# Create a list comprehension
lst = [(k, v) for k, v in data]
# print(f'`lst` is {lst}')
# print(f'type(lst) is {type(lst)}')

# Create a set comprehension
st = {k for k, v in data}
print(f'`st` is {st}')
print(f'type(st) is {type(st)}')