
print ("Mengurutkan data berdasarkan input jumlah data dari yang terkecil hingga terbesar" )

data = []
for i in range (5):
    x = int(input("masukan bilangan : "))
    data.append(x)
print ("data sebelum diurutkan : ",data)
list.sort(data)
print("data setelah diurutkan : ",data)