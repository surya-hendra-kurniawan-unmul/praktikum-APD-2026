barang_1 = 15000
barang_2 = 25000
barang_3 = 10000
barang_4 = 5500
barang_5 = 5000
barang_6 = 20000
usd = 17740
ringgit = 4326

barang = [barang_1, barang_2, barang_3, barang_4, barang_5, barang_6]
print("List barang         :", barang)

total_belanja = barang[0] + barang[1] + barang[2] + barang[3] + barang[4] + barang[5]
print("Total belanja       :", total_belanja)

pajak = total_belanja * 0.15
print("Pajak 15%           :", pajak)

total_bayar = total_belanja + pajak
print("Total bayar         :", total_bayar)

rata_rata = total_bayar / len(barang)
print("Rata-rata           :", rata_rata)

nim = 11
print("NIM                 :", nim)

bolean = nim < rata_rata
print("Bolean              :", bolean)

total_bayar_usd = total_bayar / usd
print("Total dalam USD     :$", total_bayar_usd)

total_bayar_ringgit = total_bayar / ringgit
print("Total dalam RINGGIT :RM", total_bayar_ringgit)
 
print("Barang 1, 3, 5      :", barang[0:5:2])
#bang, mba ini saya pakai tab supaya rapih di bagian "printnya" bukan karena AI :( 