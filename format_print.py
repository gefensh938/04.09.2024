# first_name: str = input('whats your first name?')
# last_name: str = input('whats your last name?')
# age: int = int(input('whats your age?'))
#
# # avi cohen
# # "Your name is [last_name], [first_name] your age is [age]."
#
# print( "Your name is", last_name + "," + " " + first_name + " your age is", age, ".")
# print(f"Your name is {last_name}, {first_name} your age is {age}.")

pi: float = 3.14159
print(f"Pi: {pi}")
print(f"Pi: {pi:.2f}")
name1: str = "Alice"
#             12345
age1: int = 30
name2: str = "Laura Croft"
#             12345678901
age2: int = 31

print(f"Name: {name1:<20} {age1}")
print(f"Name: {name1:>20} {age1}")
print(f"Name: {name1:^20} {age1}")
print(f"Name: {name2:^20} {age2}")

prc: float = 0.5
print(f"percentage: {prc:%}")
print(f"percentage: {prc * 100:.2f}%")
