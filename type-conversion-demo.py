'''
     Daire Alanı : pirekare
     Daire Çevresi : 2pire

     * Yarı çapı verilen bir dairenin alanını 
     hesaplayınız. (r: 3.14)
'''

pi = 3.14
r = float(input("Dairenin yarı çapı: "))
alan = pi * (r ** 2)
print(type(alan))

cevre = 2 * pi * r
print(type(cevre)) 

print("alan: "+ str(alan) + " çevre: " + str(cevre))