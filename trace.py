import numpy as np

def tracematriks():
    while True:
        print()
        print("---------------------------------------")
        print("SELAMAT DATANG DI PROGRAM TRACE MATRIKS")
        print("---------------------------------------")
        print()
        print("alert : untuk melakukan trace matriks maka matriks harus berordo n x n")
        print()

        row = int(input("masukkan jumlah ordo N = "))
        pengulang = row

        matriks = []

        count = 1

        while pengulang > 0:
            print(count, ". ", end="")
            inrow = input("masukkan angka perkolom pisahkan angka dengan spasi = ").split(" ")
            inrow = list(map(int, inrow))
            if len(inrow) != row:
                print("masukkan angka sesuai jumlah agar ordo matriks n x n.")
                continue
            else:
                matriks.append(inrow)
                pengulang -= 1
                count+=1

        matriks = np.array(matriks).trace()

        print()
        print("------------------------------------")
        print("hasil dari trace matriks adalah =",matriks)
        print("------------------------------------")
        
        print()
        lanjut = input('ketik "back" untuk kembali ke program utama dan enter bila masih ingin di program ini = ')
        if lanjut == "back":
            print("anda keluar dari program penjumlahan matriks")
            break
        else:
            continue