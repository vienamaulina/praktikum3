print ("Menampilkan bilangan terbesar dari n buah data yang diinputkan.")

max = 0
while True:
    a=int(input("masukan bilangan :"))
    if max < a:
        max = a
    if a ==0:
        break
print ("\n bilangan terbesar adalah :", max)