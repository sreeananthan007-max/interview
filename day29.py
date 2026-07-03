s="hello world"
print(s.capitalize())

s="HELLO"
print(s.casefold())

s="python"
print(s.center(12,"-"))

s="banana"
print(s.count("a"))

s="hello"
print(s.encode())

s="python.py"
print(s.endswith(".py"))

s="hello\tworld"
print(s.expandtabs(4))

s="hello world"
print(s.find("world"))

name="sree"
print("my name is {}".format(name))

d={"name":"sree"}
print("my name is {name}".format_map(d))

s="hello world"
print(s.index("world"))

s="abc123"
print(s.isalnum())

s="python"
print(s.isalpha())

s="hello"
print(s.isascii())

s="123"
print(s.isdecimal())

s="123"
print(s.isdigit())

s="my_var"
print(s.isidentifier())

s="python"
print(s.islower())

s="123"
print(s.isnumeric())

s="hello"
print(s.isprintable())

s="   "
print(s.isspace())

s="Hello World"
print(s.istitle())

s="HELLO"
print(s.isupper())

a=["i","love","python"]
print(" ".join(a))

s="python"
print(s.ljust(10,"-"))

s="HELLO"
print(s.lower())

s="   hello"
print(s.lstrip())

table=str.maketrans("a","x")
print(table)

s="apple-banana"
print(s.partition("-"))

s="i like java"
print(s.replace("java","python"))

s="banana"
print(s.rfind("a"))

s="banana"
print(s.rindex("a"))

s="python"
print(s.rjust(10,"-"))

s="apple-banana"
print(s.rpartition("-"))

s="a,b,c,d"
print(s.rsplit(",",2))

s="hello   "
print(s.rstrip())

s="python is easy"
print(s.split())

s="one\ntwo\nthree"
print(s.splitlines())

s="hello world"
print(s.startswith("hello"))

s="  hello  "
print(s.strip())

s="Hello World"
print(s.swapcase())

s="python programming"
print(s.title())

table=str.maketrans("a","x")
s="apple"
print(s.translate(table))

s="python"
print(s.upper())

s="25"
print(s.zfill(5))