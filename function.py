# def greet():
#     print("hi wellcome")

# greet()

# def greet(name):
#     print(f"Wellcome {name}")

# greet('ali')
# greet('bilal')

# def add(a,b):
#     print(a + b)

# add(5,6)

# def sub(a,b):
#     return a - b

# print(sub(9,7))

# def check_number(a):
#     if a % 2 == 0:
#         print("Even Number")
#     else:
#         print("odd number")

# check_number(7)

# def square(num):
#     return num * num

# result = square(6)
# print(result)

# square = lambda x : x*x

# print(square(5))

numbers = [2,5,6,9,12]
# result = map(lambda x : x*2, numbers)
# print(list(result))
result = filter(lambda x: x %2==0, numbers)
print(list(result))