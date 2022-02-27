from instruksi import printinstruksi
from tambah import tambahmatriks
from kurang import kurangmatriks
from dot import dotmatriks
from trace import tracematriks
from transpose import transposematriks
from determinan import determinanmatriks
from invers import inversmatriks
from gj import gaussjordan

while True:
    printinstruksi()
    pilpro = input("masukkan salah satu instruksi program = ")
    if pilpro == "exit":
        print("terimakasih, tekan enter sekali lagi untuk menutup program")
        temp = input()
        break
    elif pilpro == "1":
        tambahmatriks()
    elif pilpro == "2":
        kurangmatriks()
    elif pilpro == "3":
        dotmatriks()
    elif pilpro == "4":
        tracematriks()
    elif pilpro == "5":
        transposematriks()
    elif pilpro == "6":
        determinanmatriks()
    elif pilpro == "7":
        inversmatriks()
    elif pilpro == "8":
        gaussjordan()
    else:
        print("masukkan instruksi program yang tersedia")
