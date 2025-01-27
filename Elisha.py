from socketserver import ThreadingTCPServer

from Tools.scripts.md5sum import printsum
birth_year = input("Enter your birth year: ")
age = 2025 - int(birth_year)
print(age)

height = 5.65
length = 8
area = float(height) * int(length)
print(area)

height = input("what is the height of the fence? ")
length = input("what is the length of the fence? ")
area = (f'{float(height) * float(length)}cm')
print(area)


name = input("Name ")

if len(name) < 3:
    print("Name characters is too short")
elif len(name) > 30:
    print("Name must not be more than 50 characters")
else:
    print("Continue")
