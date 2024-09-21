fruits = ("apple","banana","cherry")  # assigning values to tuple (packing)

# extracting tuple values back into variables (unpacking)
a, b, c = fruits 
(i,j,_) = fruits    # for variables less than the list items

print(b)
print(i)


fruits2 = ("apple","banana","cherry","raspberry","strawberry")
green, yellow, *red = fruits2
print(red)

letters = ["A","B","C","D","E"]     # Lists can also be unpacked
x,y,*z = input().split()
print(type(z))


