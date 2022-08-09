message = "Hello There. My name is Alptekin Küçükali"
#message = message.upper()   =>Cümlenin her harfini büyük yazar upper metodu.
#message = message.lower()   =>Cümlenin her harfini küçük yazar.
#message = message.title()   =>Her kelimenin baş harfi büyük olur.
#message = message.capitalize()   =>İlk kelimenin ilk harfini büyük yapar diğerleri küçük olur.

#message = message.strip()   =>Kullanıcının girdiği karakterlerin başı ve sonundaki boşluk karakterleri siler.
#message = message.split()   =>Her kelime ayrı ayrı gösterilir.
#message = message.split(".")   =>Noktadan itibaren ayırır. 

#message = " ".join(message)  =>Split ile ayrılan kelimeleri tekrar bütün yapar.

#index = message.find("Alptekin")   =>Cümlenin içinde bu kelime geçiyor mu?
#isFound = message.startswith("H")   =>Cümle bu harfle başlıyor mu ona bakar.
#isFound = message.endswith("i")   =>Cümle bu harf ile bitiyor mu?
#print(isFound)

#message = message.replace("Alptekin","Ali")   =>Bir kelime yerine söyleneni yazar 
#message = message.replace(" ","*")

message = message.center(50,"*")

print(message) 