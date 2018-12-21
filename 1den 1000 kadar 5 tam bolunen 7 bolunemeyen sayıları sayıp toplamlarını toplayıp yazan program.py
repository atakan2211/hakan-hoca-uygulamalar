sonuc=0
for a in range(1,1000):
    if a%5 ==0 and a%7 !=0:
        sonuc+=a
        print(a)
print("Sayıların Toplamı:",sonuc)
