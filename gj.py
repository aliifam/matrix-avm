import numpy as np
from fractions import Fraction

def gaussjordan():
    while True:
        print()
        print("------------------------------------------------------------------------------------------")
        print("SELAMAT DATANG DI PROGRAM PENYELESAIAN PERSAMAAN ALJABAR LINEAR DENGAN METODE GAUSS JORDAN")
        print("------------------------------------------------------------------------------------------")
        print()

        row = int(input("masukkan jumlah ordo N = "))
        pengulang = row

        matriks = [] #an linea algebra equal

        count = 1

        while pengulang > 0:
            print(count, ". ", end="")
            inrow = input("masukkan angka perkolom pisahkan angka dengan spasi = ").split(" ")
            inrow = list(map(int, inrow))
            if len(inrow) != row:
                print("masukkan angka sesuai jumlah agar ordo matriks yaitu", row, "x", row)
                continue
            else:
                matriks.append(inrow)
                pengulang -= 1
                count+=1
        
        while True:
            hasper = list(map(int, input("masukkan jawaban persamaan pisahkan dengan spasi = ").split(" ")))
            if len(hasper) != row:
                print("masukkan sesuai dengan jumlah persamaan linearnya.")
                continue
            else:
                break
        
        try:
            matriks = np.array(matriks)
            hasper = np.array(hasper)

            hasil = np.linalg.inv(matriks).dot(hasper)

            visual = []

            for i in range(1, row+1):
                temp = []
                for j in range(1, row+1):
                    if j == i:
                        temp.append(1)
                    else:
                        temp.append(0)
                visual.append(temp)
            
            visual = np.array(visual)

            nomor = 1

            print()
            print("-------------------------------------")
            print("HASIL OPERASI PERSAMAAN LINEAR ADALAH")
            print("-------------------------------------")
            print()

            print(hasil)
            for i in hasil:
                print("X", end="")
                print(nomor, "=", float(i))
                nomor+=1
            
            print("-------------------------------------")
            print(visual)
            print("-------------------------------------")
            print()
        except:
            print("-------------------------------------")
            print("sorry but no solution for that matrix")
            print("-------------------------------------")

        lanjut = input('ketik "back" untuk kembali ke program utama dan enter bila masih ingin di program ini = ')
        if lanjut == "back":
            print("anda keluar dari program pengurangan matriks")
            break
        else:
            continue