print("\n       Gaji Karyawan")
print("\n ===========================")

kode = input("\nMasukkan Kode Karyawan : ")
nama = input("Masukkan Nama Karyawan : ")
gol = input("Masukkan Golongan Karyawan (A-D) : ")

print ("\n==========================")
print ("\nSTRUCK RINCIAN GAJI KARYAWAN")
print ("\n--------------------------")
print ("\nNama Karyawan : "+str(nama)+" (kode: "+str(kode)+")")
print ("Golongan : "+str(gol))

if (gol == "A"):
    gajiPokok = 10000000
    potongan = round(0.025 * gajiPokok)
elif (gol == "B"):
    gajiPokok = 8500000
    potongan = round(0.02 * gajiPokok)
elif (gol == "C"):
    gajiPokok = 7000000
    potongan = round(0.015 * gajiPokok)
elif (gol == "D"):
    gajiPokok = 550000
    potongan = round(0.01 * gajiPokok)
elif (gol != "A") or (gol != "B") or (gol != "C") or (gol != "D"):
    print ("Golongan Tidak Ditemukan")
    exit()
print ("\n---------------------------")
print ("Gaji Pokok : Rp " +str(gajiPokok))
print ("Potongan : Rp " +str(potongan))
print ("\n---------------------------")
print ("Gaji Bersih : Rp " +str(gajiPokok - potongan))