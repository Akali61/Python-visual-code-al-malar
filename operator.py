#ctrl + k + c => toplu yorum satırı
#shift + alt + mause ile seç => toplu satır seçme

#x = 5
#y = 10
#z = 20

#x, y, z = 5,16,20
#x, y = y,x

# x = x + 5
# x += 5 # x = x + 5
# x -= 5 # x = x - 5
# x *= 5 # x = x * 5
# x /= 5 # x = x / 5 => ondalıklı bölme işlemi yapar
# x %= 5 # x = x % 5 =>  bölme işleminde kalanı verir
# y //= 5 # y = y // 5 => Bölme işleminin tam kısmını verir.
# y **= z # y = y ** z

values = 1, 2, 3, 4, 5  
print(values)
print(type(values))

x, y, *z = values

print(x,y,z)
print(x, y, z[1]) 