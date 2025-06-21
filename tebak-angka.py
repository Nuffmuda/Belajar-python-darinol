import random

angka_rahasia = random.randint(1, 100)
tebakan = 0
jumlah_tebakan = 0

print("=== Game Tebak Angka ===")
print("Tebak angka dari 1 sampai 100!")

while tebakan != angka_rahasia:
    try:
        tebakan = int(input("Masukkan tebakan kamu: "))
        jumlah_tebakan += 1

        if tebakan < angka_rahasia:
            print("Terlalu kecil!")
        elif tebakan > angka_rahasia:
            print("Terlalu besar!")
        else:
            print(f"🎉 Selamat! Kamu berhasil menebak dalam {jumlah_tebakan} kali.")
    except ValueError:
        print("Masukkan angka yang valid!")