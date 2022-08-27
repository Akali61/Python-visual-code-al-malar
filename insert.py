import mysql.connector

def insertProduct(name,price,ımageUrl,description):
    connection = mysql.connector.connect(host = "localhost", user = "root", password = "A20022006Kt@S", database = "node-app")
    cursor = connection.cursor()

    sql = "INSERT INTO Products(name,price,ımageUrl,description) VALUES (%s,%s,%s,%s)"
    values = (name,price,ımageUrl,description)

    cursor.execute(sql,values)

    try:
        connection.commit()
        print(f'{cursor.rowcount} tane kayıt eklendi.')
        print(f'son eklenen kaydın id: {cursor.lastrowid}')
    except mysql.connector.Error as err:
        print('hata:',err)
    finally:
        connection.close()
        print('database bağlantısı kapandı.')

def insertProducts(list):
    connection = mysql.connector.connect(host = "localhost", user = "root", password = "A20022006Kt@S", database = "node-app")
    cursor = connection.cursor()

    sql = "INSERT INTO Products(name,price,ımageUrl,description) VALUES (%s,%s,%s,%s)"
    values = list

    cursor.executemany(sql,values)

    try:
        connection.commit()
        print(f'{cursor.rowcount} tane kayıt eklendi.')
        print(f'son eklenen kaydın id: {cursor.lastrowid}')
    except mysql.connector.Error as err:
        print('hata:',err)
    finally:
        connection.close()
        print('database bağlantısı kapandı.')

list = []
while True:   
    name = input('ürün adı: ')
    price = float(input('ürün fiyatı: '))
    ımageUrl = input('ürün resim adı: ')
    description = input('ürün açıklaması: ')

    insertProduct(name,price,ımageUrl,description)

    #list.append((name, price, ımageUrl, description))


    result = input('devam etmek istiyor musunuz? (e/h: ')
    if result == 'h':
        print('Kayıtlarınız veritabanına aktarılıyor...')
        print(list)
        insertProducts(list)
        break

insertProduct(name,price,ımageUrl,description)