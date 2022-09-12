# Penjelasan Tugas 2 PBP

## Identitas
Nama    : Jaycent Gunawan Ongris<br>
NPM     : 2106750231<br>
Kelas   : F

## Link Hasil Deploy
Link untuk menuju ke web yang sudah di-deploy dapat diklik di [sini](https://tugas-pbp-2.herokuapp.com/katalog/).

## Jawaban dari Pertanyaan
### Bagan *Request Client*
![bagan](https://user-images.githubusercontent.com/88029772/189681692-6527e06e-05f8-490f-86f6-c6c076742bd2.png)
Penjelasan terkait bagan tersebut adalah sebagai berikut.
1. *Client* akan melakukan *request*.
2. *Request* yang masuk akan diproses pada `urls.py` berdasarkan *routes* yang ada di `urlpatterns`.
3. *Request* lalu diproses pada `views.py` oleh fungsi-fungsi yang terkait.
4. Jika perlu untuk mengakses *database*, `views.py` ini akan memanggil *query* ke `models.py` yang terhubung dengan *database*.
5. *Database* akan memberikan respons data yang merupakan hasil pemanggilan *query* ke `views.py`.
6. Respons data yang sudah didapatkan kemudian dipetakan ke berkas HTML yang sesuai untuk kemudian siap dilakukan *render*.
7. Berkas HTML ditampilkan sebagai respons.

### Virtual Environment
Penggunaan *virtual environment* untuk pembuatan proyek Django diperlukan untuk mengisolasi modul-modul yang diperlukan oleh suatu proyek dari proyek lain. Dengan adanya *virtual environment*, tiap proyek dapat mengelola modul-modulnya sendiri secara terpisah agar dapat berjalan dengan baik. Jika memanfaatkan *global environment*, ada kemungkinan timbulnya isu perbedaan versi modul jika *user* secara global meng-*update* modul yang seharusnya tidak di-*update* untuk proyek tersebut, demi keperluan proyek yang lain. Akibatnya, proyek tersebut berpotensi tidak berjalan dengan baik.<br>

Kita masih bisa membuat aplikasi web berbasis Django tanpa *virtual environment*. Akan tetapi, hal ini tentu saja tidak direkomendasikan karena berpotensi menimbulkan konflik antara satu proyek dan proyek lainnya jika misalnya untuk suatu modul yang sama diperlukan dua versi yang berbeda untuk masing-masing proyek.

### Tahap-Tahap Implementasi Langkah 1 — 4
Tahapan yang saya lakukan dalam mengimplementasikan langkah 1 sampai 4:
1. Saya membuat fungsi `show_catalog` pada `katalog\views.py` yang menerima parameter `request` yang merupakan *request* dari *client*. Fungsi ini yang melakukan pengambilan data dari *database* melalui `models`, lalu hasilnya dipetakan pada `katalog\templates\katalog.html` untuk ditampilkan berdasarkan *context* yang disediakan.
2. Selanjutnya, saya membuat *route* pada `katalog\urls.py` dengan membuat variabel `urlpatterns` dan memasukkan `path('', show_catalog, name='show_catalog')` ke *list* `urlpatterns` tersebut agar *route* tersebut terhubung dengan fungsi `show_catalog` yang sudah dibuat pada `katalog\views.py` sebelumnya. Saya juga memasukkan *route* tersebut ke `urlpatterns` pada `project_django\urls.py` dengan menambahkan `path('katalog/', include('katalog.urls'))`.
3. Setelah itu, saya membuat *migration* berdasarkan model dengan menjalankan `python manage.py makemigrations`. Setelah itu, saya menerapkan *migration* tersebut ke *database* Django dengan menjalankan `python manage.py migrate`. Setelah itu, data pada *file* `.json` yang sudah terdapat pada *folder* `katalog/fixtures` akan di-*load* ke *database* dengan menjalankan `python manage.py loaddata initial_catalog_data.json`.
4. Setelah data di-*load*, selanjutnya akan dilakukan pemetaan data-data tersebut ke `katalog\templates\katalog.html` agar data siap ditampilkan pada halaman web. Pada berkas HTML tersebut, tabel katalog akan diisi dengan data yang diiterasi satu persatu dari *list* berisi barang-barang katalog dengan memanfaatkan sintaks *template tags*.
5. \[BONUS\] Saya juga mengimplementasikan *testing* pada proyek ini untuk *model*, *url*, dan *view* pada `katalog/tests.py`. Selain itu, untuk memperindah tampilan halaman web, saya juga melakukan *styling* berdasarkan *file stylesheet* yang saya buat pada `static/css/style.css`. 
6. Terakhir, sebelum melakukan *deploy*, saya akan menambahkan konfigurasi terkait `PROJECT_ROOT` dan `STATIC_ROOT` pada `project_django/settings.py`. Konfigurasi lain seperti `ALLOWED_HOSTS` dan `MIDDLEWARE` tidak saya tambahkan karena sudah ada dari *template* tugas ini. Lalu, saya melakukan *add*, *commit*, dan *push* ke GitHub.
7. Sampai tahap ini, halaman web sudah jadi dan siap untuk di-*deploy*. Untuk men-*deploy* halaman web ini, saya membuat suatu aplikasi baru pada Heroku, lalu menyambungkan aplikasi tersebut dengan GitHub Repository yang berisi kode-kode dari halaman web. Tidak lupa juga saya menambahkan `HEROKU_API_KEY` dan `HEROKU_APP_NAME` pada `repository secret` GitHub. Setelah itu, saya menjalankan kembali *workflow* yang gagal hingga halaman web berhasil ter-*deploy* dengan baik.

### Referensi
https://www.anbidev.com/python-virtual-environtment/
