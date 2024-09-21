# list methods
list = ["annita","apurbo","python"]
list.append("django")  #changes in the list
list.sort()   # ascending order , changes in the list
list.sort (reverse = True)   # descending order , changes in the list

print(list)
print(list [-3:-1])   # slicing in list

list.reverse()
list.insert(2,"ml")   # inserts element at a position specified
print(list)

list1 = [3,2,1,5]
list1.remove(1)  # removes an element specified
print(list1)
list1.pop(1)    # removes the element of a position specified
print(list1)

print("python"[::-2]) # slicing with steps 
