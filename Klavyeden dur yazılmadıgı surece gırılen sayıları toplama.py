sonuc=0

while True:
    a=input("Dur yazılana kadar bir sayı giriniz:")
    if a=="dur":
        break
    elif a!="dur":
        b=int(a)
        sonuc+=b
        print(sonuc)
