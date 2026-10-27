#NIM/Nama: 16426130/Ihsanul Amin
#Tanggal: 16 Oktober 2026
#Deskripsi:Menghitung kWh maksimum yang dapat digunakan sesuai dengan anggaran yang tersedia


AM = int(input("Masukkan anggaran maksimum (Rp):"))
S = str(input("Apakah pelanggan subsidi? (y/n):"))
WT = int(input("Masukkan lama menunggak (hari):"))

if (WT > 30):
    D = 100000
elif (1 < WT <= 30):
    D = 25000
else:
    D = 0

A = AM - D



if (A <= 100000):
    KM = A // 1000
    if (S == "y"):
        HT = KM*1000 + (KM*1000)*0.3
        KM = HT // 1000
        print(f"Pemakaian maksimal yang bisa dipakai: {KM} kWh")
    else:
        print(f"Pemakaian maksimal yang bisa dipakai:{KM} kWh")
elif (100000 < A < (380000)):
    KM = 100 + ((A - 100000) // 1400)
    if (S == "y"):
        HT = 100000 + ((KM - 100)*1400) + ((100000 + ((KM - 100)*1400))*0.3)
        KM = 100 + ((HT - 100000) // 1400)
        print(f"Pemakaian maksimal yang bisa dipakai:{KM} kWh")
    else:
        print(f"Pemakaian maksimal yang bisa dipakai:{KM} kWh")
else:
    KM = 300 + ((A - 380000)) // 1800
    if (S == "y"):
        HT = 380000 + (A - 380000)*1800 +(380000 + (A - 380000)*1800)*0.3
        KM = 300 + (HT - 380000) // 1800
        print(f"Pemakaian maksimal yang bisa dipakai:{KM} kWh")
    else:
        print(f"Pemakaian maksimal yang bisa dipakai:{KM} kWh")

