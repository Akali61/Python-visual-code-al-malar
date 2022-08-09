#Bankamatik Uygulaması

SadikHesap = {
    'ad': 'Sadık Turan',
    'hesapNo': '1324567867484',
    'bakiye': 3000,
    'ekHesap': 2000
}

AliHesap = {
    'ad': 'Ali Turan',
    'hesapNo': '1324567856847',
    'bakiye': 2000,
    'ekHesap': 1000
}

def paraCek(hesap, miktar):
    print(f"Merhaba {hesap['ad']}")

    if (hesap['bakiye'] >= miktar):
        hesap['bakiye'] -= miktar
        print('Paranızı alabilirsiniz.')
        bakiyeSorgula(hesap)
    else: 
        toplam = hesap['bakiye'] + hesap['ekHesap']

        if (toplam >= miktar):
            ekHesapKullanimi = input('Ek hesap kullanılsın mı(e/h): ')

            if ekHesapKullanimi == 'e':
                ekHesapKullanilacakMiktar = miktar - hesap['bakiye']
                hesap['bakiye'] = 0
                hesap['ekHesap'] -= ekHesapKullanilacakMiktar
                print('Paranızı alabilirsiniz.')
                bakiyeSorgula(hesap)
            else:
                print(f"{hesap['hesapNo']} nolu hesabınızda {hesap['bakiye']} bulunmaktadır")
        else:
            print('Üzgünüz bakiye yetersiz.')
            bakiyeSorgula(hesap)

def bakiyeSorgula(hesap):
    print(f"{hesap['hesapNo']} nolu hesabınızda {hesap['bakiye']} TL bulunmaktadır. Ek hesap limitinizde ise {hesap['ekHesap']} TL bulunmaktadır.")

paraCek(SadikHesap, 3000)
bakiyeSorgula(SadikHesap)
print('******************')
paraCek(SadikHesap, 2000)
bakiyeSorgula(SadikHesap)