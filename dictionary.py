# key - value
# 41 => Kocaeli  34 => İstanbul

sehirler = ["Kocaeli", "İstanbul"]
plakalar = [41, 34]
print(plakalar[sehirler.index("İstanbul")])

#print(plakalar["Kocaeli"]) => 41
#print(plakalar["İstanbul"])  => 34

plakalar = { "Kocaeli" : 41, "İstanbul": 34 }
print(plakalar["Kocaeli"])

plakalar["Ankara"] = 6
plakalar["Kocaeli"] = "new value"

print(plakalar)

users = {
    "sadikturan": {
        "age" : 36,
        "roles": ["user"],
        "email" : "sadikturan@gmail.com",
        "address" : "Kocaeli",
        "phone" : "1231321",
      },
    "cinarturan" : {
        "age" : 2,
        "roles": ["admin","user"],
        "email" : "cinar@gmail.com", 
        "address" : "Kocaeli",
        "phone" : "1231321" 
      }
}

#print(users["cinarturan"]["roles"][0])