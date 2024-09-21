if __name__ == '__main__':
    # x,y,z = map(int,input().split())
   # ks = [x,y,z]
   # j = set((x,y,z))
   # print(sum(ks))   
   # print(sum((x,y,z)))
    str ='abcdefghijklmnopqrstuvwxyz'
    ka = ['-'.join(str[1:6])]
    print(ka)

    fruit1 = {"apple","banana","cherry"}
    dic = {'a':'apple', 'b':'ball', 'c':'cat'}
    fruit1.update(dic)
    print(fruit1)

    # sum function cant take more than one value except for an iterable
    # like list, tuple or set