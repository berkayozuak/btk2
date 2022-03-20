
try:
    sayi1=int(input("Bir sayı giriniz"))
    sayi2=int(input("bir sayı giriniz"))
    print("Sayılarınızın bölümü"),sayi1/sayi2
except ValueError:
        print("Girdiğiniz değer int olmalı!")
except ZeroDivisionError:
    print("Bir sayı 0'a bölünemez")