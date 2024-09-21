# ----- If Else -------

while (True) :

    marks = int(input("Enter your marks "))

    if (marks < 0):
        print("Marks can't be negative! ")
        break

    if marks >= 80 and marks <= 100:
        print("A+")
    elif marks >= 75  and marks < 80:
        print("A")
    elif marks >= 70  and marks < 75:
        print("A-")
    elif marks >= 65  and marks < 70:
        print("B+")
    elif marks >= 60  and marks < 65:
        print("B")
    else:
        print("Passed")
