import random
def add_club(clubs, club):
    if club in clubs:
        print(f"{club} zaten listede mevcut.")
    else:
        clubs.append(club)
        print(f"{club} başarıyla eklendi.")

def shuffle_clubs(clubs):
    random.shuffle(clubs)
    print("Kulüpler başarıyla karıştırıldı.")

def save_to_next_season(current_season, next_season):
    next_season.clear()
    next_season.extend(current_season)
    print("Karışık sıralama bir sonraki sezon için kaydedildi.")

def list_clubs(clubs):
    if clubs:
        print("Mevcut futbol kulüpleri:")
        for index, club in enumerate(clubs, start=1):
            print(f"{index}. {club}")
    else:
        print("Listede hiç futbol kulübü yok.")

def main():
    current_season = []
    next_season = []

    while True:
        print("\nFutbol Kulübü Yönetimi Programı")
        print("1. Kulüp Ekle")
        print("2. Kulüpleri Karıştır")
        print("3. Karışık Sıralamayı Kaydet (Bir Sonraki Sezon İçin)")
        print("4. Kulüpleri Listele")
        print("5. Programı Sonlandır")

        choice = input("Yapmak istediğiniz işlemi seçin (1/2/3/4/5): ")

        if choice == '1':
            club_name = input("Eklemek istediğiniz kulübün adını girin: ")
            add_club(current_season, club_name)
        elif choice == '2':
            shuffle_clubs(
                          current_season)
        elif choice == '3':
            save_to_next_season(current_season, next_season)
        elif choice == '4':
            list_clubs(current_season)
        elif choice == '5':
            print("Programdan çıkılıyor...")
            break
        else:
            print("Geçersiz seçim. Lütfen 1 ile 5 arasında bir seçim yapın.")

if __name__ == "__main__":
    main()