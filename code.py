# Small test script

name = "Zackery"
grades = [67, 100, 87, 56]
my_int = 82307
my_float = 14.5
my_complex = complex(0, 14)
my_string_double = "Foo"
my_string_single = 'Baz'
my_string_index = "esrever morf olleH"[::-1]

def my_func(a: str, b: float, c: int=0):
    if c == 0:
        print(":(")
        return
    print(a, b, c)

my_func(":)", 64.0)
my_func(":)", 64.0, 0.1)
print("Hello, World!")
print("Foo", end="")
print("Bar")

