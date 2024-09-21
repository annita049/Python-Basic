list = []

list.append(['bonu','cat','chui'])
list.append([1,3,6])

list2 = ['cairo','warsaw','cardiff']

(a, b, c) = list2   #extracting list values into variables (unpacking)
print(b)

# insert() -> also used to insert a list to a specific position
list.insert(1, ['A','B'])   
list.insert(0, list2)

print(list)
list.pop()
print(list)
list.pop()
print(list)

