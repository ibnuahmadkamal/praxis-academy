import pymysql

db = pymysql.connect(
  host="localhost",
  user="root",
  passwd="",
  database="praktik_praxis"
)
cursor =db.cursor()
sql = "SELECT * FROM customers"
cursor.execute(sql)

results = cursor.fetchall()

for data in results:
  print(data)