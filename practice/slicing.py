# slicing in strings
a = "hello world"
print(type(a[:4]))
print(a)

b = ['a','b','c','d','e','f','g']  # slicing in a list
print(type(b[:]))
print(b[0:7:3])  # including steps

# through slice() method
x = slice(0,7,3)
print(x)
print(type(x))  # <class 'slice'>
print(b[x])

print(b.count('a'))