R = int(input("Masukkan uang (Rp):"))
H = int(input("Masukkan harga (Rp):"))
K = R-H
if K>0:
  print("Kembalian:Rp" + str(K))
elif K==0:
  print("Uang pas")
else:
  print(f"Uang kurang {-K}")

LP = K//50000
Sisa1 = K - (LP*50000)
DP = Sisa1//20000
Sisa2 = Sisa1 - (DP*20000)
SP = Sisa2//10000
Sisa3 = Sisa2 - (SP*10000)
LR = Sisa3//5000
Sisa4 = Sisa3 - (LR*5000)
SR = Sisa4//1000
print(f"Berikan Rp 50.000 {LP} lembar, Rp 20.000 {DP} lembar, Rp 10.000 {SP} lembar, Rp 5.000 {LR} lembar, dan Rp 1.00 {SR} lembar")