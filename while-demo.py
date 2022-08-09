sayilar = [1,3,5,7,9,12,19,21]

# i = 0
# while (i < len(sayilar)):
#     print(sayilar[i])
#     i += 1


# baslangic = int(input('Başlangıç: '))
# bitis = int(input('Bitiş: '))

# i = baslangic
# while i < bitis:
#     i += 1
#     if (i % 2 == 1):
#         print(i)


# i = 100

# while i > 0:
#     print(i)
#     i -= 1


# numbers = []
# i = 0

# while i<5:
#     sayi = int(input('Sayı: '))
#     numbers.append(sayi)
#     i+=1
# print(numbers)



urunler = []
adet = int(input('Kaç ürün eklemek istiyorsunuz: '))
i = 0

while(i<adet):
    name = input('Ürün ismi: ')
    price = input('Ürün fiyatı: ')
    urunler.append({
        'name': name,
        'price': price
    })
    i += 1

for urun in urunler:
    print(f'ürün adı: {urun["name"]} ürün fiyatı: {urun["price"]}')