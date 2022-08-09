#isim = input('İsminiz: ')
#yas = int(input('Yaşınız: '))
#egitim = input('Eğitim: ')
#
#if (yas >= 18): 
#    if (egitim == 'lise' or egitim == 'üniversite'):
#        print(f'{isim} ehliyet alabilirsin.')
#    else:
#        print(f'{isim} ehliyet alamazsın eğitim durumun yetersiz' )
#else: 
#    print(f'{isim} ehliyet alamazsın yaşın tutmuyor. ')


isim = input('İsmin: ')
soyisim = input('Soy ismin: ')

yazili1 = float(input('1. Yazılı: '))
yazili2 = float(input('2. Yazılı: '))
sozlu = float(input('Sözlü: '))
ortalama = (yazili1 + yazili2 + sozlu) / 3
print(ortalama)
if (ortalama>=0) and (ortalama<25):
     print(f'{isim} {soyisim} notun 0')
elif (ortalama>=25) and (ortalama<44):
     print(f'{isim} {soyisim} notun 1')
elif (ortalama>=44) and (ortalama<55):
     print(f'{isim} {soyisim} notun 2')
elif (ortalama>=55) and (ortalama<69):
     print(f'{isim} {soyisim} notun 3')
elif (ortalama>=69) and (ortalama<84):
     print(f'{isim} {soyisim} notun 4')
elif (ortalama>=84) and (ortalama<=100):
     print(f'{isim} {soyisim} notun 5')
else:
     print('Yanlış bilgi girdiniz.')


# import datetime

# tarih = input('Aracınız hangi tarihte trafiğe çıktı (2019/8/9): ')
# tarih = tarih.split('/')
# trafigeCikis = datetime.datetime(int(tarih[0]),int(tarih[1]),int(tarih[2]))
# simdi = datetime.datetime.now()
# fark = simdi - trafigeCikis
# days = fark.days

# if days<=365:
#      print('1. servis aralığı')
# elif days > 365 and days<=365*2:
#      print('2. Servis aralığı')
# elif days > 365*2 and days <= 365*3:
#      print('3. Servis aralığı')
# else: 
#      print('Hatalı süre')