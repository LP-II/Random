from random import randint

print("Skal vi spille fucking sten saks papir!?")
prut = input()

k = ["Sten","Saks","Papir"]
Modstander = k[randint(0,2)]



if prut == Modstander:
    print("I står lige")
elif prut == "Sten":
    if Modstander == "Papir":
        print(prut + " taber til " + Modstander)
    else:
        print(prut + " vinder over " + Modstander)
elif prut == "Saks":
    if Modstander == "Sten":
        print(prut + " taber til " + Modstander)
    else:
        print(prut + " vinder over " + Modstander) 
elif prut == "Papir":
    if Modstander == "Saks":
        print(prut + " taber til " + Modstander)
    else:
        print(prut + " vinder over" + Modstander)


            