b=10
import random
a=random.randint(1,100)
while True :
    print(b,"hakınız var.")
    b-=1
    if b<0:
        print("Hakkınız bitti.")
        break
    c=int(input("Sayıyı tahmin ediniz:"))
    if c<a:
        print("Biraz daha büyük sayı tahmin ediniz.")
    elif c>a:
        print("Biraz daha küçük sayı tahmin ediniz.")
    else:
        print("Tebrikler sayıyı buldunuz.")
        break


