# Loops
n = int(input("How many times? "))

for i in range (1, n, 2):
    print("hello ",i)

# Loops for List
    
list1 = ["date","guava","apple","pineapple","banana"]

for item in list1:
    if item == "apple":
        continue
    print(item, end=' ')