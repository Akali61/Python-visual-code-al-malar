x = 5

hak = 5
devam = 'e'
result = 5 < x < 10
result = (hak > 0) and (devam == 'e')
print(result)

#and

result = (x > 5) and (x < 10)  
# True, True => True  True, False => False

#or

result = (x > 0) or (x % 2 == 0)
#True, False => True

#not

result = not(x > 0)
# x, 5-10 arasında olan bir çift sayı mı?
result = (x>5) and (x<10) and (x%2==0)

print(result)