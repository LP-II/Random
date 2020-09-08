import random

gæt = 0

RN = random.randint(1,10)
print("hvad er dit navn ?")
Navn = input()


print("Hej " + Navn,"prøv at gætte et tal mellem 1 og 10!")
while gæt < 6:
    x = input()
    x = int(x)
    gæt = gæt + 1

    if x < RN:
        print("Dit tal er for lavt")

    if x > RN:
        print("Dit tal er for højt")

    if x == RN:
        break

if x == RN:
    gæt = str(gæt)
    print("Flot " + Navn, ",du gættede tallet rigtigt med " + gæt, "gæt!")
if x != RN:
    RN = str(RN)
    print("Nummeret var " + RN, "din noob")


