values = []
for x in range(10):
    values.append(x)
# print(values)

values = [x + 5 for x in range(10)]
# print(values)


evens = []
for number in range(50):
    is_even = number % 2 == 0
    if is_even:
        evens.append(number)
        
evens = [number for number in range(50) if number % 2 == 0]
evens = [
    number 
    for number in range(50) 
    if number % 2 == 0 
]
# print(evens)


options = ['any','alban','apple','world','hello','']
valid_options = []
for string in options:
    if len(string) <= 1:
        continue
    if string[0] != "a":
        continue
    if string[-1] != 'y':
        continue
    valid_options.append(string)    
# print(valid_options)


options = ['any','alban','apple','world','hello','']
valid_options = [
    string
    for string in options
    if len(string) >= 2
    if string[0] == 'a'
    if string[-1] == 'e'
]
# print(valid_options)


matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]
flattened = []
for row in matrix:
    for num in row:
        flattened.append(num)
# print(flattened)

matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]
flattened = [
    number
    for row in matrix
    for number in row
]
# print(flattened)


categories = []
for number in range(10):
    if number % 2 == 0:
        categories.append("Even")
    else:
        categories.append("Odd")
# print(categories)

categories = ["Even" if number % 2 == 0 else "Odd" for number in range(10)]
# print(categories)


import pprint
printer = pprint.PrettyPrinter()
lst = []
for a in range(5):
    l1 = []
    for b in range(5):
        l2 = []
        for num in range(5):
            l2.append(num)
        l1.append(l2)
    lst.append(l1)
# printer.pprint(lst)

lst = [
    [
        [
            num for num in range(5)
        ]
        for _ in range(5)
    ]
    for _ in range(5)
]
lst = [[[num for num in range(5)] for _ in range(5)] for _ in range(5)]
# printer.pprint(lst)


def square(x): return x**2
def valid(x): return True
squared_numbers = [square(x) for x in range(10)]
squared_numbers = [square(x) for x in range(10) if valid(x)]
# print(squared_numbers)

pairs = [('a', 1), ('b', 2), ('c', 3)]
# print(pairs)
my_dict = {k: v for k, v in pairs}
# print(my_dict)

numbers = [1, 2, 2, 3, 3, 3, 4, 4, 4, 4]
unique_squares = {x for x in numbers}
unique_squares = {x**2 for x in numbers}
# print(unique_squares)

sum_of_squares = sum(x**2 for x in range(100000))
print(sum_of_squares)
