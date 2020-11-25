jawab = True
while jawab:
        i = input("Tambah data (y/t) ? ")
        if i == ("t"):
            jawab = False
        else:

            nama = input("Nama        : ")
            nim = input("NIM         : ")
            tugas = int(input("Nilai Tugas : "))
            uts = int(input("Nilai UTS   : "))
            uas = int(input("Nilai UAS   : "))

            Uts = uts * 35 / 100;
            Uas = uas * 35 / 100;
            Tugas = tugas * 30 / 100;
            nilai_akhir = Uts + Uas + Tugas;

        
print("==============================================================")
print("| No |   Nama    |   NIM    | Tugas |  UTS  |  UAS  | Akhir |")
print("===============================================================")
print("| 1  |", nama, "|", nim, "|", tugas, "|", uts, "|", uas, "|", float(nilai_akhir), "|")
print("===============================================================")


