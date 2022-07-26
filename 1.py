def mul3():
    a = 1
    s = 0
    ch = 0
    while ch<1000:
        a+=1
        ch = a*3
        s +=ch
    return s
def mul5():
    a = 1
    s = 0
    ch = 0
    while ch<1000:
        a+=1
        ch = a*5
        s +=ch
    return s
print(mul3() + mul5())
