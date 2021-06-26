modulo = 1000000007
def fibonacci(a):
    if a == 1 or a == 2:
        return 1

    else:
        return fibonacci(a - 1) + fibonacci(a - 2)

n, m = map(int, input().split())
b = []
b.append(-1)
for i in range(m):
    bstep = int(input())
    b.append(bstep)
b.append(n + 1)

for i in range(len(b) - 1):
    ways = 0
    totways = 1
    d = b[i + 1] - b[i] - 1
    if d == 0:
        totways = 0
        break
    else:
        ways = fibonacci(d)

    ways = ways % modulo
    totways *= ways

print(totways)
