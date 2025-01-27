weight =float (input("what is your weight? ") )
unit = input("K(g) or L(lb)? ")
if unit.upper() == "K":
    converted = weight * 0.45
    print("weight in Kgs: " + str (converted) )
else:
    converted = weight / 0.45
    print("weight in Lbs: " + str (converted) )
