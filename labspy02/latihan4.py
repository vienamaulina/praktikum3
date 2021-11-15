def main():
    print('menentukan nilai terbesar dari tiga bilangan')
 
    a = int(input("masukan nilai pertama : "))
    b = int(input("masukan nilai kedua : "))
    c = int(input("masukan nilai ketiga : "))

    if a > b and a > c :
        max = a
    elif b > c  and b > c :
        max = b
    else:
        max = c

    print('Nilai Terbesar adalah %d' % max)
 
if __name__ == '__main__':
    main()