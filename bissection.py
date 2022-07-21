import timeit
start = timeit.timeit()

from math import fabs
a = float(input('Lower limit: '))
b = float(input('Upper limit: '))
e = float(input('Accuracy: '))


def h(x):
    h = (x**3) - 3.5*x
    return h


k = 0

while True:
    m = (a+b)/2
    if fabs(h(m)) < e:
        print()
        print('Abcissa value in the interception =', m)
        print('Number of interations =', k)
        break
    else:
        k += 1
        if h(m)*h(a) < 0:
            b = m
        else:
            a = m

print()
end = timeit.timeit()
print('Execution time:',end - start)