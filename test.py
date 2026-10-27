R = int(input("Masukkan RAM (GB):"))
P = int(input("Masukkan penyimpanan (GB):"))

if (R >= 16):
    if (P >= 512):
        print("Layak")
    else:
        print(" Tidak layak (penyimpanan tidak memenuhi syarat)")
elif (R < 16):
    if (P >= 512):
        print("Tidak layak (RAM tidak memenuhi syarat)")
    else:
        print("Tidak layak (RAM dan penyimpanan tidak memenuhi syarat)")