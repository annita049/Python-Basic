# ... Lists are ...

# Ordered (Iterable)
# Changeable
# Allow Duplicate values

emojis = ["like","moonFace","chick"]

print(emojis[0])

# List is a changeable entity

emojis[0]="kalaHaat"

print(emojis[0]*5)

emojis.append("monkey")
emojis.insert(2,"angry")

print(emojis[0:5])

for item in emojis:
    print(item)


fruits = ["apple","orange","cherry"]
x = fruits.copy()
print(x)
