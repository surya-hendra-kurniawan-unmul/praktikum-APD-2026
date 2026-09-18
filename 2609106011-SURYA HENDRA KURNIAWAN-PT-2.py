barang_1 = 15000
barang_2 = 25000
barang_3 = 10000
barang_4 = 5500
barang_5 = 5000
barang_6 = 20000
barang_7 = 12345
usd = 17740
ringgit = 4326

barang = [barang_1, barang_2, barang_3, barang_4, barang_5, barang_6]

total_belanja = barang[0] + barang[1] + barang[2] + barang[3] + barang[4] + barang[5]

pajak = total_belanja * 0.15

total_bayar = total_belanja + pajak

rata_rata = total_bayar / len(barang)

nim = 11

bolean = nim < rata_rata

total_belanja_usd = total_belanja / usd
total_belanja_ringgit = total_belanja / ringgit

print("List barang         :", barang)
print("Total belanja       :", total_belanja)
print("Pajak 15%           :", pajak)
print("Total bayar         :", total_bayar)
print("Rata-rata           :", rata_rata)
print("NIM                 :", nim)
print("Bolean              :", bolean)
print("Total dalam USD     :$", total_belanja_usd)
print("Total dalam RINGGIT :RM", total_belanja_ringgit)
print("Barang 1, 3, 5      :", barang[0:5:2])
