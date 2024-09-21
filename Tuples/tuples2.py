# python tuples are unchangeable
# so they are converted into lists first

x = ("berlin","dublin","warsaw")
y = list(x)    # tuple converted into list to change the elements

y[1:] = ["seoul","beijing","colombo"]  # these elements after the element 0 
y.append("tokyo")
y.remove("colombo")

x = tuple(y)
print(x)

# del x   # the entire tuple is deleted
# print(x)  # throws compilation error (the tuple is deleted) 