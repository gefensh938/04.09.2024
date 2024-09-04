# input age from user
#  0 <= x <= 10
#  x >=0 or x <= 10
#  -1
# age: 10 11 12  -- print("young")
#      13 14 15  -- print("teenager")
#      16 17 18  -- print("almost adult")
#      19 20     -- print("adult")
#      otherwise -- print("not in range")

age: int = int(input('Whats your age?'))

if age == 10 or age == 11 or age == 12:
    print("young")
elif age == 13 or age == 14 or age == 15:
    print("teenager")
elif age == 16 or age == 17 or age == 18:
    print("almost adult")
elif age == 19 or age == 20:
    print("adult")
else:
    print("not in range")

# if age >= 10 and age <= 12:
if 10 <= age <= 12:
    print("young")
elif 13 <= age <= 15:
    print("teenager")
elif 16 <= age <= 18:
    print("almost adult")
elif age == 19 or age == 20:
    print("adult")
else:
    print("not in range")

# if age == 10 or age == 20 or age == 25:
# if age in (10, 20, 25)

match age:
    case 10 | 11 | 12:
        print("young")
    case 13 | 14 | 15:
        print("teenager")
    case 16 | 17 | 18:
        print("almost adult")
    case 19 | 20:
        print("adult")
    case _:
        print("not in range")
