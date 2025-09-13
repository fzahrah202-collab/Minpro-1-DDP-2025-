#sistem manajemen jasa penitipan hewam

#List kosong untuk menampung data
hewan = []

print("===Data penitipan Hewan===")

#input data hewan yang dititipkan
nama = input("Masukkan nama hewan peliharaan anda   : ")
jenis = input("Masukkan jenis hewan peliharaan anda : ")
lama = input("Masukkan lama penitipan (hari)        : ")
hewan.append((nama, jenis, lama))


pilihan = input("Mau masukkan data lagi? (ya/tidak)  : ")

if pilihan == "ya" :

    #input data ke 2
    nama = input("Masukkan nama hewan peliharaan anda   : ")
    jenis = input("Masukkan jenis hewan peliharaan anda : ")
    lama = input("Masukkan lama penitipan (hari)        : ")
    hewan.append((nama, jenis, lama))

    pilihan = input("Mau masukkan data lagi? (ya/tidak)  : ")

    if pilihan == "ya" :

        #input data ke 3
        nama = input("Masukkan nama hewan peliharaan anda   : ")
        jenis = input("Masukkan jenis hewan peliharaan anda : ")
        lama = input("Masukkan lama penitipan (hari)        : ")
        hewan.append((nama, jenis, lama))

        #output data ke 3
        print("\ninput selesai data penuh (maksimal 3 hewan)")
        print("===Daftar hewan yang dititipkan===")
        print("1. Nama : ", hewan[0][0], " | Jenis : ", hewan[0][1], " | lama : ",hewan[0][2] )
        print("2. Nama : ", hewan[1][0], " | Jenis : ", hewan[1][1], " | lama : ",hewan[1][2] )
        print("3. Nama : ", hewan[2][0], " | Jenis : ", hewan[2][1], " | lama : ",hewan[2][2] )
        print("\nTerimakasih! hewan kesayanganmu siap kami rawat dengan penuh cinta🐶🐱🐰")

    else :
        
        #output data ke 2
        print("\ninput selesai, ada 2 hewan!")
        print("===Daftar hewan yang dititipkan===")
        print("1. Nama : ", hewan[0][0], " | Jenis : ", hewan[0][1], " | lama : ",hewan[0][2] )
        print("2. Nama : ", hewan[1][0], " | Jenis : ", hewan[1][1], " | lama : ",hewan[1][2] )
        print("\nTerimakasih! hewan kesayanganmu siap kami rawat dengan penuh cinta🐶🐱🐰")

else :

    #output data ke 1
    print("\ninput selesai, ada 1 hewan!")
    print("===Daftar hewan yang dititipkan===")
    print("1. Nama : ", hewan[0][0], " | Jenis : ", hewan[0][1], " | lama : ",hewan[0][2] )
    print("\nTerimakasih! hewan kesayanganmu siap kami rawat dengan penuh cinta🐶🐱🐰")

