faktoriyel=1

while True:
    sayı=int(input("Bir sayı giriniz:"))
    if sayı <=0:
        print("Negatif olmayan bir sayı giriniz.")
    else:
        for i in range(1,sayı+1):
            faktoriyel*=i
        print("Sayınızın cevabı:",faktoriyel)
        break

