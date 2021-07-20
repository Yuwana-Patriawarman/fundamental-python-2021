"""
Tipe data dictionary sekedar menghubungkan KEY dan VALUE
KVP = Key Value Pair
Dictionary = Kamus
"""
from typing import Dict

kamus_eng_in = {"anak": "son", "istri": "wife", "bapak": "father", "ibu": "mother"}

print(kamus_eng_in)
print(kamus_eng_in['bapak'])
print(kamus_eng_in['ibu'])

print("\nData dikirimkan oleh server Gojek, untuk memberikan info driver disekitar pemakai aplikasi")
data_dari_server_gojek = {
    "tanggal" : "2021-07-21",
    "driver_list" : ["Eko", "Dwi", "Tri", "Catur"]
}
print(data_dari_server_gojek)
print(f"Driver sekitar sini {data_dari_server_gojek['driver_list']}")
print(f"Driver #1 {data_dari_server_gojek['driver_list'][0]}")
print(f"Driver #4 {data_dari_server_gojek['driver_list'][3]}")