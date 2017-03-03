n1 = n = int(input())
m = [[0 for j in range(n)] for i in range(n)]
k = 0
l = 0
s = n - 1
t = 0
while k < n1 ** 2 - 1:
    for i in range(2):
        for j in range(0, n - 1):          # Заполняем верхнюю грань
            if i == 0:
                k += 1
                l = t
                c = j + t
                m[l][c] = k
            else:          # Заполняем правую грань
                k += 1
                l = j + t
                c = n - 1 + t
                m[l][c] = k
    for i in range(2):
        for j in range(1, n):          # Заполняем нижнюю грань
            if i == 0:
                k += 1
                l = n - 1 + t
                c = n - j + t
                m[l][c] = k
            else:          # Заполняем левую грань
                k += 1
                l = n - j + t
                c = t
                m[l][c] = k
    t += 1          # Заполняем верхнюю грань
    n -= 2
if n1 % 2 == 1:
    n = (n1 - 1) // 2
    m[n][n] = k + 1
for i in range(n1):
    for j in range(n1):
        print(m[i][j], end=' ')
    print()
