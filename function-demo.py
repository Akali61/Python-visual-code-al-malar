#1- Gönderilen bir kelimeyi belirtilen kez ekrana yazdıran fonsiyon

# def yazdir(kelime, adet):
#     print(kelime * adet)

# yazdir('Merhaba\n', 10)


#2- Kendine gönderilen sınırsız parametreyi bir listeye çeviren fonksiyon yazınız.

# def listeyeCevir(*params):
#     liste = []

#     for param in params:
#         liste.append(param)
#     return liste
# result = listeyeCevir(10, 20, 30, 'Merhaba')
# print(result)


#3- Gönderilen 2 sayı arasındaki tüm asal sayıları bulun.

# def asalSayılariBul(sayi1, sayi2):
#     for sayi in range(sayi1, sayi2 + 1):
#         if sayi > 1:
#             for i in range(2,sayi):
#                 if (sayi % i == 0):
#                     break
#                 else: 
#                     print(sayi)
# sayi1 = int(input('Sayı 1: '))
# sayi2 = int(input('Sayı 2: '))
# asalSayılariBul(sayi1, sayi2)

#4- Kendisine gönderilen bir sayının tam bölenlerini bir liste şeklinde dönüştürün.

def tamBolenleriBul(sayi):
    tamBolenler = []

    for i in range(2,sayi):
        if (sayi % i == 0):
            tamBolenler.append(i)
        
    return tamBolenler

print(tamBolenleriBul(20))