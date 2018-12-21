sonuc=0

while True:
    sayı=int(input("Bir sayı giriniz:"))
    sonuc+=sayı
    if sayı==15:
        print("Bu sayıyı kullanamazsınız!!")
        sonuc-=15
        print("Sayıların toplamı:",sonuc)
        break
