taskagitmakas=["ta�","ka��t","makas"]
import random
ta�=taskagitmakas[0]
ka��t=taskagitmakas[1]
makas=taskagitmakas[2]
gir=input("Ta� m�? Ka��t m�? Makas m�?")
a=random.choice(taskagitmakas)

print("bilgisayar", a,"se�ti")
if gir==ka��t:
    if ka��t==a:
        print("berabere")
    elif ta�==a:
        print("kazand�n�z")
    elif makas==a:
        print("kaybettiniz")
elif gir==ta�:
    if ta�==a:
        print("berabere")
    elif ka��t==a:
        print("kaybettiniz")
    elif makas==a:
        print("kazand�n�z")
elif gir==makas:
    if makas==a:
        print("berabere")
    elif ta�==a:
        print("kaybettiniz")
    elif ka��t==a:
        print("kazand�n�z")


