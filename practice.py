#Problem 1

print("Hi! If you are stupid and can't multp 3 number this program will help you\n")
input("Press any key to start...\n")

firstNumber = int(input("Please enter the first number: "))
secondNumber = int(input("Please enter the second number: "))
thirdNumber = int(input("Please enter the third number: "))

print("\nThe multiplication of all 3 numbers is {}\n".format(firstNumber*secondNumber*thirdNumber))

input("Press any key for next program...\n")

#Problem 2

print("Good to see u again! This program is more useful than previous one.\n")
input("Press any key to know you BMI...\n")

weight = int(input("Please, enter your weight: "))
height = float(input("\nAnd now ur height(m): "))

print("Your IBM is {:.2f}".format(weight / (height ** 2)))

input("Press any key for next program...\n")

#Problem 3

print("\nThis is something different...")
print("\n\n*Please reset ur km/gasoline system before calculation for more accurate result*\n")
input("Press any key to start...\n")

gasolinePrice = 1.2
gasolinePerKm = int(input("Gasoline ur vehicle use per km: "))
km = int(input("How many km google map shows to ur destination(?): "))

print("You will have to pay ${:.2f} to gasoline".format((km * gasolinePerKm)/gasolinePrice))

input("\nPress any key for next program...\n")

#Problem 4

print("\n*It is also not a useful program*\n\n")

name = input("Enter ur name: ")
surname = input("Enter ur surname: ")
number = int(input("Enter ur telephone number "))

userInfo = [name, surname, number]

print("\nRequested user info....\n")

print("{}\n{}\n{}\n".format(userInfo[0], userInfo[1], userInfo[2]))
input("\nPress any key for next program...\n")

#Problem 5

print("\n\nReverse 2 numbers\n")

temp = 0

num1 = int(input("Please enter 1st number: "))
num2 = int(input("Please enter 2nd number: "))

temp = num1
num1 = num2
num2 = temp

print("1st number:{}\t2nd number:{}\n".format(num1, num2))
input("\nPress any key for next program...\n")

#Problem 6

print("\n\n*Pythagorean theorem*\n")

a = int(input("Enter 1st side: "))
b = int(input("Enter 2st side: "))

print("The hypotenuse is: {}".format((a ** 2 + b ** 2) ** 0.5))










