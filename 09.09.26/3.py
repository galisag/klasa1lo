print("ile masz na koncie?")
stan_konta = float(input())

if stan_konta < 0:
    print("masz debet")
elif stan_konta == 0:
    print("zero")
elif stan_konta <= 40:
    print("klepiesz biede")
elif stan_konta > 40 and stan_konta <= 100:
    print("moze wyzyjesz")
elif stan_konta > 100 and stan_konta <= 400:
    print("spoko")
else:
    print("podziel sie")