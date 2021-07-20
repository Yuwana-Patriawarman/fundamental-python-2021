print("Tipe data List/daftar/Array")
anak = ["Eko", "Dwi", "Tri", "Catur"]
anak.append("Panca")
anak.append("Namnam")
print(anak)

print("\nsapa anak kedua")
print(f"Hai {anak[1]}")

print("\nsapa semua anak")
for a in anak:
    print (f"Hai {a}")

print("\nsapa semua anak cara ribet")
for a in range(0,len(anak)):
    print(f"{a+1}. Hai {anak[a]}")
