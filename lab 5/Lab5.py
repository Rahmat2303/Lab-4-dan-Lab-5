print("Program input nilai")
print("===================")

tambah = True
while tambah:
    tambahkan = input("(L)ihat, (T)ambah, (U)bah, (H)apus, (C)ari, (K)eluar : ")
    if tambahkan == "l":
        tambah = False
    else:
        print("Tambah Data")
        nama = input("Nama        : ")
        nim = input("NIM         : ")
        tugas = int(input("Nilai Tugas : "))
        uts = int(input("Nilai UTS   : "))
        uas = int(input("Nilai UAS   : "))

        Uts = uts * 35 / 100;
        Uas = uas * 35 / 100;
        Tugas = tugas * 30 / 100;
        nilai_akhir = Uts + Uas + Tugas

print("Daftar Nilai")
print("=============================================================")
print("| No |   Nama    |   NIM    | Tugas |  UTS  |  UAS  | Akhir |")
print("=============================================================")
print("| 1  |", nama, "|", nim, "|", tugas, "|", uts, "|", uas, "|", float(nilai_akhir), "|")
print("=============================================================")


