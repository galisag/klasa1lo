print("trojkat matematyczny")

a = float(input("1. bok: "))
b = float(input("2. bok: "))
c = float(input("3. bok: "))

if a == b == c:
    print("trojkat rownoboczny")
if a + b > c:
    if a + c > b:
        if b + c > a:
            print("mozna zbudowac trojkat")
        else:
            print("nie mozna zbudowac trojkata")
    else:
        print("nie mozna zbudowac trojkata")
else:
    print("nie mozna zbudowac trojkata")
