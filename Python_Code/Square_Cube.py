print("------------------------------------")
print("     Square and Cube any number")
print("------------------------------------")
print()
numTxt = input("What number would you like to square? ")
num = int(numTxt)
square = num * num
cube = num * num * num
print(f"Okay the square of {num} = {square}")
yesno = input(f"Would you also like to know the Cube of {num}? ")
if yesno != "no":
    print(f"Okay the cube of {num} = {cube}")
else:
    print("Okay have a nice day.")

# <K2>
