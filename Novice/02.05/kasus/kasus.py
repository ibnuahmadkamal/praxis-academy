import mysql.connector
db = mysql.connector.connect(
  host="localhost",
  user="root",
  passwd="",
  database="kasus_praxis"
)
number = 0
cursor = db.cursor()
sql = "SELECT t1.Full_Names, t2.movie_rented FROM tabel1 t1, tabel2 t2 WHERE t1.Membership_id = t2.membership_id and t1.Full_Names='janet jones'"
cursor.execute(sql)

for Full_Names, movie_rented in cursor:
    number += 1
    # print(number, "{}rented {}".format(Full_Names, Movies_Rented))
    print("{}".format(Full_Names))
    print( number,"{}".format(movie_rented)) 