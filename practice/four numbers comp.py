array = []

print("Enter 4 numbers (hit enter to enter)")

for i in range(4):
    array.append (int(input()))

print("The Largest number is: ")

if (array[0]>array[1] and array[0]>array[2] and array[0]>array[3]):
    print(array[0])
elif (array[1]>array[0] and array[1]>array[2] and array[1]>array[3]):
    print(array[1])
elif (array[2]>array[0] and array[2]>array[1] and array[2]>array[3]):
    print(array[2])
elif (array[3]>array[0] and array[3]>array[1] and array[3]>array[2]):
    print(array[3])