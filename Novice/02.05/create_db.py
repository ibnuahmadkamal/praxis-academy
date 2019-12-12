import pymysql

db = pymysql.connect(
  host="localhost",
  user="root",
  passwd=""
)
cursor = db.cursor()
cursor.execute("CREATE DATABASE praktik_praxis")

print("Database berhasil dibuat!")
