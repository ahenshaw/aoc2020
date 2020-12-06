from time import perf_counter

a = list(range(1000000))

start = perf_counter()
for i in range(len(a)):
    b = 2 * a[i]
print(perf_counter()-start)


start = perf_counter()
for i in a:
    b = 2 * i
print(perf_counter()-start)

