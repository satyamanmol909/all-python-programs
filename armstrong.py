number = input("Enter the number to check if it is an Armstrong number: ")
arm = 1
armstrong = 0

for char in number:
    n = int(char)
    arm = (n ** 3)
    armstrong += arm

if int(number) == armstrong:
    print(f"{number} is an Armstrong number")
else:
    print(f"{number} is not an Armstrong number")
