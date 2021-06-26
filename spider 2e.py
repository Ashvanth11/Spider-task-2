n = int(input())
q = int(input())

a = [0 for i in range(n)]

for i in range(q):
    l, r, val = map(int, input().split())
    a[l-1] += val
    if (r != n):
        a[r] -= val

for i in range(1, n):
    a[i] += a[i - 1]

for i in range(n):
    a[i] += i+1

print(max(a))

