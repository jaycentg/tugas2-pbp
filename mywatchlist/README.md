# Penjelasan Tugas 3 PBP

## Identitas
Nama    : Jaycent Gunawan Ongris<br>
NPM     : 2106750231<br>
Kelas   : F

## Link Hasil Deploy
Link untuk menuju ke web yang sudah di-deploy dapat diklik di [sini](https://tugas-pbp-2.herokuapp.com/katalog/).

## Screenshots dari Postman

## Jawaban dari Pertanyaan
### Perbedaan JSON, XML, dan HTML
JSON (JavaScript Object Notation) adalah suatu format *file* turunan dari bahasa pemrograman JavaScript yang ditujukan untuk proses penyimpanan dan transportasi data. JSON memiliki alternatif yang juga banyak digunakan untuk tujuan yang sama, yaitu XML. XML (eXtensible Markup Language) merupakan *markup language* yang didesain untuk menyimpan dan mengirimkan data. Sementara itu, sama seperti XML, HTML (HyperText Markup Language) juga merupakan *markup language*, tetapi bedanya HTML didesain khusus untuk menampilkan data. 

Berikut adalah perbedaan JSON, XML, dan HTML.
1. JSON dan XML memiliki tujuan untuk penyimpanan dan transportasi data, sedangkan HTML khusus untuk menampilkan data.
2. XML dan HTML memiliki sintaks yang mirip, yaitu menggunakan *opening* dan *closing tags*, sementara itu JSON memiliki sintaks yang serupa dengan *object* pada JavaScript.

Sementara itu, secara khusus, berikut adalah perbedaan dari JSON dan XML dalam konteks penyimpanan dan transportasi data.
1. JSON mendukung penggunaan *array*, sedangkan XML tidak.
2. Sintaks JSON lebih ringkas dan mudah dipahami jika dibandingkan dengan XML.
3. File JSON lebih ringan dan cepat jika dibandingkan dengan XML.
4. Untuk *browser* yang tidak terlalu aman, JSON lebih rentan terhadap serangan *hacking* dibanding XML.
5. JSON tidak menggunakan *tag*, sedangkan XML membutuhkan *tag* pembuka dan *tag* penutup.

Secara khusus, berikut adalah perbedaan dari XML dan HTML.
1. XML berfungsi untuk penyimpanan dan transportasi data, sedangkan HTML untuk menampilkan data.
2. XML bersifat *case sensitive*, sedangkan HTML bersifat *case insensitive*.
3. XML dalam penerapannya bebas menggunakan *tag* yang dibuat sendiri, hanya saja wajib ada *tag* penutupnya, sedangkan HTML hanya bisa menggunakan *tag* tertentu yang sesuai dan terkadang tidak memerlukan *tag* penutup.
4. XML bersifat dinamis karena digunakan untuk transfer data, sedangkan HTML bersifat statis karena hanya digunakan untuk menampilkan data.

### Pentingnya Data Delivery
Data delivery penting dalam pengembangan aplikasi pada suatu platform sebagai sarana untuk mengirimkan data antarstack yang digunakan dalam aplikasi tersebut. Dengan adanya data delivery, kita dapat mengirimkan, menyimpan, dan menggunakan data yang dibutuhkan.

### Tahap-Tahap Implementasi Checklist
Tahapan yang saya lakukan dalam mengimplementasikan checklist:
1. Pertama-tama, saya membuat suatu aplikasi baru yang bernama "mywatchlist" dengan menjalankan perintah `python manage.py startapp mywatchlist` dan menambahkan `mywatchlist` ke `INSTALLED_APPS` di `settings.py`.
2. Setelah itu, saya mengisi `models.py` dengan membuat *class* `MyWatchList` yang berisi atribut-atribut yang sesuai dengan *checklist* yang diberikan dengan tipe data yang sesuai. Lalu, saya melakukan *migration* dengan menjalankan `python manage.py makemigrations` dan `python manage.py migrate`. Selanjutnya, saya membuat file `initial_watchlist.json` di `fixtures` yang berisi 10 inisial data terkait film yang akan dimasukkan ke *database*. Setelah itu, data tersebut di-*load* ke *database* dengan menjalankan perintah `python manage.py loaddata initial_watchlist.json`. 
3. Selanjutnya, saya membuat *folder* `templates` di direktori `mywatchlist` dan mengisi *folder* tersebut dengan dua buah *file* HTML yang akan ditampilkan pada `localhost:8000/mywatchlist` dan `localhost:8000/mywatchlist/html`. Untuk yang `localhost:8000/mywatchlist` saya hanya menggunakan *file* HTML kosong, yaitu `empty.html` dikarenakan *file* tersebut hanya untuk keperluan *routing*, dan data yang sebenarnya akan ditampilkan pada `localhost:8000/mywatchlist/html`, yaitu `watchlist.html`.
4. Setelah itu, saya mengedit file `views.py` di *folder* `mywatchlist` dan menambahkan fungsi-fungsi yang diperlukan, seperti `show_watchlist` untuk `localhost:8000/mywatchlist`, `show_html` untuk `localhost:8000/mywatchlist/html`, `show_xml` untuk `localhost:8000/mywatchlist/xml`, dan `show_json` untuk `localhost:8000/mywatchlist/json`. Fungsi `show_html` akan menampilkan page HTML `watchlist.html`, `show_xml` akan menampilkan data dalam bentuk XML, dan `show_json` akan menampilkan data dalam bentuk JSON.
5. \[BONUS\] Lalu, saya menambahkan *logic* untuk menghitung jumlah film yang sudah ditonton pada fungsi `show_html` untuk kemudian dimasukkan pada `context` agar dapat ditampilkan hasilnya di `localhost:8000/mywatchlist/html`.
6. Sehabis itu, saya kemudian mengedit *file* `watchlist.html` yang telah dibuat dengan memasukkan hasil modifikasi *template* HTML dari tugas sebelumnya, termasuk menambahkan pesan terkait jumlah film yang sudah ditonton.
7. Selanjutnya, saya menambahkan `path('mywatchlist/', include('mywatchlist.urls'))` di `urlpatterns` pada `urls.py` di `project_django`. Lalu, menambahkan `app_name = 'mywatchlist'` dan `urlpatterns = [path('', show_watchlist, name='show_watchlist'),path('html/', show_html, name='show_html'),path('xml/', show_xml, name='show_xml'),path('json/', show_json, name='show_json'),]` di `urls.py` milik *folder* `mywatchlist` setelah fungsi-fungsi tersebut diimpor ke dalam file tersebut.
8. Setelah itu, saya mempersiapkan *testing* pada *tests.py* untuk mengecek apakah URL `localhost:8000/mywatchlist/html`, `localhost:8000/mywatchlist/xml`, dan `localhost:8000/mywatchlist/json` mengembalikan respon `HTTP 200 OK`. Hal ini diimplementasikan dengan membuat tiga fungsi untuk masing-masing URL, melakukan `get` dari URL tersebut dan mengecek apakah `status_code`-nya 200 atau bukan.
9. Selanjutnya, saya melakukan `add`, `commit`, dan `push` ke GitHub, lalu melakukan *re-run jobs* agar perubahan yang telah saya buat ter-*deploy*. 

### Referensi
https://www.dicoding.com/blog/apa-itu-json/
https://www.geeksforgeeks.org/difference-between-json-and-xml/
https://www.geeksforgeeks.org/html-vs-xml/
https://www.dewaweb.com/blog/apa-itu-xml/