taskagitmakas=["taþ","kaðýt","makas"]
import random
taþ=taskagitmakas[0]
kaðýt=taskagitmakas[1]
makas=taskagitmakas[2]
gir=input("Taþ mý? Kaðýt mý? Makas mý?")
a=random.choice(taskagitmakas)

print("bilgisayar", a,"seçti")
if gir==kaðýt:
    if kaðýt==a:
        print("berabere")
    elif taþ==a:
        print("kazandýnýz")
    elif makas==a:
        print("kaybettiniz")
elif gir==taþ:
    if taþ==a:
        print("berabere")
    elif kaðýt==a:
        print("kaybettiniz")
    elif makas==a:
        print("kazandýnýz")
elif gir==makas:
    if makas==a:
        print("berabere")
    elif taþ==a:
        print("kaybettiniz")
    elif kaðýt==a:
        print("kazandýnýz")


