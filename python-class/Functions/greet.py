def greet():
    print("Hi there")
    print(("How are you ?"))

greet()

def greet(first_name, last_name):
    print("Hi", first_name, last_name)
    print(("How are you ?"))

greet("Amit", "Kulkarni")

def save_user(**user): # multiple arguments
    print(user["name"])

save_user(id=1, name="amit", age=32)
# Returns Dictionary

