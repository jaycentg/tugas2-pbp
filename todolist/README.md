# Penjelasan Tugas 4 PBP

## Identitas
Nama    : Jaycent Gunawan Ongris<br>
NPM     : 2106750231<br>
Kelas   : F

## Link Hasil Deploy
Link untuk menuju ke web yang sudah di-deploy dapat diklik di [sini](https://tugas-pbp-2.herokuapp.com/todolist/login/).

## Jawaban dari Pertanyaan
### Kegunaan CSRF Token
CSRF Token yang dimasukkan pada berkas *form* berfungsi untuk mencegah serangan yang berupa CSRF (Cross Site Request Forgery). Serangan ini akan memanfaatkan *state user* yang sudah terautentikasi untuk melakukan aksi yang tidak seharusnya *user* ingin lakukan, seperti mengubah *request* dari *user* pada aplikasi. CSRF Token dalam implementasinya akan di-*generate* pada *server-side* saat halaman di-*render* dan token ini akan dicocokkan dengan *request* yang masuk. Jika hasil pencocokkan tidak sesuai, maka *request* tidak akan dilayani.<br>
Tentu saja kita tetap masih bisa menjalankan aplikasi tanpa CSRF Token ini, yang dapat dilakukan dengan menambahkan potongan kode `@csrf_exempt` di atas definisi fungsi yang bersesuaian di `views.py`. Akan tetapi, hal ini sangat tidak disarankan untuk dilakukan karena dapat meningkatkan potensi terjadinya serangan CSRF oleh oknum yang tidak bertanggung jawab.

### Pembuatan Form secara Manual
Ya, tentu saja *form* dapat dibuat secara manual tanpa memanfaatkan *template* yang di-*generate* dari Django, salah satu contohnya adalah *form* untuk menambahkan *task* pada aplikasi ini. Saya juga membuat *form* tersebut tanpa menggunakan `forms.py`. Cara yang saya lakukan dalam membuat *form* tersebut adalah membuat suatu berkas HTML yang akan diisi dengan *form* tersebut, lalu membuat tag pembuka dan penutup untuk *form*, yaitu `<form>...</form>`, lalu ditambahkan *attribute* yang bersesuaian, dalam hal ini saya menggunakan *method* `POST` yang dijadikan nilai dari *attribute* `method`. Selain itu, dapat ditambahkan juga *attribute* `action` yang dapat berisi *URL Destination* dari *form*. Kemudian, di dalam tag tersebut, dapat ditambahkan elemen-elemen HTML yang dapat digunakan bagi *user* untuk meng-*input* data, seperti `<input>...</input>`, `<textarea>...</textarea>`, dan sebagainya. Lalu, tambahkan atribut-atribut yang diperlukan pada tag tersebut. Salah satu atribut yang penting adalah `name`, karena `value` dari atribut ini akan digunakan untuk mendapatkan data yang dimasukkan *user* pada *field* tersebut. Selanjutnya, kita dapat membuat fungsi pada `views.py` yang akan mengambil data yang sudah dimasukkan oleh *user*. Pengambilan data tersebut dapat dengan menggunakan `request.POST.get('attribute')` atau `request.POST['attribute']`. Setelah itu, data tersebut akan diproses sesuai dengan keinginan kita, entah itu mau dimasukkan ke *database*, mau diautentikasi, atau keperluan lainnya.

### Alur Data pada Form
Pertama-tama user akan memasukkan data pada *form*, spesifiknya pada *field* yang sudah disediakan. Kemudian, untuk mengambil data dari form tersebut, dapat dilakukan pemanggilan `request.POST`. Pemanggilan ini akan mengembalikan *dictionary* dengan *key* berupa nilai dari atribut `name` pada *field* dan *value* berupa data yang diisi oleh *user*. Sampai saat ini, kita sudah mendapatkan data yang dimasukkan *user* pada *form* tersebut. Selanjutnya, kita akan memasukkan data tersebut ke *database* dapat dengan memanfaatkan *method* `create(attr1=val1, attr2=val2, ...)` atau dengan melakukan instansiasi *class* yang menjadi *model*, lalu meng-*edit* atribut dari *class* tersebut satu persatu, dan terakhir menyimpannya dengan menggunakan *method* `save`. Sampai saat ini, data sudah tersimpan ke *database* Django. Untuk ditampilkan ke dalam berkas HTML, kita harus mengakses data tersebut dari *database* terlebih dahulu, dapat dengan menggunakan *method* `all` untuk mengambil semua objek dari *database*, *method* `filter` untuk mengambil objek yang memenuhi kriteria yang di-*state* pada parameter *method* tersebut, atau dapat juga dengan *method* `get` untuk mengambil tepat satu objek yang memenuhi kriteria yang di-*state* pada parameter *method* tersebut (umumnya memanfaatkan *primary key* yang bersifat unik agar bisa mengembalikan tepat satu). Setelah itu, data yang sudah didapatkan lalu dimasukkan ke `context` yang menjadi parameter fungsi `render` dari fungsi yang bersesuaian di `views.py` agar dapat diakses dan ditampilkan menggunakan *template tags* pada berkas HTML yang bersesuaian.

### Tahap-Tahap Implementasi Checklist
Tahapan yang saya lakukan dalam mengimplementasikan checklist:
1. Pertama-tama, saya membuat suatu aplikasi baru yang bernama "todolist" dengan menjalankan perintah `python manage.py startapp todolist` dan menambahkan `todolist` ke `INSTALLED_APPS` di `settings.py`.
2. Selanjutnya, saya menambahkan `routing` berupa `path('todolist/', include('todolist.urls'))` pada `urlpatterns` di `urls.py` milik `project_django`.
3. Setelah itu, saya membuat sebuah class `Task` di `models.py` pada aplikasi *todolist* dengan atribut seperti yang telah diberikan pada soal, yaitu `user`, `date`, `title`, dan `description`. 
4. Lalu, saya menambahkan suatu fungsi `register` untuk meng-*handle* *user* yang ingin *register* pada `views.py` milik `todolist`. Kemudian, saya membuat berkas `register.html` sebagai halaman *register* dari *user*. Selanjutnya, saya mengimpor fungsi ini ke dalam `urls.py` pada `todolist` untuk kemudian saya tambahkan ke `urlpatterns`.
5. Saya kemudian membuat suatu fungsi `show_todolist` untuk menampilkan daftar *todolist* pada `views.py` milik `todolist`. Kemudian, saya membuat berkas `todolist.html` sebagai halaman untuk menampilkan *todolist* dari *user*. Selanjutnya, saya mengimpor fungsi ini ke dalam `urls.py` pada `todolist` untuk kemudian saya tambahkan ke `urlpatterns`.
6. Selanjutnya, saya membuat fungsi `login_user` sebagai `login page` dari `user` pada `views.py` milik `todolist`. Kemudian, saya membuat berkas `login.html` sebagai halaman untuk bagi *user* untuk `login`. Setelah itu, saya mengimpor fungsi ini ke dalam `urls.py` pada `todolist` untuk kemudian saya tambahkan ke `urlpatterns`.
7. Setelah itu, saya membuat fungsi `logout_user` untuk meng-*handle* *user* yang ingin *logout* dari aplikasi. Fungsi ini akan mengembalikan fungsi `redirect` yang akan membawa *user* kembali ke halaman *login*. Setelah itu, saya mengimpor fungsi ini ke `urls.py` pada `todolist` dan memasukkannya ke `urlpatterns`. Saya juga kemudian menambahkan tombol untuk *logout* pada halaman `todolist.html` yang sudah di-*link* dengan URL `logout` yang berisi mekanisme *logout user*.
8. Selanjutnya, saya akan melakukan restriksi akses terhadap halaman `todolist`, yaitu user yang sudah login saja yang boleh masuk, dengan cara mengimpor `login_required` pada `views.py` dan menambahkan kode `@login_required(login_url='/todolist/login/')` di atas fungsi `show_todolist`.
9. Sehabis itu, saya membuat suatu fungsi `create_task` pada `views.py` yang berfungsi untuk meng-*handle* *user* yang ingin membuat *task* baru. Saya lalu mengambil data dari *form* yang sudah diisi oleh *user* dengan memanfaatkan `request.POST` untuk kemudian siap dimasukkan ke database. Kemudian, saya membuat berkas `new_task.html` yang berisi *form* bagi *user* untuk memasukkan detail terkait *task* baru. Lalu, saya membuat *route* ke *page* ini dengan mengimpor fungsi `create_task` pada `urls.py` pada `todolist` dan memasukkannya ke `urlpatterns`. Terkahir, saya menambahkan potongan kode `@login_required(login_url='/todolist/login/')` di atas definisi fungsi `create_task` ini.
10. [BONUS] Selanjutnya, saya membuat tambahan atribut pada `class Task` yaitu `is_finished` dengan *default value False*. Setelah itu, saya membuat skema migrasi dan melakukan migrasi dengan menjalankan perintah `python manage.py makemigrations` dan `python manage.py migrate`.
11. [BONUS] Lalu, saya membuat fungsi baru yang bernama `delete_task` pada `views.py` yang menerima parameter `request` dan `id`. Fungsi ini berfungsi untuk menghapus *instance* dengan `id` yang di-*pass* ke parameter tersebut. Caranya adalah dengan mengambil objek tersebut dari *database* dengan menggunakan *method* `get` berdasarkan `id` lalu dihapus dengan *method* `delete`. Setelah itu, saya mengimpor fungsi ini ke `urls.py` pada `todolist` dan memasukkannya ke `urlpatterns`. Saya kemudian membuat suatu kolom baru di tabel pada `todolist.html` untuk menghapus objek yang bersangkutan.
12. [BONUS] Setelah itu, saya membuat fungsi yang bernama `change_status` pada `views.py` yang menerima parameter `request` dan `id` untuk mengubah status dari atribut `is_finished` dari `True` ke `False` atau sebaliknya. Sama seperti pada *step* sebelumnya, saya pertama-tama mengambil objek tersebut dari *database* dengan menggunakan *method* `get` berdasarkan `id`, lalu saya mengubah atribut dari objek tersebut. Selanjutnya, saya menyimpan perubahan tersebut dengan memanfaatkan *method* `save`. Setelah itu, saya mengimpor fungsi ini ke `urls.py` pada `todolist` dan memasukkannya ke `urlpatterns`. Kemudian, saya membuat dua kolom baru pada tabel di `todolist.html` untuk menampilkan status dari *task* dan tombol untuk mengubah status tersebut.
13. Untuk melakukan *tracking* perubahan pada *database*, saya membuat akun *superuser* agar dapat mengakses *Django Admin*. Lalu, saya menambahkan model `Task` ke dalam `admin.py`.
14. Selanjutnya, saya melakukan `add`, `commit`, dan `push` ke GitHub, lalu melakukan *re-run jobs* agar perubahan yang telah saya buat ter-*deploy*.

### Username dan Password
1. USERNAME: dummy1   PASSWORD: abc43210987
2. USERNAME: dummy2   PASSWORD: 0987abcd4321

### Referensi
https://www.educative.io/answers/what-is-a-csrf-token-in-django<br>

# Penjelasan Tugas 5 PBP

## Identitas
Nama    : Jaycent Gunawan Ongris<br>
NPM     : 2106750231<br>
Kelas   : F

## Link Hasil Deploy
Link untuk menuju ke web yang sudah di-deploy dapat diklik di [sini](https://tugas-pbp-2.herokuapp.com/todolist/login/).

## Jawaban dari Pertanyaan
### Perbedaan Inline, Internal, dan External CSS
Inline CSS adalah metode penulisan CSS pada atribut `style` elemen HTML yang bersangkutan. Internal CSS adalah metode penulisan CSS pada *tag* `style` di halaman HTML yang bersangkutan. *Tag* ini biasanya ditempatkan di bagian *header* dari *file* HTML yang bersangkutan. Sedangkan, external CSS adalah metode penulisan CSS pada file berekstensi `.css` yang terpisah dengan halaman HTML.<br>
Berikut adalah kelebihan dan kekurangannya masing-masing.
1. Inline CSS memiliki kelebihan berupa mempercepat *load website* dan memperkecil *HTTP Request*, serta bermanfaat jika kita hanya akan menguji perubahan pada tampilan HTML untuk elemen tertentu saja. Sedangkan, kelemahannya adalah kurang efisien dikarenakan kode CSS yang dimasukkan hanya berlaku pada elemen HTML tersebut saja.
2. Internal CSS memiliki kelebihan berupa tidak perlu melakukan *import file* dari luar *file* HTML, sudah bisa memanfaatkan *selector* untuk `class` dan `ID`, serta bermanfaat jika perubahan yang diinginkan hanya pada satu halaman HTML tertentu saja. Sedangkan, kelemahannya adalah akan memperlambat *load website* karena CSS yang berbeda akan perlu di-*load* ulang tiap kali mengganti halaman web, serta membuat ukuran *file* HTML menjadi lebih besar.
3. External CSS memiliki kelebihan dapat membuat *file* HTML menjadi lebih kecil, proses *load website* menjadi lebih cepat, dan satu *file* CSS tersebut dapat dimanfaatkan untuk beberapa halaman sekaligus. Sedangkan, kelemahannya adalah tidak cocok untuk halaman web yang membutuhkan halaman yang berbeda-beda antara satu dengan yang lainnya (*custom*), serta halaman web akan menjadi berantakan jika halaman HTML-nya berhasil ditampilkan tetapi CSS-nya gagal saat di-*load*.

### Tag HTML5 yang Diketahui
Berikut adalah *tag* HTML5 yang saya ketahui:
1. `<a>` untuk menambahkan *hyperlink*
2. `<b>` untuk mempertebal teks (*bold*)
3. `<body>` untuk mendefinisikan *body* dari halaman HTML
4. `<br>` untuk menambahkan *line break* (baris baru)
5. `<button>` untuk menambahkan tombol
6. `<caption>` untuk mendefinisikan *caption* dari suatu *table*
7. `<div>` untuk mendefinisikan suatu *division* atau bagian tertentu dalam suatu halaman HTML
8. `<form>` untuk mendefinisikan suatu *form* untuk mengambil input dari *user*
9. `<head>` untuk mendefinisikan bagian *head* dari suatu halaman HTML, yang berisi informasi terkait halaman HTML tersebut
10. `<h1>` sampai `<h6>` untuk membuat suatu *heading*
11. `<html>` mendefinisikan *root* dari sebuah halaman HTML
12. `<i>` untuk memiringkan teks (*italic*)
13. `<img>` untuk menambahkan gambar
14. `<input>` untuk mendefinisikan *input field* yang akan diisi oleh *user*
15. `<li>` untuk mendefinisikan tiap-tiap elemen dari suatu list *unordered* (`<ul>`) atau *ordered* (`<ol>`)
16. `<nav>` untuk mendefinisikan suatu bagian yang terdiri dari *navigation links*
17. `<p>` untuk mendefinisikan suatu teks paragraf
18. `<script>` sebagai tempat meletakkan *script* yang diperlukan
19. `<span>` untuk mendefinisikan bagian pada suatu teks menjadi *inline* dan *styless*
20. `<style>` sebagai tempat untuk mendefinisikan internal CSS dalam suatu halaman HTML
21. `<table>` untuk mendefinisikan tabel
22. `<td>` untuk mendefinisikan sebuah cell pada tabel
23. `<textarea>` untuk mendefinisikan *input field* untuk *text* yang bersifat *multiline*
24. `<th>` untuk mendefinisikan *header* tabel
25. `<title>` untuk mendefinisikan judul dokumen HTML
26. `<tr>` untuk mendefinisikan suatu baris pada tabel

### Tipe Selector CSS yang Diketahui
Berikut adalah tipe *selector* CSS yang saya ketahui:
1. Element selector, yakni *selector* yang langsung memanfaatkan *tag* HTML sebagai *selector*-nya. Untuk sintaks pada CSS-nya, langsung memanfaatkan nama dari *tag* tersebut, seperti `h1{...}`.
2. ID selector, yakni *selector* yang menggunakan ID yang sudah didefinisikan pada *tag* sebagai *selector*-nya. Untuk sintaks pada CSS-nya, memanfaatkan nama ID pada *tag* tersebut, tetapi ditambahkan `#` di awal, seperti untuk `id="nama"`, di CSS akan ditulis `#nama{...}`.
3. Class selector, yakni *selector* yang menggunakan class yang sudah didefinisikan pada *tag* sebagai *selector*-nya. Untuk sintaks pada CSS-nya, memanfaatkan nama class pada *tag* tersebut, tetapi ditambahkan `.` di awal, seperti untuk `class="nama"`, di CSS akan ditulis `.nama{...}`.

### Tahap-Tahap Implementasi Checklist
Tahapan yang saya lakukan dalam mengimplementasikan checklist:
1. Pertama-tama, saya menyediakan *static files* yang diperlukan dalam mengerjakan tugas ini, dalam hal ini adalah file CSS untuk page `login`, yaitu `login.css` dan untuk page `todolist` yaitu `todolist.css`. Selanjutnya, saya menjalankan perintah `collectstatic` untuk mengumpulkan semua *static files*.
2. Selanjutnya, saya menambahkan potongan kode untuk menjalankan Bootstrap di tiap *file* HTML yang akan saya kustomisasi. Potongan kode tersebut adalah `<link href="https://cdn.jsdelivr.net/npm/bootstrap@5.2.1/dist/css/bootstrap.min.css" rel="stylesheet" integrity="sha384-iYQeCzEYFbKjA/T2uDLTpkwGzCiq6soy8tYaI1GyVh/UjpbCx/TYkiZhlZB6+fzT" crossorigin="anonymous">` dan `<script src="https://cdn.jsdelivr.net/npm/bootstrap@5.2.1/dist/js/bootstrap.bundle.min.js" integrity="sha384-u1OknCvxWvY5kfmNBILK2hRnQC3Pr17a+RTT6rIHI7NnikvbZlHgTPOOmMi466C8" crossorigin="anonymous"></script>`. Tidak lupa juga saya menambahkan `{% load static %}` dan direktori *static file* dalam atribut `href` *tag* `link` jika ada *static file* yang ingin saya masukkan ke dalam *file* HTML yang akan dikustomisasi tersebut.
3. Setelah itu, saya mulai melakukan kustomisasi untuk *file* `login.html`. Saya ingin membuat *login page* yang memanfaatkan *card* dengan *background gradient* agar terlihat menarik. Adapun pengaturan untuk *gradient* tersebut saya masukkan ke file `CSS` terpisah pada *selector* `body`. Selain itu, saya juga memanfaatkan *class selector* untuk melakukan kustomisasi teks pada class `title` dan `label-input`. Sementara itu, untuk *form*, saya menggunakan *floating label* pada *input field* agar terlihat menarik. Saya juga melakukan kustomisasi untuk *padding* dan *margin* pada elemen-elemen tersebut agar rapi.
4. Lalu, saya melakukan kustomisasi untuk *file* `todolist.html`. Saya menambahkan `navbar` pada bagian atas dari halaman yang berisi nama aplikasi, nama *user* yang *logged in*, tombol untuk menambahkan *task* baru, dan tombol untuk *logout*. Saya memanfaatkan `button` bawaan dari Bootstrap untuk itu. Selanjutnya, saya mengganti metode penampilan task dari bentuk *tabel* ke bentuk *card* agar terlihat lebih menarik. Di dalam tiap *card*, akan ada informasi terkait nama *task* yang menjadi `card-title`, deskripsi task dan tanggal pembuatan *task* yang menjadi `card-text`, informasi terkait status dari *task* apakah sudah selesai atau tidak yang ditampilkan dalam bentuk `badge` di samping nama *task*, serta dua tombol di bawah informasi tanggal pembuatan *task* yang berfungsi untuk mengubah status dari *task* dan menghapus *task*. Saya juga melakukan kustomisasi *message* yang ditampilkan dengan memanfaatkan `alert-dismissible` dari Bootstrap. Lalu, untuk mengerjakan *bonus task*, saya menambahkan `:hover` pada `todolist.css` untuk *class card* dengan mengubah `background-color` dari *card* tersebut. Saya juga menggunakan *conditionals* dari *template tags* Django untuk menampilkan teks 'No Task' jika belum ada *task* yang dibuat.
5. Selanjutnya, saya melakukan kustomisasi untuk *file* `new_task.html`. Saya tetap menggunakan `navbar` yang telah saya buat di *page* `todolist`, hanya saja saya menghilangkan tombol untuk menambah *task* baru. Setelah itu, saya merapikan halaman ini dengan menambahkan *margin* dan *padding* pada *input field* serta menambahkan dua `button` di bawah untuk *save task* dan *discard task* memanfaatkan `button` dari Bootstrap.
6. Terakhir, untuk halaman `register.html`, saya memanfaatkan kembali *card* yang telah saya buat sebelumnya pada halaman `login`, tetapi dengan mengubah isinya. Saya masih memanfaatkan `{{form.as_table}}` untuk membuat *input field* yang dibutuhkan, akan tetapi saya melakukan kustomisasi menggunakan Bootstrap dengan menghilangkan *border* dari *table* dan membuat tabel menjadi *responsive* dengan memanfaatkan *class* `table-responsive`.
7. Selanjutnya, saya melakukan `add`, `commit`, dan `push` ke GitHub, lalu melakukan *re-run jobs* agar perubahan yang telah saya buat ter-*deploy*.

### Referensi
https://mdbootstrap.com/docs/standard/extended/login/<br>
https://getbootstrap.com/<br>
https://www.niagahoster.co.id/blog/perbedaan-internal-external-dan-inline-css/<br>
https://qwords.com/blog/perbedaan-internal-external-dan-inline-css/<br>
https://www.tutorialrepublic.com/html-reference/html5-tags.php
