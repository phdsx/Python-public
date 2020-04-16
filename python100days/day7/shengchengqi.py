import sys
f3=[x**2 for x in range(1000)]
print(sys.getsizeof(f3))
for val in f3:
    print(val)