print("trojkat matematyczny")

a = float(input("1. bok: "))
b = float(input("2. bok: "))
c = float(input("3. bok: "))

if a + b > c and a + c > b and b + c > a:
    if a == b == c:
        print("mozna zbudowac trojkat rownoboczny")
    elif a == b or a == c or b == c:
        print("mozna zbudowac trojkat rownoramienny")
    elif a**2 + b**2 == c**2 or a**2 + c**2 == b**2 or b**2 + c**2 == a**2:
        print("mozna zbudowac trojkat prostokatny")
    else:
        print("mozna zbudowac trojkat")
else:
    print("nie mozna zbudowac trojkata")