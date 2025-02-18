"""
Text = str
numeric = int, float, complex
sequence = list, tuple, range
map(key-value) = dict
colection = set, fronzenset
boolean = bool
binary = bytes, bytearray, memoryview

dir(returns list of methods that can be exected by the object)

help(get doc and information about python objects)
"""

print(10340 + 2176)
print(2.5 + 0.5)
print(True)
print(False)

#variable
name = "Dracula"

#const
BRAZILIAN_STATES = ["SP", "RJ", "SC", "RS"]

value = 10
print(value)

value = float(value) # (value / 2) 
print(value)

value = int(value) # (value // 2) 
print(value)

print(int(10.123123123))
print(float(10))

print(type(str(10.10)))

username = input("Enter your name: ")
print(f"Hi, {username}! ")

quote = ("Do you know that happiness depends on us")

print({username}, {quote}, end="?\n ")
print(username, quote, sep="#")

