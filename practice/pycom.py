

set_a = set()
set_b = set()

for i in range(n):
    x = int(input())
    if (x<= k): set_a.add(x)

for i in range(m):
    x = int(input())
    if (x<= k): set_b.add(x)

s = set_a.union(set_b)

flag = False

if len(set_a) >= k/2 and len(set_b) >= k/2 and len(s) == k:
    flag = True

if flag:
    print("YES")
else:
    print("NO")

