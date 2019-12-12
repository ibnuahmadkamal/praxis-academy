import pymysql

db = pymysql.connect(
  host="localhost",
  user="root",
  passwd="",
  database="praktik_praxis"
)

cursor = db.cursor()
sql = """CREATE TABLE customers (
  Id_user INT(13) AUTO_INCREMENT PRIMARY KEY,
  Nama VARCHAR(255),
  Alamat Varchar(255)
)
"""
cursor.execute(sql)

print("Tabel customers berhasil dibuat!")