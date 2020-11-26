daftar_mahasiswa = {'nama':'ari', 'nim':'2323', 'tugas':'80', 'uts':'90', 'uas':'85'}

print("Program input nilai")
print("===================")

tambah = True
while tambah:
    tambahkan = input("(L)ihat, (T)ambah, (U)bah, (H)apus, (C)ari, (K)eluar : ")
    if tambahkan == "l":
        tambah = False
    else:
        print("Tambah data")
        daftar_semua = daftar_mahasiswa.items()
        for k, v in daftar_semua:
            print(f'{k} : {v}')

            Tugas = int(daftar_mahasiswa['tugas']) * 35 / 100
            Uts = int(daftar_mahasiswa['uts']) * 30 / 100
            Uas = int(daftar_mahasiswa['uas']) * 30 / 100
            nilai_akhir = Tugas + Uts + Uas

print("Daftar Nilai")
print("=======================================================")
print("| No | Nama  |  NIM   | Tugas |  UTS  |  UAS  | Akhir |")
print("=======================================================")
print("| 1  |", daftar_mahasiswa['nama'], "|", daftar_mahasiswa['nim'], "|", \
      daftar_mahasiswa['tugas'], "|", daftar_mahasiswa['uts'], "|", daftar_mahasiswa['uas'], "|", float(nilai_akhir), "|")
print("=======================================================")


