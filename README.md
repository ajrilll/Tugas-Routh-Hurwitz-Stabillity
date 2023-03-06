# Tugas-Routh-Hurwitz-Stabillity
Nama : Danendra Azriel Ramdhany

NIM : 21/478295/PA/20739

Kode program tersebut merupakan implementasi algoritma Routh-Hurwitz dalam bahasa pemrograman Python. Algoritma ini digunakan untuk menentukan stabilitas suatu sistem dinamik berdasarkan persamaan polinomial karakteristiknya.

Pertama, program meminta pengguna untuk memasukkan koefisien polinomial sebagai string dan mengonversinya menjadi array numpy dengan tipe data float. Kemudian, program memanggil fungsi routh_hurwitz yang menghitung tabel Routh-Hurwitz menggunakan rumus yang diberikan dalam loop for. Tabel ini disimpan sebagai matriks numpy dan dicetak di layar.

Setelah tabel Routh-Hurwitz dibuat, program meminta pengguna untuk memasukkan faktor penguatan K. Berdasarkan tabel Routh-Hurwitz dan faktor penguatan K, program menentukan stabilitas sistem dan menampilkan pesan yang sesuai. Jika semua elemen pada kolom pertama tabel Routh-Hurwitz positif, maka sistem stabil. Jika semua elemen pada kolom pertama memiliki tanda yang sama, sistem tidak stabil. Jika ada elemen pada kolom pertama yang nol, sistem marginally stable. Dalam hal ini, program memberikan penjelasan lebih lanjut tentang stabilitas sistem.
