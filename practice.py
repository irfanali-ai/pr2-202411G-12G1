# def my_decorator(func):
#     def wrapper():
#         print("Somthing After function called.")
#         func()
#         print("Somthing Before function called")
#     return wrapper


# @my_decorator
# def greeting():
#     print("Hello World!")



# greeting()

import functools


def smart_divide(func):
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        print(f"Attempting to divide numbers: {args}")
        if len(args) >1 and args[1]==0:
            print("Error: cannot divide by 0")
            return None
        return func(*args, **kwargs)
    return wrapper

        
@smart_divide
def divide(a,b):
    return a/b

print("Result:",divide(30,4))
print("-" * 10)
print("Result: ", divide(30,0))

current_user = {
    "authentic":False,
    "user":"Admin"
}
def login_required(func):
    def wrapper(*args, **kwargs):
        if not current_user["authentic"]:
            print("access denied: You must login to view dashboard")
            return None
        
        return func(*args, **kwargs)
    return wrapper

is_login = True

@login_required
def dashboard():
    print("Welcome Admin!")

dashboard()

print("\n... logging User In....\n")
current_user["authentic"] = True
current_user["user"] = "Irfan"

dashboard()


