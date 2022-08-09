#1
# a = int(input("a: "))
# b = int(input("b: "))
# result =(a > b)
# print(f"a: {a} b: {b} den büyüktür: {result}")

#2
# vize1 = float(input("Vize1: "))
# vize2 = float(input("Vize2: "))
# final = float(input("Final: "))
#ortalama = vize1 * 0.3 + vize2 * 0.3 + final * 0.4
#result = ortalama >= 50
#print(f'ortalama: {ortalama} ile geçtiniz: {result}' )

#3
#a = int(input(" Sayı: "))
#sonuc = a % 2 == 0
#print(f"{a} sayısı çifttir: {sonuc}") 

#4
# a = int(input("Bir sayı giriniz: "))
# sonuc = a < 0 
# print(f"Girdiğin sayı {a} negatiftir: {sonuc}")

#5
parola= "12345"
email = "alptekin@gmail.com"
girilenEmail = input("Email giriniz: ")
girilenParola = input("Parola giriniz: ")
sonuc = (girilenParola == parola) and (girilenEmail == email)
print(f'Doğru giriş yapıldı: {sonuc}')