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

def getProductById(id):
    connection = mysql.connector.connect(host = "localhost", user = "root", password = "A20022006Kt@S", database = "node-app")
    cursor = connection.cursor()

    sql = "Select * From Products Where id=%s"
    params = (id,)

    cursor.execute(sql,params)

    #cursor.execute("Select * From Products Where name LIKE '%Samsung%' and price=3000") #İsmi Samsung olan telefonları gösterir.
    #cursor.execute("Select * From Products Where id=1")

    #result = cursor.fetchall()
    result = cursor.fetchone()

    #print(result)

    print(f'id: {result[0]} name: {result[1]} price: {result[2]}')

getProductById(6)