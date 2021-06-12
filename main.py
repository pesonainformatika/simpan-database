import MySQLdb

def mysql_connection():
    return MySQLdb.connect(
        host="localhost",
        user="root",
        passwd="",
        db="simpan_db"
    )

def run():
    try:
        nama = input("masukan nama: ")
        alamat = input("masukan alamat: ")
        sql = "INSERT INTO biodata (nama, alamat) VALUES (%s, %s)"
        val = (nama, alamat)
        myConnection = mysql_connection()
        cursor = myConnection.cursor()
        cursor.execute(sql, val)
        print("data tersimpan")
        myConnection.commit()

    except Exception as e:
        print(e)
        print("data tidak tersimpan")

    myConnection.close()


if __name__ == '__main__':
    run()