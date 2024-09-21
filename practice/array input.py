# create an array space

# array = input("enter elements separated by space: ").split()

''' for elements in array:
    print(elements) '''

# creating array with n elements

array = []
n = int (input("Enter the number of array elements: "))
for i in range(n):
    array.append (int(input()))

print("The last element of the array is: ", array[n-1])