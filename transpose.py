import numpy as np 

def transposematriks():
    while True:
        print()
        print("-------------------------------------------")
        print("SELAMAT DATANG DI PROGRAM TRANSPOSE MATRIKS")
        print("-------------------------------------------")
        print()

        row = int(input("masukkan jumlah baris matriks = "))
        column = int(input("masukkan jumlah kolom matriks = "))

        matriks = []

        count = 1

        while row > 0:
            print(count, ". ", end="")
            inrow = input("masukkan angka perkolom pisahkan angka dengan spasi = ").split(" ")
            inrow = list(map(int, inrow))
            if len(inrow) != column:
                print("masukkan angka sesuai jumlah kolom")
                continue
            else:
                matriks.append(inrow)
                row -= 1
                count+=1
            

        matriks = np.array(matriks).T.tolist()

        print()
        print("------------------------------")
        print("HASIL OPERASI TRANSPOSE ADALAH")
        print("------------------------------")
        print()

        for i in matriks:
            print(i)
        
        print()
        lanjut = input('ketik "back" untuk kembali ke program utama dan enter bila masih ingin di program ini = ')
        if lanjut == "back":
            print("anda keluar dari program pengurangan matriks")
            break
        else:
            continue
        
