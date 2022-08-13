# x = 10

# if x > 5:
#raise Exception("x 5 ten büyük değer alamaz.")

# def check_password(psw):
#     import re
#     if len(psw) < 8:
#         raise Exception("Parola en az 7 karakterli olmalıdır.")
#     elif not re.search("[a-z]", psw):
#         raise Exception("Parola küçük harf içermelidir.")
#     elif not re.search("[A-Z]", psw):
#         raise Exception("Parola büyük harf içermelidir.")
#     elif not re.search("[0-9]", psw):
#         raise Exception("Parola rakam içermelidir.")
#     elif not re.search("[_@$]", psw):
#         raise Exception("Parola alpha numeric karakter içermelidir.")
#     elif re.search("[\s]", psw):
#         raise Exception("Parola boşluk içermemelidir.")
#     else:
#         print("Geçerli parola")
# password = "123456aE@"

# try:
#     check_password(password)
# except Exception as ex:
#     print(ex)
# else:
#     print("Geçerli parola: else")
# finally:
#     print("Validation tamamlandı.")

from unicodedata import name


class Person:
    def __init__(self, name, year):
        if len(name) > 10:
            raise Exception("Name alanı fazla karakter içeriyor.")
        else:
            self.name = name

p = Person("Aliiiiiiiiiiiii", 1989)