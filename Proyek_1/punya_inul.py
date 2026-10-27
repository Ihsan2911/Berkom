from inputimeout import inputimeout, TimeoutOccurred

TH = int(input("Total Harga (Rp):"))
Status_Berjalan = True

while Status_Berjalan:
    print("Silakan Lakukan Pmebayaran")
    Pembayaran_Sukses = False
    while not Pembayaran_Sukses:
        try:
            BB_input = inputimeout (prompt="Scan QRIS di sini: ", timeout=60)
            BB = int(BB_input)
            if (BB == TH):
                ST = 1
                print ("Pembayaran Berhasil!")
                Status_Berjalan = False
                Pembayaran_Sukses = True
            elif (BB < TH):
                ST = 0
                print ("Nominal yang Anda bayarkan tidak cukup")
        except TimeoutOccurred:
            print("\n[Waktu Habis] Sesi pembayaran dibatalkan karena waktu habis.")
            

if (ST == 1):
    print("\n =====STRUK PEMBELIAN=====)
    total = 0
    for item in keranjang:
       nama = item["produk"]["nama"]
       jumlah = item["jumlah"]
       subtotal = item["produk"][harga] * jumlah
       total += subtotal
       print(f"{nama} x{jumlah} = {rupiah(subtotal)}")
    
    print("-" * 30)
    print("Tota: ", rupiah(total))      