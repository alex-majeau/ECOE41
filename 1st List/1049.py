type1 = input()
type2 = input()
type3 = input()

if (type1 == "vertebrado"):
    if(type2 == "ave"):
        if (type3 == "carnivoro"):
            print("aguia")
        else:
            print("pomba")
    else: # nao e' ave
        if (type3 == "onivoro"):
            print("homem")
        else:
            print("vaca")

else:   # nao e' vertebrado
    if (type2 == "inseto"):
        if (type3 == "hematofago"):
            print("pulga")
        else:
            print("lagarta")
    else:   #nao e' inseto
        if (type3 == "hematofago"):
            print("sanguessuga")
        else:
            print("minhoca")
