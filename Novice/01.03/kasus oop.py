class luas_bangun:
    def persegi (angka):
        print ("")
        luas =angka.sisi*angka.sisi
        print ("Luas Bangun Persegi Adalah :", luas )


    def persegi_panjang (angka):
        print ("")
        luas = angka.panjang*angka.lebar
        print ("Luas Bangun Persegi Panjang Adalah :",luas)
     
class nilai_persegi(luas_bangun) :
    def __init__(self):
        self.sisi = int(input("Masukan Sisi : "))

class nilai_persegi_panjang(luas_bangun) :
    def __init__(self):
        self.panjang = int(input("Masukan Panjang : "))
        self.lebar = int(input("Masukan Lebar : "))

'''
import math
class trigonometri :
    def  cari_nilai (derajat):
        print("")
        nilai_sin = math.sin(math.radians(derajat))
        print("Hasil dari perpangkatan derajat tersebut adalah :",nilai_sin)

class masukan_trigonometri (trigonometri):
    def __init__(self):
        self.derajat = int(input("masukan derajat :"))

objek = masukan_trigonometri()
objek.cari_nilai()
'''
print ("===============================")
print ("program sederhana ")
print ("1. luas bangun")
print ("2. keluar")
print ("===============================")
pilihan = int(input ("masukan pilihan : "))
print ("")
if (pilihan == 1):
    print ("===============================")
    print ("1. luas bangun persegi")
    print ("2. luas bangun persegi panang")
    print ("===============================")
    pilihan_luas = int (input ("masukan pilihan : "))
    print("")
    if (pilihan_luas == 1):
            objek = nilai_persegi()
            objek.persegi ()
    else:
            objek = nilai_persegi_panjang()
            objek.persegi_panjang()
else: 
    print ("|===============================|")
    print ("|  program telah berhenti ^-^   |")
    print ("|===============================|")



