#16426130/IhsanulAmin
#02 Oktober 2026
#Menghitung minimal nilau UAS agar mencapai target

#input variabel
X = float(input("Masukkan nilai tugas:"))
Y = float(input("Masukkan nilai praktikum:"))
Z = float(input("Masukkan nilai UTS:"))

XT = float(input("Masukkan bobot nilai tugas(%):"))
YP = float(input("Masukkan bobot nilai  praktikum(%):"))
ZU = float(input("Masukkan bobot nilai UTS(%):"))
NU = 100 - XT - YP - ZU #bobot nilai UAS
N = float(input("Berapa target nilaimu?:"))
#perhitungan nilai minimal
NM = ( N - ((X*XT/100) + (Y*YP/100) + (Z*ZU/100)))/(NU/100) 


print(f"Minimal nilau UAS yang harus kamu dapatkan adalah: {NM}")