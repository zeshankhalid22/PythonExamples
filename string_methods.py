s = "hello"
print(len(s))

# object into string
num = 32
num2str = str(num)
print(num2str)

s = s.capitalize()
print(s)

s = s.upper()
print(s)

s = s.lower()
print(s)

s = " hell o "
s = s.strip() # remove leading and trailing spaces
print(s)

s = "a1sda8s"
print(s.startswith("a1s"))
print(s.endswith("8s"))

print(s.find("a1"))

print(s.replace("a8s","k"))
