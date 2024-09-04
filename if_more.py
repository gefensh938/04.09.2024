
# we require to be bigger than 18 years old
# and more than 100_000 in balance

age: int = int(input("what's your age?"))
balance: int = int(input("what's your balance?"))

# short circuit
#   _____   and  _____
#   False ... not check second
# True and True =>   True
# True and False =>  False
# False and True =>  False
# False and False => False
if age > 18 and balance > 100_000:
    # YES
    print('you are qualified for the program')
else:
    # NO
    print('you are NOT qualified for the program')

# True or True   => True
# True or False  => True
# False or True  => True
# False or False => False
if age <= 18 or balance <= 100_000:
    print('you are NOT qualified for the program')
else:
    print('you are qualified for the program')

# if the age is bigger than 18 and the balance is not smaller equal 100_000
#if age > 18 and balance > 100_000:
if age > 18 and not balance <= 100_000:
    # YES
    print('you are qualified for the program')
else:
    # NO
    print('you are NOT qualified for the program')

x: int = 0
y: int = 200

# check if x is not zero and y bigger than 100
#if not x == 0 and y > 100:
#if x != 0 and y > 100:


