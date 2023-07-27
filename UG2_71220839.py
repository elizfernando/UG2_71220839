def main():
    print("==================== KALKULATOR CERDAAS ====================")
    print("1. Tabung")
    print("2. Kubus")
    print("3. Balok")

import math
def VolumeTabung(jari_jari, tinggi):
    tabung = math.pi * jari_jari**2 *tinggi
    return tabung

def VolumeKubus(sisi):
    kubus = sisi**3
    return kubus

def VolumeBalok(panjang, lebar, tinggi):
    balok = panjang * lebar * tinggi
    return balok

pilihan_jenis = int(input("Masukkan pilihan bangun (1/2/3): "))

if pilihan_jenis == 1:
    jari_jari = float(input("Masukkan jari jari tabung: "))
    tinggi = float(input("Masukkan tinggi tabung: "))
    hasil = VolumeTabung(jari_jari, tinggi)
    print(f"Volume tabung adalah {hasil:.2f} cm")    
elif pilihan_jenis == 2:
    sisi = float(input("Masukkan sisi kubus: "))
    hasil = VolumeKubus(sisi)
    print(f"Volume kubus adalah {hasil:.2f} cm")
elif pilihan_jenis == 3:
    panjang = float(input("Masukkan panjang balok: "))
    lebar = float(input("Masukkan lebar balok: "))
    tinggi = float(input("Masukkan tinggi balok: "))
    hasil = VolumeBalok(panjang, lebar, tinggi)
    print(f"Volume balok adalah {hasil:.2f} cm")
else:
    print("Inputan yang anda masukkan salah !!")
