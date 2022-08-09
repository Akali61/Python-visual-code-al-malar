import random

sayi = random.randint(1,100)
can = int(input('Kaç hak kullanmak istersiniz:'))
hak = can
sayac = 0
while hak > 5:
    hak -= 1
    sayac += 1
    tahmin = int(input('tahmin: '))

    if sayi == tahmin:
        print(f'Tebrikler {sayac}.defada bildiniz. Toplam puanınız: {100 - (100/can)*(sayac-1)}')
        break
    elif sayi > tahmin:
        print('yukarı')
    else: 
        print('aşağı')

    if hak == 0:
        print(f'Hakkınız bitti.Tutulan sayı: {sayi}')