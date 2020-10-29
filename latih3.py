print ("Cek Status Kelulusan Mahasiswa")
print ("Range 0-100")

Ind = int(input("Masukkan Nilai Bahasa Indonesia:"))
Ipa = int(input("Masukkan Nilai IPA:"))
Mat = int(input("Masukkan Nilai Matematika:"))

if (Ind < 0) or (Ipa < 0) or (Mat < 0):
    print("Maaf Input Anda Tidak Valid")
elif (Ind >= 60) and (Ipa >= 60) and (Mat > 70):
    print("Status Kelulusan: LULUS")
else:
    print("Status Kelulusan: TIDAK LULUS")
    if(Ind < 60):
        print("Nilai Bahasa Indonesia Anda Dibawah KKM("+str(Ind)+")")
    if(Ipa < 60):
        print("Nilai IPA Anda Dibawah KKM("+str(Ipa)+")")
    if(Mat < 70):
        print("Nilai Matematika Anda Dibawah KKM("+str(Mat)+")")