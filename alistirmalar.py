###soru 1: Bir listedeki sayıların toplamını ekrana yazdırınız.
#sayi = int(input('Sayı: '))
#liste = list(range(1,sayi+1))
# liste = [3,5,8]
# toplam = 0
# for say in liste:
#     toplam += say

# print("Sonuç " +  toplam)

###Soru 2: 1 den 100 'e kadar (100 dahil) 3'e bölünen çift sayıları yazınız.
# print('3 e bölünen çift sayılar: ')
# for sayi in range(1,101):
#     if sayi % 2 == 0:
#         if sayi % 3 == 0: 
#             print(sayi)

### Soru 3: 1 otoparkta ücret tarifesi aşağıdaki gibidir.
# 1 saate kadar saat başı 5 TL
#1-5 saat arası saat başı 4 TL
#5 saatten fazlası saat başı 3 TL 
#kullanıcıdan alınan saat değereine göre ödenmesi gereken miktarı ekrana yazdırınız.
# saat = int(input('Kullanım süresi(saat): '))
# if saat <= 1:
#     print('Vereceğiniz ücret 5TL dir.')
# elif (saat <= 5):
#     print(f'Vereceğiniz ücret: {saat*4}')
# else:
#     print(f'Vereceğiniz ücret: {saat*3}')


### Soru 4: Bir dikdörtgenin genişliği ve yüksekliğini kullanarak alanını ve çevresini hesaplayınız.
# kisaKenar = int(input('Dikdörtgenin kısa kenarı: '))
# uzunKenar = int(input('Dikdörtgenin uzun kenarı: '))
# cevre = (uzunKenar + kisaKenar) *2
# alan = uzunKenar * kisaKenar
# print(alan)
# print(cevre)


### Soru 5: Çarpım taplosunu ekrana yazırınız.
# for i in range(1,11):
#     for j in range(1,11):
#         print(f"{i} * {j} = { i * j }")
#     print("*********")


### Soru 6: Klavyeden girilen bir sayının asal olup olmadığını yazdıran
# asalmi = True
# sayi = int(input('Bir sayı giriniz: '))
# for i in range(2,sayi):
#     if sayi % i == 0:
#         asalmi = False
#         break
# if asalmi :
#     print(f'Sayı asaldır {sayi}')
# else:
#     print(f'Sayı asal değildir. {sayi}')


### Soru 4: Kullanıcı tarafından girilen bir metin içerisinde kaç adet "a" harfi oldugunu ekrana yazdıran programı yazınız.
# metin = input('Bir metin giriniz: ')
# sayac = 0
# for i in metin:
#     if i == 'a' or i == 'A':
#         sayac += 1

# print(sayac)

### Soru 8: aşagıdakı kadun çıktısını yazınız
# for x in range(10):
#     if x % 2 == 0:
#         continue
#     print(x)
#1,3,5,7,9

### Soru 9: aşagıdakı kodun çıktısı nedir?
# for sayi in range(10,0,-1):
#     print(sayi)
#10,9,8,7,...,1

### Soru 10: 1-100 arasında hem 3 hem de 5 e bölünen sayıları bulunuz.
# for i in range(1,101):
#     if i % 3 == 0 and i % 5 == 0:
#         print(f'{i} 3 ve 5 e bölünür ')


###Soru 11: 1-100 arasındaki çift ve tek sayıların toplamı
# ciftToplam = 0
# tekToplam = 0
# for sayi in range(1,101):
#     if sayi % 2 == 0:
#         ciftToplam = ciftToplam + sayi
#     else:
#         tekToplam += sayi
# print(tekToplam, ciftToplam)

###Soru 12: Kullanıcıdan alınan maaş ve zom oranını kullanarak 
#zamlı maaşı ekrana yazdırınız.
# maas = int(input('Maaşınız: '))
# zamOrani = int(input('Maaşınıza gelen zam oranı: % '))
# zamliMaas = maas + maas * zamOrani/100
# print(zamliMaas)

###Soru 13 : Kullanıcının girdiği iki sayı arasındaki çift sayıların ortalamasını
#bulunuz.
# altSinir = int(input('1. Sayı: '))
# ustSinir = int(input('2. Sayı: '))
# toplam = 0
# sayac = 0
# for sayi in range(altSinir,ustSinir + 1):
#     if sayi % 2 == 0:
#         sayac += 1
#         toplam += sayi
# ort = toplam / sayac
# print(ort)




        




###Genel Notlar
# mesaj = "Toplam : {} + {} = {}".format(3,5, 3 + 5)
# print(mesaj)

# mesaj = "Toplam : {1} + {0} = {2}".format(3,5, 3 + 5)
# print(mesaj)

# print('Ankara \'nın bagları')

# metin = "Alptekin"
# print(metin[0])

#print("Alptekin","ismail","Levent","Ali" ,sep=" * ", end=" => ")

# def topla(*sayilar, islem="+"):
    
#     if islem == "+":
#         sonuc = 0
#     else:
#         sonuc = 1

#     for say in sayilar:
#         if islem == "+" :
#             sonuc += say
#         else:
#             sonuc *= say
#     return sonuc

# print(topla(12,3,1,4,islem="*"))

text = "Alptekin Küçükali"

print(text[2:5])
print(text[::-1])
print(text[::2])

liste = [1,2,3,4,5,6,7,8]



a = 4 
b = 3 
print(a,b)
a = 3
print(a,b)
b = 4
print(a,b)