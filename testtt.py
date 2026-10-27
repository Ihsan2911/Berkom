JL = str(input("Masukkan jenis layanan (Reguler/Kilat/Sameday:)"))
if (JL != "Reguler"):
    if (JL != "Kilat"):
        if (JL != "Sameday"):
            print("Jenis layanan tidak valid")
            exit()
B = int(input("Masukkan berat paket (kg):"))
JR = int(input("Masukkan jarak pengiriman (km):"))

if (JL == "Reguler"):
    if (JR <= 50):
        H = B*8000
    elif (51 <= JR < 150):
        H = B*12000
    else:
        H = B*18000
elif (JL == "Kilat"):
    if (JR <= 100):
        H = B*15000
        if (B > 10):
            H += 20000
    elif (JR > 100):
        H = B*25000
        if (B > 10):
            H += 20000
elif (JL == "Sameday"):
    if (JR <= 40):
        if (B <= 5):
            H = 30000
        else:
            H = 30000 + (B - 5)*6000
else:
    print("Jenis layanan tidak valid")
    exit()

AS = str(input("Gunakan asuransi? (y/n):"))

if (AS == "y"):
    NB = int(input("Masukkan nilai barang (Rp):"))
    if (NB > 1000000):
        HS = 15000
    else:
        HS = 5000
else:
    HS = 0
    
TH = H + HS
print(f"Total biaya pengiriman adalah: {TH}")
        