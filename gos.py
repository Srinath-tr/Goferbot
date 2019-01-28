def fun1():
    a=1
    b=2
    c=3
    return a,b,c
def fun2():
    res = fun1()
    x=res[0]
    y=res[1]
    z=res[2]
    print(x,y,z)

fun2()
