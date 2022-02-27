import numpy as np

def tambahmatriks():
    while True:
        print()
        print("---------------------------------------------")
        print("SELAMAT DATANG DI PROGRAM PENJUMLAHAN MATRIKS")
        print("---------------------------------------------")
        print()
        print("alert : syarat dua matriks dapat dijumlahkan yaitu keduanya harus memiliki ordo yang sama")
        print()

        while True:
            row1 = int(input("masukkan jumlah baris matriks 1 = "))
            column1 = int(input("masukkan jumlah kolom matriks 1 = "))

            row2 = int(input("masukkan jumlah baris matriks 2 = "))
            column2 = int(input("masukkan jumlah kolom matriks 2 = "))

            if column1 != column2 or row1 != row2:
                print()
                print("matriks 1 memiliki jumlah kolom =", column1)
                print("matriks 1 memiliki jumlah baris =", row1)
                print("matriks 2 memiliki jumlah kolom =", column2)
                print("matriks 2 memiliki jumlah baris =", row2)
                print()
                print("alert : untuk menjumlahkan dua matriks pastikan keduanya memiliki ordo metriks yang sama")
                continue
            else:
                break

        matriks1 = []
        matriks2 = []

        count1 = 1
        print("----------------------------------------------")
        print("                  MATRIKS 1")
        print("----------------------------------------------")
        while row1 > 0:
            print(count1, ". ", end="")
            inrow = input("masukkan angka perbaris matriks 1 pisahkan angka dengan spasi = ").split(" ")
            inrow = list(map(int, inrow))
            if len(inrow) != column1:
                print("masukkan angka sesuai jumlah kolom dalam satu baris matriks 1")
                continue
            else:
                matriks1.append(inrow)
                row1 -= 1
                count1+=1

        print()

        count2 = 1
        print("----------------------------------------------")
        print("                  MATRIKS 2")
        print("----------------------------------------------")
        while row2 > 0:
            print(count2, ". ", end="")
            inrow = input("masukkan angka perbaris matriks 2 pisahkan angka dengan spasi = ").split(" ")
            inrow = list(map(int, inrow))
            if len(inrow) != column2:
                print("masukkan angka sesuai jumlah kolom dalam satu matriks 2")
                continue
            else:
                matriks2.append(inrow)
                row2 -= 1
                count2+=1

        hasil = np.add(matriks1, matriks2)

        print()
        print("--------------------------------")
        print("HASIL PENJUMLAHAN MATRIKS ADALAH")
        print("--------------------------------")
        print()

        print(hasil)
        print()
        lanjut = input('ketik "back" untuk kembali ke program utama dan enter bila masih ingin di program ini = ')
        if lanjut == "back":
            print("anda keluar dari program penjumlahan matriks")
            break
        else:
            continue