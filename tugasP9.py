import random

# Membuat data awal
data = random.sample(range(1, 100), 20)
data.sort()


# Binary Search Iterative
def binary_search_iterative(arr, target):
    kiri = 0
    kanan = len(arr) - 1

    while kiri <= kanan:
        tengah = (kiri + kanan) // 2

        if arr[tengah] == target:
            return tengah
        elif arr[tengah] < target:
            kiri = tengah + 1
        else:
            kanan = tengah - 1

    return -1


# Binary Search Recursive
def binary_search_recursive(arr, target, kiri, kanan):
    if kiri > kanan:
        return -1

    tengah = (kiri + kanan) // 2

    if arr[tengah] == target:
        return tengah
    elif arr[tengah] < target:
        return binary_search_recursive(arr, target, tengah + 1, kanan)
    else:
        return binary_search_recursive(arr, target, kiri, tengah - 1)


# Menu
def menu():
    global data  # ✅ dipindah ke sini (awal fungsi)

    while True:
        print("\n=== PROGRAM BINARY SEARCH ===")
        print("1. Tampilkan Data")
        print("2. Cari (Iterative)")
        print("3. Cari (Recursive)")
        print("4. Acak Ulang Data")
        print("5. Keluar")

        pilihan = input("Pilih menu (1-5): ")

        if pilihan == "1":
            print("\nData:", data)

        elif pilihan == "2":
            try:
                target = int(input("Masukkan angka yang dicari: "))
                hasil = binary_search_iterative(data, target)

                if hasil != -1:
                    print(f"Data ditemukan di indeks ke-{hasil}")
                else:
                    print("Data tidak ditemukan")
            except:
                print("Input harus angka!")

        elif pilihan == "3":
            try:
                target = int(input("Masukkan angka yang dicari: "))
                hasil = binary_search_recursive(data, target, 0, len(data) - 1)

                if hasil != -1:
                    print(f"Data ditemukan di indeks ke-{hasil}")
                else:
                    print("Data tidak ditemukan")
            except:
                print("Input harus angka!")

        elif pilihan == "4":
            data = random.sample(range(1, 100), 20)
            data.sort()
            print("Data berhasil diacak dan diurutkan ulang!")

        elif pilihan == "5":
            print("Program selesai.")
            break

        else:
            print("Pilihan tidak valid!")


# Menjalankan program
menu()
