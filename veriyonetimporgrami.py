import json
import os
def veri_yükle(dosya_adı):
    if os.path.exists(dosya_adı):
        with open (dosya_adı, "r") as dosya:
            return json.load(dosya)
    return {"gelir": [], "gider": []}

def veri_kaydet(dosya_adı, veri):
    with open (dosya_adı, "w") as dosya:
        json.dump(veri, dosya, indent=4) 


def gelir_ekle(veri):
    try:
        miktar = float(input("Gelir miktarınızı girin: "))
        aciklama = input("Gelir açıklamasını girin: ")
        veri["gelir"].append({"miktar": miktar, "açıklama": aciklama})
        print("Gelir eklendi.")
    except ValueError:
        print("Geçersiz giriş. Lütfen geçerli bir sayı girin.")

    
def gider_ekle(veri):
    try:
        miktar = float(input("Gider miktarını girin: "))
        aciklama = input("Gider açıklamasını girin: ")
        veri["gider"].append({"miktar": miktar, "açıklama": aciklama})
        print("Gider eklendi.")
    except ValueError:
        print("Geçersiz giriş. Lütfen geçerli bir sayı girin.")

def mali_durum(veri):
    toplam_gelir = sum(gelir ["miktar"] for gelir in veri["gelir"])
    toplam_gider = sum(gider ["miktar"] for gider in veri["gider"])
    bakiye = toplam_gelir - toplam_gider

    print("\n--- Mali Durum ---")
    print(f"Toplam Gelir: {toplam_gelir:.2f} TL")
    print(f"Toplam Gider: {toplam_gider:.2f} TL")
    print(f"Mevcut Bakiye: {bakiye:.2f} TL")

def ana_menu():
    dosya_adı = "finans.json"
    veri = veri_yükle(dosya_adı)

    while True:
        print("\n Kişisel Finans Yönetim Programı ")
        print("\n 1. Gelirinizi Girin:  "),
        print("\n 2. Giderinizi Girin:  ")
        print("\n 3. Mali Durumu görüntüle ")
        print("\n 4. Çıkış ")

        secim = input("Seçiminizi yapınız: 1/2/3/4 ::")

        if secim == '1':
            gelir_ekle(veri)
        elif secim == '2':
            gider_ekle(veri)
        elif secim == '3':
            mali_durum(veri)
        elif secim == '4':
            veri_kaydet(dosya_adı, veri)
            print("Çıkış yapılıyor...")
            break

        else:
            print("Geçersiz Seçim. Lütfen 1-2-3-4 sayılarından birini girin.")

if __name__ == "__main__":
    ana_menu()
