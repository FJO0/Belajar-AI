j = '''
pada hari sEnin ini saya mempelajari python di startup Campus. pada
Modul kedua INI, saya mempelajari salah satu TIPE data yaitu STRing,
dimana sebuah STRINg dimulai dengan tanda petik (\") dan diakhiri juga
dengan Tanda petik (\").
'''

kecil = j.lower()
# string berubah menjadi list setelah menggunakan split
paragraf = kecil.split('.') 
hasil_list = []
for kalimat in paragraf:
    if kalimat.strip():  # Memastikan kalimat tidak kosong
        k = kalimat.strip().capitalize()
        hasil_list.append(k)

# Di luar loop: gabungkan semua kalimat dengan titik dan spasi
paragraf_utuh = '. '.join(hasil_list) + '.'
print(paragraf_utuh)