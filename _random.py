from cgitb import reset
from platform import java_ver
import random
from unittest import result

# result = dir(random)
# result = help(random)

result = random.random() # 0.0 - 1.0
result = random.random() *100
result = int(random.uniform(1,10))
result = random.randint

greeting = 'hello there'
names = ['ali','yağmur','deniz','cenk','ahmet','efe']
#result = names[random.randint(0,len(names)-1)]
result = random.choice(names)
result = random.choice(greeting)

liste = list(range(10))
random.shuffle(liste) #orjinal liste içindeki elemanların yeri değişir.
result = liste

liste = range(100)
result = random.sample(liste, 3) #orijinal liste içinden rastgele 3 sayı seçip ekrana yazar.
result = random.sample(names, 2)

print(result)