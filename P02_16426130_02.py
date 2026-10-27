#NIM/Nama: 16426130
#Tanggal: 16 Oktober 2026
#Deskripsi Menentukan harga tiket masuk berdasarkan umur, tinggi badan, dan membership menggunakan if-else

#Variabel
HN = int(input("Masukkan harga tiket normal (Rp):"))
U = int(input("Masukkan umur pengunjung:"))
T = float(input("Masukkan tinggi pengunjung (m):"))
M = str(input("Apakah pengunjung member? (y/n):"))

#Algoritma penentuan harga berdasarkan kriteria
if (U < 4):
    HT = 0
elif (4 <= U <= 12):
    HT = HN*0.6
    if (T < 1.2):
        HT = HT - (HT*0.2)
elif (12 < U <= 60 ):
    HT = HN
elif (U > 60):
    HT = HN - (HN*0.5)
#pengurangan harga untuk member
if (HT >= 50000):
    HT -= 15000
#output
print(f"Biaya tiket yang harus dibayar adalah:Rp{HT}")
