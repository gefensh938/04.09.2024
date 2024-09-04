# 1
# START
x: int = int(input('Enter first number: '))
y: int = int(input('Enter second number: '))
z: int = int(input('Enter third number: '))

print('sum: ', x + y + z)
print('product: ', x * y * z)
# STOP

# # 2
# START
f1: float = float(input('Enter first number: '))
f2: float = float(input('Enter second number: '))

diff: float = f1 - f2

print('difference is ', diff)
# STOP

# 3
# START
str1: str = input('Enter first string: ')
str2: str = input('Enter second string: ')

print('*' + str1 + '*' + str2 + '*')
print('-' + str1 + '-' + str2 + '-')

# STOP

# 4
# START
a: int = int(input('Enter a: '))
b: int = int(input('Enter b: '))

if a > b:
    #YES
    print(a)
else:
    #NO
    print(b)

print('goodbye...')
# STOP

# 5
# START
num1: int = int(input('Enter num1: '))
num2: int = int(input('Enter num2: '))

#   54    99
if num1 > num2:
    #YES
    print(num2) # 54
    print(num1) # 99
else:
    #NO
    print(num1)
    print(num2)

print('goodbye...')
# STOP

