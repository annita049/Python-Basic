def custom_sort(list):
    return (list[0]+list[1])  # based on inner list sum (increasing order)

def cus(x):
    return x[1]  # based on the second element of each tuple (increasing order)


list2 = [[3,0],[1,2],[4,6],[2,0],[1,1],[4,2]]  # list of lists
list2.sort(key=custom_sort)     # sorted in the increasing order of inner list sum

print(list2)

list3 = [(1,'a'),(2,'c'),(1,'b'),(3,'a')]   # List of tuples
list3.sort(key=cus)
list3.pop()
