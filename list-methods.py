numbers = [1,10,5,16,4,9,10]
letters = ["a", "g", "s", "b","y", "a", "s"]

val = min(numbers)
val = max(numbers)
val = max(letters)
val = min(letters)

val = numbers[3:6]
print("index : ")
print(val)
val = numbers[:3]
val = numbers[4:]
print(val)

numbers[4] = 40

numbers.append(49) #Listeye eleman ekler
numbers.insert(3, 78)
numbers.insert(-1, 52) #İlk yazılan elemandan öncesine başka bir eleman ekler

#numbers.pop()  
#numbers.pop(-1) Yazılan sıradaki elemanı siler.
#numbers.remove(49) Yazılan elemanı siler.

numbers.sort() #En küçük sayıdan büyüğe sıralar.
letters.sort() #En baş harften sona doğru sıralar.
numbers.reverse() #Ters çevirir
letters.reverse()

print(numbers)
print(letters)

print(len(numbers))
print(len(letters))

print(numbers.count(10))
print(letters.count("a"))

numbers.clear()
print(numbers)


names = ["Ali", "Yağmur", "Hakan", "Deniz"]
years = [1998, 2000, 1998, 1987]


#1
#names.append("Cenk")
#print(names)

#2
#names.insert(0, "Sena")
#print(names)

#3
#names.remove("Deniz")
#print(names)

#4
#index = names.index("Deniz")
#print(index)

#5
#result = "Ali" in names
#print(result)

#6
#names.reverse()
#print(names)

#7
#names.sort()
#print(names)

#8
#years.sort()
#print(years)

#9
#str = "Chevrolet, Dacia"
#result = str.split(",")
#print(result)

#list = ["Chevrolet", "Dacia"]
#print(list)

#10
#list = max(years)
#list1 = min(years)
#print(list, list1) 

#11
#result =(years.count(1998))
#print(result)

#12
#years.clear()

13
markalar = []

marka = input("Marka: ")
markalar.append(marka)

marka = input("Marka: ")
markalar.append(marka)

marka = input("Marka: ")
markalar.append(marka)
print(markalar)