# START
# input a, b, c
a: int = int(input('a:'))
b: int = int(input('b:'))
c: int = int(input('c:'))

if a > b and a > c:
    print(a)
elif b > c:
    print(b)
else:
    print(c)
# STOP