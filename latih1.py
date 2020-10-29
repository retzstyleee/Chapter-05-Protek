print("Cek Status Kelulusan Mahasiswa")
print("Range 0-100")

Indonesia = int(input("Masukkan Nilai Bahasa Indonesia:"))
Ipa = int(input("Masukkan Nilai IPA:"))
Mat = int(input("Masukkan Nilai Matematika:"))

if(Indonesia < 0) or (Ipa < 0) or (Mat <0):
    print("Maaf Input Anda Tidak Valid")
elif(Indonesia >= 60) and (Ipa >= 60) and (Mat > 70):
    print("Status Kelulusan : LULUS")
else:
    print("Status Kelulusan : TIDAK LULUS")