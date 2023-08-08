# create a hello world function using fstrings
def hello(name):
    return f"Hello {name}!"


if __name__ == "__main__":
    print(hello("world"))
    print(hello("Corey"))
    print(hello("Python"))
