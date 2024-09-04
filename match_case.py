
# input a number from the user
# if number is 1 ==> print('Sunday')
#              2 ==> print('Monday')
#              ..
#              7 ==> print('Saturday')
# otherwise print('invalid day number')

day: int = int(input('enter a day number:'))

# if day is 1:
match day:
    # if day == 1
    case 1:
        print("Sunday")
    # elf day == 2
    case 2:
        print("Monday")
    # elf day == 3
    case 3:
        print("Tuesday")
    case 4:
        print("Wednesday")
    case 5:
        print("Thursday")
    case 6:
        print("Friday")
    case 7:
        print("Saturday")
    # else
    case _:
        print('invalid day')
# input age from user
#  0 <= x <= 10
#  x >=0 or x <= 10
#  -1
# age: 10 11 12  -- print("young")
#      13 14 15  -- print("teenager")
#      16 17 18  -- print("almost adult")
#      19 20     -- print("adult")
#      otherwise -- print("not in range")

