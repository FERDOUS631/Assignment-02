
a, b = 0, 1
series_length = int(input())

print(a, b,end=' ')
for i in range(series_length):
    c = a + b
    a = b
    b = c
    print(c, end=' ')
    