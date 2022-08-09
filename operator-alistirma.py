x, y, z = 2, 5, 10
numbers = 1, 5, 7, 10, 6 #tuple olarak atama yapar
print(numbers) 


#1
#a = int(input("1. Sayı: "))
#b = int(input("2. Sayı: "))
#theresult = (a * b)-(x + y + z)
#print(theresult)

#2
#y //= x
#
#3
#sonuc = (x + y + z) % 3 

#4
#sonuc = y ** x

#5 
#sonuc = z ** 3

#6
x, *y, z = numbers
sonuc = y[0] + y[1] + y[2]
print(sonuc)