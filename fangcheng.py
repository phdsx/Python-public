import math
def quadratic(a,b,c):
    a = float(a)
    b = float(b)
    c = float(c)
    deta=b*b-4*a*c
    if deta<0:
        return('无解')
    else:
        x1=(-b+math.sqrt(deta))/(2*a)
        x2=(-b-math.sqrt(deta))/(2*a)
        return x1,x2
