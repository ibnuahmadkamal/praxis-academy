import pymysql

db = pymysql.connect(
  host="localhost",
  user="root",
  passwd="",
  database="praktik_praxis"
)

cursor = db.cursor()
sql ="INSERT INTO customers(Nama,Alamat) VALUES (%s,%s)"
values = [
    ("Bot1","Kudus"),
    ("Bot2","Jepara"),
    ("Bot3","Pati")
]
for val in values:
  cursor.execute(sql, val)
  db.commit()

print("{} data ditambahkan".format(len(values)))