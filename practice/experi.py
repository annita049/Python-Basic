a = int(4)
b = int(3)
c = complex("7")
d = 4 + 2j

print(a)
print(b)
print(not False)
print(not (a>b))

x,y = "2",4
txt = "@"

print(int(x)*txt*y)
print((x+ txt)*y)  # 2@ * 3 

print(c+d)

m , n = -50 , 4
print(m//n, m/n)
print(m%n) 

print(type("python")==int)  #False
print(bool("")) # Null string  # False
print(bool(3.5))   # Always True

x = 20
x >>= 2
print(x)