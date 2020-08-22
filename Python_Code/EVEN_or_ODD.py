print("---------------------")
print("     Even or Odd")
print("---------------------")
print()
print("Enter any number other than 0 and I will tell you if it's ODD or EVEN to quit just enter 0")
print()

# userNumTxt = input("What number would you like to find out if it's EVEN or ODD? ")
# userNum = int(userNumTxt)
# umber = userNum % 2
# if number == 0:
#   print("Your number is even")
# else:
#   print("Your number is odd")
i = 0
while i == 0:
    print()
    userNumTxt = input("What number would you like to find out if it's EVEN or ODD? ")
    userNum = int(userNumTxt)
    if userNum == 0:
        i += 1
    remainder = userNum % 2
    if remainder == 0:
        print(f"{userNum} is EVEN.")
    elif remainder != 0:
        print(f"{userNum} is ODD.")
print("Goodbye")

# <K2>
