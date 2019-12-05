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
class masukan_trigonometri :
    def __init__(self,derajat,pangkat):
        self.derajat = derajat
        self.pangkat = pangkat
       

    def nilai_sin(self):
        self.nilai_sin=math.pow(self.derajat,self.pangkat)
        return 'nilai sinya {}'.format(self.nilai_sin)



a=int(input('masukan derajat :'))
objek =masukan_trigonometri.nilai_sin(a,2)
objek.nilai_sin()
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



