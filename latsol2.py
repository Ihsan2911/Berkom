w = float(input("Waktu keterlambatan (jam):"))
H = w//24
J = (w%24)//1
M = ((w%24) - (w%24)//1) * 60
D = (H*800000) + (J*25000) + ((M//5)*1000)
print(f"Terlambat {H} hari, {J} jam, dan {M} menit")
print(f"Denda yang harus dibayar (Rp): {D}")