# ... Tuples are ...

# Ordered (Iterable)
# Unchangeable
# Allow Duplicate values


cars = ("volvo", "audi", "BMW", 1,2,3) # tuples
flowers = tuple(["daffodil",tuple(["rose","tulip"]),"dandelion"])  # list to tuples

print(cars)
print(flowers)

fruits = ("apple","banana","cherry")  # assigning values to tuple (packing)

# extracting tuple values back into variables (unpacking)
(_,yellow, red) = fruits 

print(_); print(yellow)

vit_c = ("orange",)  # Single element tuples are written with a " , " at the end

fruits+= vit_c
print(fruits)
