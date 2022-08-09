#1
# sayi = float(input("Sayı: "))
# result = (sayi > 0) and (sayi <= 100)
# print(f" sayı 0 ile 100 arasında mı? {result}")

#2
#sayi = int(input("Sayı: "))
#result = (sayi > 0) and (sayi %2 == 0)
#print(f'Sayı, pozitif çift sayı mı? {result}')

#3
# email = "alptekin61@gmail.com"
# sifre = "64734728"
# girilenEmail = input('Email giriniz: ')
# girilenPassword = input('Şifre giriniz: ')
# result = (girilenEmail == email) and (girilenPassword == sifre)
# print(f'Doğru giriş yaptınız: {result}')

#4
# a = int(input('a: '))
# b = int(input('b: '))
# c = int(input('c: '))

# result = (a > b) and (a > c)
# print(f'a en büyük sayıdır : {result}')

# result = (b > a) and (b > c)
# print(f'b en büyük sayıdır : {result}')

# result = (c > a) and (c > b)
# print(f'c en büyük sayıdır : {result}')

#5
#vize1 = float(input('vize 1 : '))
#vize2 = float(input('vize 2 : '))
#final = float(input('final: '))
#ortalama = (vize1 * 0.3) + (vize2 * 0.3) + (final * 0.4)
#print(ortalama)
#result = (ortalama >= 50)
#sonuc = (f'Dersten geçtiniz: {result}')
#print(sonuc)
#sonuc2 = (ortalama == 50) or (final >= 50 )
#resut = (f'Final notu 50 ve 50 den büyüktür: {sonuc2}')
#print(resut)
#sonuc3 = (final == 70) and (ortalama >= 0)
#rest = (f'Ortalamanın önemi yoktur: {sonuc3}')
#print(rest)

#6
"""
Hoşgeldiniz
0-18.4   => Zayıf
18.5-24.9  => Normal
25.0-29.9  => Fazla Kilolu
30.0-34.9  => Şişman (Obez)
"""
name = input('Adınız: ')
kilo = float(input('Kilonuz: '))
boy = float(input('Boyunuz: '))

sonuc = (kilo) / (boy **2)
zayif = (sonuc >= 0) and (sonuc <= 18.4)
normal = (sonuc > 18.4) and (sonuc <= 24.9)
kilolu = (sonuc > 24.9) and (sonuc <= 29.9)
obez = (sonuc >= 29.9) and (sonuc <= 34.9)

print(f'{name} kilo indeksin: {sonuc} ve kilo değerlendirmen zayıf {zayif}')
print(f'{name} kilo indeksin: {sonuc} ve kilo değerlendirmen normal {normal}')
print(f'{name} kilo indeksin: {sonuc} ve kilo değerlendirmen kilolu {kilolu}')
print(f'{name} kilo indeksin: {sonuc} ve kilo değerlendirmen şişman {obez}')