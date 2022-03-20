import random
seviye=input("bir seviye seçiniz (kolay/orta/zor):").upper()

if seviye =="kolay":
    uret=random.randint(1,10)#1 ile 10 arasında rastgele sayı üretiniz
elif seviye=="orta":
    uret=random.randint(1,50)
elif seviye=="zor":
    uret=random.randint(1,100)
else:
    print("lütfen doğru sayıyı giriniz")
while True:
    tahmin=int(input ("Tahmininiz"))
    if tahmin==uret:
        print("Tebrikler sayıyı buldunuz")
        break
    elif tahmin<uret:
        print("üzgünüm, sayınızı büyültün!")
    else:
        print("üzgünüm, sayınızı küçültün")