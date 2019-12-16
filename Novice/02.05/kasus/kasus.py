import mysql.connector
db = mysql.connector.connect(
  host="localhost",
  user="root",
  passwd="",
  database="kasus_praxis"
)
cursor = db.cursor()
sql = "select movie_rented FROM tabel2 WHERE Membership_id = 1"
cursor.execute(sql)

results = cursor.fetchall()

for data in results:
  print(data)