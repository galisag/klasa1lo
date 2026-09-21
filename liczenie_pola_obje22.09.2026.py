import math


PI = math.pi
pier = math.sqrt #pierwiastek

print("Bryly - 1 | Plaskie - 2")
inp = input("wpisz: ").lower().strip()

if inp == "1":
    print("pole powierzchni bryl - 1 | objetosc bryl - 2")
    inp = input("wpisz: ").lower().strip()
    
    if inp == "1":
        print("pole powierzchni Szescianu - 1 | pole powierzchni Prostopadloscianu - 2 | pole powierzchni Graniastoslupa - 3 | pole powierzchni Ostroslupa - 4 | pole powierzchni Walca - 5 | pole powierzchni Stozka - 6 | pole powierzchni Kuli - 7")
        inp = input("wpisz: ").lower().strip()
        
        if inp == "1":
            a = float(input("a = "))
            print(f"pole powierzchni Szescianu o boku {a} = {6 * a**2}")
        elif inp == "2":
            a = float(input("a = "))
            b = float(input("b = "))
            c = float(input("c = "))
            print(f"pole powierzchni Prostopadloscianu o bokach {a}, {b}, {c} = {2*a*b + 2*b*c + 2*c*a}")
        elif inp == "3":
            pp = float(input("Pole podstawy = "))
            pb = float(input("Pole powierzchni bocznej = "))
            print(f"pole powierzchni Graniastoslupa = {2 * pp + pb}")
        elif inp == "4":
            pp = float(input("Pole podstawy = "))
            pb = float(input("Pole powierzchni bocznej = "))
            print(f"pole powierzchni Ostroslupa = {pp + pb}")
        elif inp == "5":
            r = float(input("r (promien) = "))
            h = float(input("wysokosc = "))
            print(f"pole powierzchni Walca = {2 * PI * r**2 + 2 * PI * r * h}")
        elif inp == "6":
            r = float(input("r (promien) = "))
            l = float(input("l (tworzaca) = "))
            print(f"pole powierzchni Stozka = {PI * r**2 + PI * r * l}")
        elif inp == "7":
            r = float(input("r (promien) = "))
            print(f"pole powierzchni Kuli = {4 * PI * r**2}")
        else:
            print("WYBIERZ POPRAWNIE")

    elif inp == "2":
        print("objetosc Szescianu - 1 | objetosc Prostopadloscianu - 2 | objetosc Graniastoslupa - 3 | objetosc Ostroslupa - 4 | objetosc Walca - 5 | objetosc Stozka - 6 | objetosc Kuli - 7")
        inp = input("wpisz: ").lower().strip()
        
        if inp == "1":
            a = float(input("a = "))
            print(f"objetosc Szescianu = {a**3}")
        elif inp == "2":
            a = float(input("a = "))
            b = float(input("b = "))
            c = float(input("c = "))
            print(f"objetosc Prostopadloscianu = {a * b * c}")
        elif inp == "3":
            pp = float(input("Pole podstawy = "))
            h = float(input("Wysokosc = "))
            print(f"objetosc Graniastoslupa = {pp * h}")
        elif inp == "4":
            pp = float(input("Pole podstawy = "))
            h = float(input("Wysokosc = "))
            print(f"objetosc Ostroslupa = {(1/3) * pp * h}")
        elif inp == "5":
            r = float(input("r (promien) = "))
            h = float(input("wysokosc = "))
            print(f"objetosc Walca = {PI * r**2 * h}")
        elif inp == "6":
            r = float(input("r (promien) = "))
            h = float(input("wysokosc = "))
            print(f"objetosc Stozka = {(1/3) * PI * r**2 * h}")
        elif inp == "7":
            r = float(input("r (promien) = "))
            print(f"objetosc Kuli = {(4/3) * PI * r**3}")
        else:
            print("WYBIERZ POPRAWNIE")
    else:
        print("WYBIERZ POPRAWNIE")

elif inp == "2":
    print("obwody figur plaskich - 1 | pole figur plaskich - 2 | inne wzory plaskie - 3")
    inp = input("wpisz: ").lower().strip()
    
    if inp == "1":
        print("obwKwadratu - 1 | obwProstokata - 2 | obwRownolegloboku - 3 | obwTrapezu - 4 | obwTrojkata - 5 | obwTrojkataRownobocznego - 6 | obwKola - 7 | obwRombu - 8")
        inp = input("wpisz: ").lower().strip()
        
        if inp == "1":
            a = float(input("a = "))
            print(f"obwod Kwadratu = {4 * a}")
        elif inp == "2":
            a = float(input("a = "))
            b = float(input("b = "))
            print(f"obwod Prostokata = {2 * a + 2 * b}")
        elif inp == "3":
            a = float(input("a = "))
            b = float(input("b = "))
            print(f"obwodRownolegloboku = {2 * a + 2 * b}")
        elif inp == "4":
            a = float(input("a = "))
            b = float(input("b = "))
            c = float(input("c = "))
            d = float(input("d = "))
            print(f"obwod Trapezu = {a + b + c + d}")
        elif inp == "5":
            a = float(input("a = "))
            b = float(input("b = "))
            c = float(input("c = "))
            print(f"obwod Trojkata = {a + b + c}")
        elif inp == "6":
            a = float(input("a = "))
            print(f"obwod TrojkataRownobocznego = {3 * a}")
        elif inp == "7":
            r = float(input("r (promien) = "))
            print(f"obwod Kola = {2 * PI * r}")
        elif inp == "8":
            a = float(input("a (dlugosc boku a) = "))
            print(f"obwod Rombu = {4 * a}")
        else:
            print("WYBIERZ POPRAWNIE")

    elif inp == "2":
        print("pole Kwadratu - 1 | pole Prostokata - 2 | pole Rownolegloboku - 3 | pole Trapezu - 4 | pole Trojkata - 5 | pole TrojkataRownobocznego - 6 | pole Kola - 7 | pole Rombu(z h) - 8 | pole Rombu(z e,f) - 9")
        inp = input("wpisz: ").lower().strip()
        
        if inp == "1":
            a = float(input("a = "))
            print(f"pole Kwadratu = {a**2}")
        elif inp == "2":
            a = float(input("a = "))
            b = float(input("b = "))
            print(f"pole Prostokata = {a * b}")
        elif inp == "3":
            a = float(input("a = "))
            h = float(input("h = "))
            print(f"pole Rownolegloboku = {a * h}")
        elif inp == "4":
            a = float(input("a = "))
            b = float(input("b = "))
            h = float(input("h = "))
            print(f"pole Trapezu = {((a + b) * h) / 2}")
        elif inp == "5":
            a = float(input("a = "))
            h = float(input("h = "))
            print(f"pole Trojkata = {0.5 * a * h}")
        elif inp == "6":
            a = float(input("a = "))
            print(f"pole TrojkataRownobocznego = {(a**2 * pier(3)) / 4}")
        elif inp == "7":
            r = float(input("r (promien) = "))
            print(f"pole Kola = {PI * r**2}")
        elif inp == "8":
            a = float(input("a (dlugosc boku a) = "))
            h = float(input("h (wysokosc) = "))
            print(f"pole Rombu = {a * h}")
        elif inp == "9":
            e = float(input("e (dlugosc przekatnej e) = "))
            f = float(input("f (dlugosc przekatnej f) = "))
            print(f"pole Rombu = {(e * f) / 2}")
        else:
            print("Nie ma takiej komendy")

    elif inp == "3":
        print("wysokosc TrojkataRownobocznego - 1 | przekatnaKwadratu - 2 | twierdzeniePitagorasa - 3")
        inp = input("wpisz: ").lower().strip()
        
        if inp == "1":
            a = float(input("a = "))
            print(f"wysokosc TrojkataRownobocznego = {(a * pier(3)) / 2}")
        elif inp == "2":
            a = float(input("a = "))
            print(f"przekatnaKwadratu = {a * pier(2)}")
        elif inp == "3":
            a = float(input("a = "))
            b = float(input("b = "))
            print(f"przeciwprostokatna c = {pier(a**2 + b**2)}")
        else:
            print("WYBIERZ POPRAWNIE")

    else:
        print("WYBIERZ POPRAWNIE")

else:
    print("WYBIERZ POPRAWNIE")





