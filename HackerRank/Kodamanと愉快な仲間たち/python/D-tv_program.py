D, Sh, Sm, Th, Tm = map(int, input().split())

if (D >= 1 and D <= 5):
    if (Sh >= 19 and (Th <= 21 or (Th == 22 and Tm == 0))):
        print("Yay!")
    else:
        print(":(")
else:
    if (Sh >= 7 and (Th <= 21 or (Th == 22 and Tm == 0))):
        print("Yay!")
    else:
        print(":(")
