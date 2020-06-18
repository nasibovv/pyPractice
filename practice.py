""" # Problem 1

print("Hi! If you are stupid and can't multp 3 number this program will help you\n")
input("Press any key to start...\n")

firstNumber = int(input("Please enter the first number: "))
secondNumber = int(input("Please enter the second number: "))
thirdNumber = int(input("Please enter the third number: "))

print("\nThe multiplication of all 3 numbers is {}\n".format(firstNumber*secondNumber*thirdNumber))

input("Press any key for next program...\n")
"""
# Problem 2

print("\nGood to see u again! This program is more useful than previous one.")
input("Press any key to know you BMI...\n")

weight = int(input("Please, enter your weight: "))
height = float(input("And now ur height(m): "))
ibm = weight / (height ** 2)

if ibm < 18.5:
    print("\nUnderweight")
elif 18.5 <= ibm < 25:
    print("\nNormal weight")
elif 25 <= ibm < 30:
    print("\nOverweight")
else:
    print("\nObesity")

input("Press any key for next program...\n")
"""
# Problem 3

print("\nThis is something different...")
print("\n\n*Please reset ur km/gasoline system before calculation for more accurate result*\n")
input("Press any key to start...\n")

gasolinePrice = 1.2
gasolinePerKm = int(input("Gasoline ur vehicle use per km: "))
km = int(input("How many km google map shows to ur destination(?): "))

print("You will have to pay ${:.2f} to gasoline".format((km * gasolinePerKm)/gasolinePrice))

input("\nPress any key for next program...\n")

# Problem 4

print("\n*It is also not a useful program*\n\n")

name = input("Enter ur name: ")
surname = input("Enter ur surname: ")
number = int(input("Enter ur telephone number "))

userInfo = [name, surname, number]

print("\nRequested user info....\n")

print("{}\n{}\n{}\n".format(userInfo[0], userInfo[1], userInfo[2]))
input("\nPress any key for next program...\n")

# Problem 5

print("\n\nReverse 2 numbers\n")

temp = 0

num1 = int(input("Please enter 1st number: "))
num2 = int(input("Please enter 2nd number: "))

temp = num1
num1 = num2
num2 = temp

print("1st number:{}\t2nd number:{}\n".format(num1, num2))
input("\nPress any key for next program...\n")

# Problem 6

print("\n\n*Pythagorean theorem*\n")

a = int(input("Enter 1st side: "))
b = int(input("Enter 2st side: "))

print("The hypotenuse is: {}".format((a ** 2 + b ** 2) ** 0.5))
"""

# Problem 7

testNum1 = int(input("Enter the 1st number: "))
testNum2 = int(input("Enter the 2nd number: "))

if testNum1 > testNum2:
    print("{} is greater than {}.".format(testNum1, testNum2))
elif testNum2 > testNum1:
    print("{} is greater than {}.".format(testNum2, testNum1))
else:
    print("Numbers are equal.")

input("\nPress any key for next program...\n")

# Problem 8

print("""***************\nFinal Grade Calculator\n***************""")
mid1 = float(input("Grade of 1st midterm: "))
mid2 = float(input("Grade of 2nd midterm: "))
finalExam = float(input("Grade of final exam: "))

finalGrade = (0.3 * mid1) + (0.3 * mid2) + (0.4 * finalExam)

if finalGrade >= 90:
    print("Final Grade: AA")
elif finalGrade >= 85:
    print("Final Grade: BA")
elif finalGrade >= 80:
    print("Final Grade: BB")
elif finalGrade >= 75:
    print("Final Grade: CB")
elif finalGrade >= 70:
    print("Final Grade: CC")
elif finalGrade >= 65:
    print("Final Grade: DC")
elif finalGrade >= 60:
    print("Final Grade: DD")
elif finalGrade >= 55:
    print("Final Grade: FD")
else:
    print("Final Grade: FF")

input("\nPress any key for next program...\n")

# Problem 9

print("""***************\nGeometric Shape Calculation\n***************""")
choice = input("Do you want to find 'triangle' or 'quadrilateral': ")

if choice == "triangle":
    sideOne = float(input("Enter 1st side of triangle: "))
    sideTwo = float(input("Enter 2nd side of triangle: "))
    sideThree = float(input("Enter 3rd side of triangle: "))

    if sideOne == sideTwo and sideTwo == sideThree:
        print("This triangle is Equilateral triangle.")
    elif (sideOne == sideTwo and sideTwo != sideThree) or (sideOne == sideThree and sideThree != sideTwo) or (sideTwo == sideThree and sideTwo != sideOne):
        print("This triangle is Isosceles triangle.")
    elif (abs(sideTwo - sideThree) < sideOne < sideTwo + sideThree) or (abs(sideOne - sideThree) < sideTwo < sideOne + sideThree) or (abs(sideOne - sideTwo) < sideThree < sideOne + sideTwo):
        print("It is an ordinary triangle.")
    else:
        print("This is not a triangle.")

elif choice == "quadrilateral":
    sideOne = float(input("Enter 1st side of quadrilateral: "))
    sideTwo = float(input("Enter 2nd side of quadrilateral: "))
    sideThree = float(input("Enter 3rd side of quadrilateral: "))
    sidePlus = float(input("Enter 4th side of quadrilateral: "))

    if sideOne == sideTwo == sideThree == sidePlus:
        print("This is a square.")
    elif (sideOne == sideThree) and (sideTwo == sidePlus):
        print("This is a rectangle.")
    else:
        print("This is an ordinary quadrilateral.")









