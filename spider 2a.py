def prefix_length(a):
    n = len(a)
    x = 0
    ans = 0
    if a[0] != '>':
      for i in range(n):
         if a[i] == '<':
            x += 1
         else:
            x -= 1

         if x == 0:
            ans = i + 1

         if x < 0:
            break

    print(ans)


t = int(input())
s = []
for i in range(t):
    string = input()
    s.append(string.strip())

for i in range(t):
    prefix_length(s[i])

