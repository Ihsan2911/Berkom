#16426130/IhsanulAmin
#02 Oktober 2026
#menghitung upah total yang didapat dengan menghitung total waktu kerja yang dikalikan dengan upah kerja normal dan upah lembur

J1 =float(input("Masukkan jam masuk:"))
M1 =float(input("Masukkan menit masuk:"))
J2 =float(input("Masukkan jam keluar:"))
M2 =float(input("Masukkan menit keluar:"))
N =float(input("Masukkan menit normal kerja:"))
U =float(input("Masukkan upah per menit:"))
L =float(input("Masukkan pengali upah lembur:"))
M =float(input("Masukkan tunjangan makan:"))
TM =float(input("Masukkan minimal tunjangan (menit):"))

W = (J2*60 + M2) - (J1*60 + M1)

KL = W - N


UP = (N*U) + (KL*U*L)

print(f"Total durasi kerja(menit):{W}")
print(f"Menit kerja normal:{N}")
print(f"Menit kerja lembur:{KL}")

W >= M
print(f"Tunjangan makan sebesar:{M}")
print(f"Total upah diterima:{UP}")