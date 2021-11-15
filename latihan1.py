def main():
    print('menentukan nilai terbesar dari dua bilangan')
 
    a = int(input("masukan nilai pertama: "))
    b = int(input("masukan nilai kedua: "))

    if a > b:
        max = a
    else:
        max = b
    # mencetak nilai maksimum
    print('Nilai Terbesar adalah %d' % max)
 
if __name__ == '__main__':
    main()