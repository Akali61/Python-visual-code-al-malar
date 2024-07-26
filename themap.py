#Öncelikle, gerekli olan bunu yüklemelisin:
#pip install geopy

import random
from geopy.geocoders import Nominatim
from geopy.exc import GeocoderTimedOut

sehirler = {
    "İstanbul": "41, 28",
    "Ankara": "39, 32",
    "İzmir": "38, 27",
    "Antalya": "36, 30",
    "Bursa": "40, 29",
    "Adana": "37, 35",
    "Konya": "37, 32",
    "Gaziantep": "37, 37",
    "Mersin": "36, 34",
    "Kayseri": "38, 35"
}

def sehir_sec():
    return random.choice(list(sehirler.keys()))

def koordinatlari_getir(sehir):
    geolocator = Nominatim(user_agent="sehir_bulmacasi")
    try:
        location = geolocator.geocode(sehir)
        if location:
            return location.latitude, location.longitude
        else:
            return None
    except GeocoderTimedOut:
        return koordinatlari_getir(sehir)

def oyun():
    print("Türkiye'deki şehirleri bulma oyunu")
    print("Şehirlerin koordinatlarını tahmin edin!")
    
    while True:
        sehir = sehir_sec()
        print(f"\nŞehir: {sehir}")
        
        koordinatlar = koordinatlari_getir(sehir)
        if not koordinatlar:
            print("Şehir bilgileri alınamadı, lütfen tekrar deneyin.")
            continue
        
        dogru_latitude, dogru_longitude = koordinatlar
        
        try:
            latitude_tahmin = float(input("Tahmininiz (enlem): "))
            longitude_tahmin = float(input("Tahmininiz (boylam): "))
        except ValueError:
            print("Lütfen geçerli bir sayı girin.")
            continue
        
        if (abs(latitude_tahmin - dogru_latitude) < 0.5 and
            abs(longitude_tahmin - dogru_longitude) < 0.5):
            print("Tebrikler! Koordinatlar doğru!")
        else:
            print(f"Üzgünüm, doğru koordinatlar: {dogru_latitude}, {dogru_longitude}")
        
        devam = input("Başka bir şehir tahmini yapmak ister misiniz? (e/h): ")
        if devam.lower() != 'e':
            break

if __name__ == "__main__":
    oyun()