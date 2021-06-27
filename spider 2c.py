modulo = 1000000007

def fibonacci(n):
    a = 0
    b = 1

    if n == 1:
        return b
    else:
        for i in range(1, n):
            c = a + b
            a = b
            b = c
        return b

n, m = map(int, input().split())

b = [-1]
for i in range(m):
    bstep = int(input())
    b.append(bstep)

b.append(n + 1)

totways = 1
for i in range(len(b) - 1):
    ways = 0
    d = b[i + 1] - b[i] - 1
    if d == 0:
        totways = 0
        break
    else:
        ways = fibonacci(d) % modulo

    totways *= ways
    totways = totways % modulo
print(totways)


