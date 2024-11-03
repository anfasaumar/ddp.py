jumlah_baris = int(input("Masukkan jumlah baris: "))

for i in range(1, jumlah_baris + 1):  # Change increment logic
    print(" " * (jumlah_baris - i) + "*" * (2 * i - 1))  # Format spacing and stars
