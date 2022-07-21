from math import fabs
import timeit
start = timeit.timeit()

a = float(input('Upper limit: '))
b = float(input('Lower limit: '))
e = float(input('Accuracy: '))


def h(x):
    h = (x**3) - 3.5*x
    return h


k = 0

while True:
    m = (a*h(b) - b*h(a)) / (h(b) - h(a))
    if fabs(h(m)) < e:
        print()
        print('Abcissa value in the interception =', m)
        print('Number of iterations =', k)
        break
    else:
        k += 1
        if h(m)*h(a) < 0:
            b = m
        else:
            a = m

end = timeit.timeit()
print('Execution time:', end - start)
