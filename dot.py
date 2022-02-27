import numpy as np

def dotmatriks():
    while True:
        print()
        print("-------------------------------------------")
        print("SELAMAT DATANG DI PROGRAM PERKALIAN MATRIKS")
        print("-------------------------------------------")
        print()
        print("alert : untuk mengalikan dua matriks pastikan jumlah kolom matriks 1 harus sama dengan jumlah baris matriks 2.")
        print()

        while True:
            row1 = int(input("masukkan jumlah baris matriks 1 = "))
            column1 = int(input("masukkan jumlah kolom matriks 1 = "))

            row2 = int(input("masukkan jumlah baris matriks 2 = "))
            column2 = int(input("masukkan jumlah kolom matriks 2 = "))

            if column1 != row2:
                print()
                print("matriks 1 memiliki jumlah kolom =", column1)
                print("matriks 2 memiliki jumlah baris =", row2)
                print()
                print("alert : untuk mengalikan dua matriks pastikan jumlah kolom matriks 1 harus sama dengan jumlah baris matriks 2.")
                continue
            else:
                break

        matriks1 = []
        matriks2 = []

        count1 = 1

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

        hasil = np.dot(matriks1, matriks2)

        print()
        print("------------------------------")
        print("HASIL PERKALIAN MATRIKS ADALAH")
        print("------------------------------")
        print()

        print(hasil)

        print()
        lanjut = input('ketik "back" untuk kembali ke program utama dan enter bila masih ingin di program ini = ')
        if lanjut == "back":
            print("anda keluar dari program perkalian matriks")
            break
        else:
            continue