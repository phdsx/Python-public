import sympy

x = sympy.symbols("x")
y = sympy.symbols("y")

fx=x*x+y*y
a=fx.evalf(subs={x:3,y:4})

print(a)