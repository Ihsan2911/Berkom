#16426130/Ihsanul Amin
#02 Oktober 2026
#membagi sembako kepada warga dengan pembagian bulat dan modulo

#kamus
#s=jumlah paket
#w=jumlah warga
#p=paket yang diterima warga
#x=sisa paket

#input variabel
s = int(input("Masukkan jumlah paket sembako:"))
w = int(input("Masukkan jumlah warga:"))

#perhitungan
p = s//w
x = s%w

#OUTPUT YG DIHASILKAN
print(f"Setiap warga mendapat {p} paket sembako dan paket yang bersisa adalah sebanyak {x} paket")

