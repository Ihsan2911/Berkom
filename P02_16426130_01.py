
#NIM/Nama: 16426130/Ihsanul Amin
#Tanggal 16 Oktober 2026
#Deskripsi: Menentukan apakah Pak Mik mendapat diskon atau ditak dengan menggunakan if-else

M = str(input("Apakah member? (y/n):"))
T = int(input("Masukkan total belanja (Rp):"))

if (M == "y"):
    print("Tuan Mik dapat diskon!")
elif (T > 200000):
    print("Tuan Mik dapat diskon!")
else:
    print("Tuan Mik tidak dapat diskon")