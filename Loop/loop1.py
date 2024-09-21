# ------ List of lists -------
    
n_lists = [["A","B","C"],[5,6,10],["Levi","Hash","Semicolon"]]

for item in n_lists:
    for i in item:
        print(i , end =', ')
    print()

# ------ While Loops --------

i = 0
while (i < 6):
    print(i)
    i+= 1
else:
    print("i is No longer less than 6!")


alpha = ["Tokyo","Kyoto","Osaka"]
city = ["Berlin","Munich","Hamburg"]

for x in alpha:
    for y in city:
        print(x + ", " + y)
    
for i in [0,1,2,3]:
    pass     # if the loop doesn't have a body "pass" keyword is to avoid error
