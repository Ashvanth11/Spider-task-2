n = int(input())
q = int(input())

a = [i for i in range(1, n + 1)]

for i in range(q):
    l, r, val = map(int, input().split())

    for x in range(l, r + 1):
        a[x - 1] += val

print(max(a))