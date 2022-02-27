import numpy as np 

def inversmatriks():
    while True:
        print()
        print("----------------------------------------")
        print("SELAMAT DATANG DI PROGRAM INVERS MATRIKS")
        print("----------------------------------------")
        print()
        print("alert : matriks dikatakan memiliki invers jika determinan dari matriks tersebut tidak sama dengan nol dan matriks harus berordo N x N agar memiliki determinan.")
        print()

        row = int(input("masukkan jumlah ordo N = "))

        matriks = []

        while True:

            pengulang = row

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
                    
            determinan = np.array(matriks)
            determinan = np.linalg.det(matriks)

            if determinan == 0:
                print("determinan matriks = ", determinan)
                print("kalau hasilnya", determinan, "maka tidak bisa diinvers")
                continue
            else:
                break

        matriks = np.array(matriks)

        print()
        print("-------------------------")
        print("MATRIKS SEBELUM DI INVERS")
        print("-------------------------")
        print()

        print(matriks)


        matriks = np.linalg.inv(matriks)

        print()
        print("---------------------------")
        print("HASIL INVERS MATRIKS ADALAH")
        print("---------------------------")
        print()

        print(matriks)

        print()
        lanjut = input('ketik "back" untuk kembali ke program utama dan enter bila masih ingin di program ini = ')
        if lanjut == "back":
            print("anda keluar dari program pengurangan matriks")
            break
        else:
            continue