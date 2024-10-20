import os

clearconsole = lambda: os.system('cls')
from datetime import datetime

now = datetime.now().strftime("%d-%m-%Y %I:%M %p")

def print_stok(Stok):
    print("==============================")
    for pilihan in Stok: 
        item = Stok[pilihan]
        print(f"{pilihan}. {item[0]} : Rp. {item[1]}")
    
    print("(-) Kembali")
    print("==============================")

def tampilkan_menu_utama(barang_dipilih):
    print("""
    ==============================
    
                T MART
             Pilihan Menu 
 
    ==============================
    A. Menu Makanan
    B. Menu Minuman
    C. Menu Kebutuhan Lainnya
    """ + ('D. Pembayaran\n' if barang_dipilih else 'D. Pembayaran\n    E. Keluar\n') +
        """==============================
    """)

def input_barang(stok, total_pembelian, jumlahArray):
    while True:
        clearconsole()
        print_stok(stok)

        pilihan = input("Pilihan anda? ").upper()

        if pilihan == "-":
            break

        if pilihan not in stok:
            pilihan = input("Pilihan anda tidak ada di menu silakan coba lagi : ").upper()

        jumlah = int(input("Silakan masuk jumlah yang ingin anda beli : "))
        jumlahArray.append(jumlah);


        total_pembelian.append([stok[pilihan], jumlah])
    

def print_pembayaran(total_pembelian, jumlahArray):
    print("""\n
                    T MART
               Telkom University
             Jl.Telekomunikasi No.1
                    Bandung 
        --------------------------------""")
    total_jumlah = 0 
    jumlah_list = len(total_pembelian)       
    x = sum(jumlahArray)
    for pembelian in total_pembelian:
        item = pembelian[0][0]
        jumlah = pembelian[1]
        harga = pembelian[0][1]
        total_jumlah += (jumlah * harga)
        print(f"        {item}")
        print(f"                {jumlah} pcs          Rp. {harga} ")
    print(f"        -----------------------------(+)")
    print(f"        Total Item    :              {jumlah_list}")
    print(f"        Total QTY     :              {x}")
    print(f"        Total HRG     :      Rp. {total_jumlah}")
    print("        -----------PEMBAYARAN-----------")
    print(f"        CASH          :      Rp. {total_jumlah}")
    print(f"        TOTAL BAYAR   :      Rp. {total_jumlah}")
    print(f"        --------------------------------")

    

    while True:
        uang_bayar = int(input('        JUMLAH BAYAR  :      Rp. '))
        if uang_bayar >= total_jumlah:
            kembalian = uang_bayar - total_jumlah
            print(f'        KEMBALIAN     :      Rp. {kembalian}')
            print(f"\n       {now}")
            print(f"        Pelanggan     : N/A")
            print(f"        kasir         : N/A")
            print(f"        Staff         : N/A")
            print(f"\n                  Terimakasih")
            print(f"                 Semoga Berkah")
            break
        else:
            print('        Jumlah uang yang dimasukkan kurang dari total harga. Mohon masukkan jumlah yang cukup.')

def main(): 
    StokMakanan = {
        "A": ["Chitato", 11_000],
        "B": ["Maitos", 12_000],
        "C": ["Maxcorn", 11_800],
        "D": ["waffer Selamat", 15_000],
        "E": ["Waffer Tango", 15_500],
        "F": ["Oreo", 10_500],
        "G": ["Biskuit Kelapa Cream", 12_000],
        "H": ["Ritz", 10_500],
        "I": ["Saltcheese", 12_500],
        "J": ["Malkist", 6_200]
    }

    StokMinuman = {
        "A": ["Fruit Tea", 4_500],
        "B": ["Garantea", 4_500],
        "C": ["Nui Green Tea", 6_500],
        "D": ["Frestea (kecil)", 4_800],
        "E": ["Frestea (besar)", 6_500],
        "F": ["Sprite", 5_600],
        "G": ["Coca Cola", 6_300],
        "H": ["Fanta", 5_000],
        "I": ["Aqua", 4_000],
        "J": ["Le Minerale", 3_700]
    }

    Stoklain = {
        "A": ["Minyak Bimoli", 45_500],
        "B": ["Minyak Fortune", 36_500],
        "C": ["Minyak Sania", 37_500],
        "D": ["Minyak Bimoli", 42_800],
        "E": ["Kopi Kapal Api (Sachet)", 11_300],
        "F": ["Kopi Gadjah", 12_000],
        "G": ["Kopi ABC", 14_500],
        "H": ["teh tong tji", 14_000],
        "I": ["teh sariwangi", 6_000],
        "J": ["teh poci", 7_700]
    }

    jumlahArray = []
    total_pembelian = []
    barang_dipilih = False

    while True:
        clearconsole()
        tampilkan_menu_utama(barang_dipilih)
        menu = input("Pilihan anda? ").upper()

        if menu == "A":
            barang_dipilih = True
            input_barang(StokMakanan, total_pembelian, jumlahArray)

        elif menu == "B":
            barang_dipilih = True
            input_barang(StokMinuman, total_pembelian, jumlahArray)

        elif menu == "C":
            barang_dipilih = True
            input_barang(Stoklain, total_pembelian, jumlahArray)

        elif menu == "D":
            clearconsole()
            if not total_pembelian:
                print("Anda belum memilih barang. Silakan pilih barang terlebih dahulu.")
            else:
                print_pembayaran(total_pembelian, jumlahArray)
                total_pembelian = []
                barang_dipilih = False
                break

        elif menu == "E":
            print('terimakasih sudah datang ke T MART')
            break
        else:
            print("Pilihan anda tidak ada!")

main()