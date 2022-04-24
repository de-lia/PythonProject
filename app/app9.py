weight = int(input("Weight: "))
input("(L)bs or (K)g: ")
if unit.upper() == "L":
   converted = weight * 0.45
   print(f"You are {converted} kilos.")
else:
    converted = weight / 0.45
    print(f"You are {converted} pounds.")
