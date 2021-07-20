# Konstruksi Dasar Python
# Squential : Eksekusi berurutan
print("Hello World")
print("By Eko")
print("Tangal 18 Juli 2021")
print("-" * 20)

#Percabangan : Eksekusi terpilih
ingin_cepat = True
if ingin_cepat:
    print("Jalan Lurus Saja")
else:
    print("Jalan lainnya")

jumlah_anak = 4

for index_anak in range(1,jumlah_anak+1): # jumlah_perulangan = 5 -1
    print(f"Halo anak ke {index_anak}")
