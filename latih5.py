print ("\n		Gaji Karyawan				")
print ("\n==============================================")

kode = input("\nMasukkan Kode Karyawan 	         : ")       
nama = input("Masukkan Nama karyawan 	         : ")
gol  = input("Masukkan Golongan Karyawan (A-D) : ")
status = input("Masukkan Status (1. Menikah 2. Belum) : ")

if (status == "1"):
		anak = int(input("Masukkan Jumlah Anak : "))
elif (status == "2"):
		anak = 0

print ("\n==============================================")
print ("\n	 STRUK RINCIAN GAJI KARYAWAN")
print ("\n----------------------------------------------")
print ("\nNama karyawan 	: " +str(nama)+ " (Kode: " +str(kode)+ ")")
print ("Golongan 	: " +str(gol))
if (gol == "A"):
	gajiPokok = 10000000
	potongan   = round(0.025 * gajiPokok)
elif (gol == "B"):
	gajiPokok = 8500000
	potongan   = round(0.02 * gajiPokok)
elif (gol == "C"):
	gajiPokok = 7000000
	potongan   = round(0.015 * gajiPokok)
elif (gol == "D"):
	gajiPokok = 5500000
	potongan   = round(0.01 * gajiPokok)
print ("Status Menikah  : " +str(status))
if (status == "1"):
	print ("Jumlah Anak     : " +str(anak))
elif (status == "2"):
	anak = 0
# print ("Jumlah Anak    : " +str(anak))
print ("\n----------------------------------------------")

if (gol == "A") and (status == "1") or (status == "2"):
	# gajiPokok  = 10000000
	# potongan   = round(0.025 * gajiPokok)
	if (status == "1"):
		tunMenikah = round(0.1 * gajiPokok)
	elif (status == "2"):
		tunMenikah = 0
	tunAnak1   = round(anak * 0.05 * gajiPokok)
	gajiKotor  = (gajiPokok + tunMenikah + tunAnak1)
	gajiBersih = (gajiKotor - potongan)
	print ("\nGaji Pokok 		= Rp " +str(gajiPokok))
	if (status == "1"):
		print ("Tunjangan Istri / Suami = Rp " +str(tunMenikah))
	elif (status == "2"):
		tunMenikah = 0
	if (status == "1"):
		print ("Tunjangan Anak	  	= Rp " +str(tunAnak1))
	elif (status == "2"):
		tunAnak = 0
	print ("\n----------------------------------------------")
	print ("Gaji Kotor = Rp " +str(gajiKotor))
	print ("Potongan   = Rp " +str(potongan))
	print ("\n----------------------------------------------")
	print ("\nGaji Bersih = Rp " +str(gajiBersih))

elif (gol == "B") and (status == "1") or (status == "2"):
	# gajiPokok  = 8500000
	# potongan   = round(0.02 * gajiPokok)
	if (status == "1"):
		tunMenikah = round(0.1 * gajiPokok)
	elif (status == "2"):
		tunMenikah = 0
	tunAnak1   = round(anak * 0.05 * gajiPokok)
	gajiKotor  = (gajiPokok + tunMenikah + tunAnak1)
	gajiBersih = (gajiKotor - potongan)
	print ("\nGaji Pokok 		= Rp " +str(gajiPokok))
	if (status == "1"):
		print ("Tunjangan Istri / Suami = Rp " +str(tunMenikah))
	elif (status == "2"):
		tunMenikah = 0
	if (status == "1"):
		print ("Tunjangan Anak	  	= Rp " +str(tunAnak1))
	elif (status == "2"):
		tunAnak = 0
	print ("\n----------------------------------------------")
	print ("Gaji Kotor = Rp " +str(gajiKotor))
	print ("Potongan   = Rp " +str(potongan))
	print ("\n----------------------------------------------")
	print ("\nGaji Bersih = Rp " +str(gajiBersih))

elif (gol == "C") and (status == "1") or (status == "2"):
	# gajiPokok  = 7000000
	# potongan   = round(0.015 * gajiPokok)
	if (status == "1"):
		tunMenikah = round(0.1 * gajiPokok)
	elif (status == "2"):
		tunMenikah = 0
	tunAnak1   = round(anak * 0.05 * gajiPokok)
	gajiKotor  = (gajiPokok + tunMenikah + tunAnak1)
	gajiBersih = (gajiKotor - potongan)
	print ("\nGaji Pokok 		= Rp " +str(gajiPokok))
	if (status == "1"):
		print ("Tunjangan Istri / Suami = Rp " +str(tunMenikah))
	elif (status == "2"):
		tunMenikah = 0
	if (status == "1"):
		print ("Tunjangan Anak	  	= Rp " +str(tunAnak1))
	elif (status == "2"):
		tunAnak = 0
	print ("\n----------------------------------------------")
	print ("Gaji Kotor = Rp " +str(gajiKotor))
	print ("Potongan   = Rp " +str(potongan))
	print ("\n----------------------------------------------")
	print ("\nGaji Bersih = Rp " +str(gajiBersih))
elif (gol == "D") and (status == "1") or (status == "2"):
	# gajiPokok  = 5500000
	# potongan   = round(0.01 * gajiPokok)
	if (status == "1"):
		tunMenikah = round(0.1 * gajiPokok)
	elif (status == "2"):
		tunMenikah = 0
	tunAnak1   = round(anak * 0.05 * gajiPokok)
	gajiKotor  = (gajiPokok + tunMenikah + tunAnak1)
	gajiBersih = (gajiKotor - potongan)
	print ("\nGaji Pokok 		= Rp " +str(gajiPokok))
	if (status == "1"):
		print ("Tunjangan Istri / Suami = Rp " +str(tunMenikah))
	elif (status == "2"):
		tunMenikah = 0
	if (status == "1"):
		print ("Tunjangan Anak	  	= Rp " +str(tunAnak1))
	elif (status == "2"):
		tunAnak = 0
	print ("\n----------------------------------------------")
	print ("Gaji Kotor = Rp " +str(gajiKotor))
	print ("Potongan   = Rp " +str(potongan))
	print ("\n----------------------------------------------")
	print ("\nGaji Bersih = Rp " +str(gajiBersih))
elif  (gol != "A") or (gol != "B") or (gol != "C") or (gol != "D"):
	print ("\nGolongan Tidak Ditemukan")
	exit()