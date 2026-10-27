# def decorator(func):
#     def wrapper():
#         print("Somthing After calling the function.")
#         func()
#         print("Somthing Before calling the function")
#     return wrapper

# @decorator
# def say_hello():
#     print("Hello World!")

# say_hello()

# import re


# def smart_divide(func):
#     def wrapper(*args, **kwargs):
#         if args[0] > 1 and args[1]==0:
#             print("Error: can not divide by 0!")
#             return None
#         return func(*args, **kwargs)
#     return wrapper


# @smart_divide
# def divide(a,b):
#     return a / b


# a = int(input("Enter first Number: "))
# b = int(input("Enter second Number: "))
# print(divide(a,b))

user = {
    "is_auth":False,
    "user": "Bilal"
}

def login_required(func):
    def wrapper(*args, **kwargs):
        if not user["is_auth"]:
            print("Access denied: first you are logging then view the dashboard!")
            return None
        return func(*args, **kwargs)
    return wrapper
@login_required
def dashboard():
    print(f"Welcome {user['user']}")

dashboard()

user["is_auth"]=True
user["user"]="ahmad"
print("\n... Attempt to Login ...\n")
dashboard()