name = 'Sadık Turan'

# for letter in name:
#     if letter == 'a':
#         break
#     print(letter)

x = 0

# while x < 5:
#     if x == 2:
#         break
#     print(x)
#     x += 1

#1-100 e kadar tek sayıların toplamı

x = 0
result = 0
while x<100:
    x += 1 
    if x % 2 == 0:
        continue
    result += x
print(f'toplam: {result}')