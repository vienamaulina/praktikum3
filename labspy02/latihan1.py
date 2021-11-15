
print ("Program Menentukan Nilai Akhir")
nama = input("Masukkan Nama :")
uts = input("Masukkan Nilai UTS :")
uas = input("Masukkan Nilai UAS :")
tugas = input("Masukkan Nilai Tugas :")
akhir = (int(tugas) * .2) + (int(uts) * .4) + (int(uas) * .4)
keterangan = ("TIDAK LULUS", "LULUS")[akhir > 60.0]
if akhir > 80:
 huruf = "A"
elif akhir > 70:
 huruf = "B"
elif akhir > 50:
 huruf = "C"
elif akhir > 40:
 huruf = "D"
else:
 huruf = "E"
print("\nNama : ",nama)
print("Nilai UTS : ",uts)
print("Nilai UAS : ",uas)
print("Nilai Tugas : ",tugas)
print("Nilai Akhir : ",akhir)
print("\nNilai Huruf : ",huruf)
print("Keterangan : ",keterangan)