# Anime-Tracker

 - [x] Membuat sebuah proyek Django baru

Untuk Membuat sebuah proyek baru pada django, kita perlu membuka terminal pada path folder direktori, pertama kita perlu membuat folder direktori utama yang menampung semua file projek kita, sebelum itu kita perlu membuat virtual environmet pada folder projek kita dengan perintah

```
python -m venv env
```

kemudian mengaktifkan virtual environmet di terminal dengan perintah

```
env\Scripts\activate
```

kemudian tampilan pada terminal akan menjadi seperti ini

```
(env) D:\UI\PBP\anime-series-tracker> 
```

kemudian kita menyiapkan depedencies yang kita perlukan untuk menginisialisasi projek dengan membuat file requirements.txt, yang isinya

```
django
gunicorn
whitenoise
psycopg2-binary
requests
urllib3
```
Kemudian melakukan instalasi django dengan mengetikkan perintah
```
pip install -r requirements.txt
```
Setelah proses instalasi selesai, kemudian kita membuat aplikasi projek django yang akan kita buat, dengan mengetikkan perintah
```
django-admin startproject anime_tracker
```
Tampilan direktori akan jadi seperti ini:

![alt text](pictures/1.png)

 - [x]  Membuat aplikasi dengan nama main pada proyek tersebut.
 
Kemudian untuk membuat aplikasi main yang berisi Models, View, Template dengan menggunakan perintah ini pada terminal di direktori utama

```
python manage.py startapp main
```

Untuk memasukkan aplikasi main sebagai bagian dari anime_series tracker lakukan konfigurasi dengan menambahkan 'main' pada settings.py di dalam direktori proyek anime_series_tracker 

```
INSTALLED_APPS = [
    'main',
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
]
```

- [x] Melakukan routing pada proyek agar dapat menjalankan aplikasi main.
  
untuk menambahkan routing ke proyek main, kita perlu mengimpor fungsi include() dari django.urls kemudian mengubah path pada urls.py 

```
urlpatterns = [
    ...
    path('', include('main.urls')),
    ...
]
```
path('') tidak diisi karena untuk menginisialisasi route pada halaman utam dari aplikasi, kemudian menambahkan route aplikasi ke aplikasi main


- [x] Membuat model pada aplikasi main dengan nama Item dan memiliki atribut wajib sebagai berikut.

- name sebagai nama item dengan tipe CharField.
- amount sebagai jumlah item dengan tipe IntegerField.
- description sebagai deskripsi item dengan tipe TextField.
  
Anime tracker disini akan membuat model dengan field name sebagai nama item dengan tipe CharField, episodes sebagai item amount dengan IntegerField, dan synopsis sebagai item description dengan Textfield

Kemudian ada atribut-atribut tambahan pada field yaitu rating, studio, genre, dan release date

```
from django.db import models

# Create your models here.

class Anime(models.Model):
    name = models.CharField(max_length=255)
    episodes = models.IntegerField()
    synopsis = models.TextField()
    rating = models.FloatField()
    studio = models.CharField(max_length=255)
    genre = models.CharField(max_length=255)
    release_date = models.DateField()
```

- [x] Membuat sebuah fungsi pada views.py untuk dikembalikan ke dalam sebuah template HTML yang menampilkan nama aplikasi serta nama dan kelas kamu.

disini kita akan mengimpor modul dengan fungsi show_main yang terintegrasi dengan routing proyek main lalu menambahkan fungsi :

```
def show_main(request):
    context = {
        'name': 'Muhammad Eagel Triutama',
        'class': 'PBP A'
    }

    return render(request, "main.html", context)
```

kemudian pada direktori main kita akan menambahkan direktori main, lalu menambahkan file html dengan nama main.html, lalu menghubungkan dengan variabel context yang ada show_main

```
<h5>Name:</h5>
<p>{{ name }}</p>
<p></p>
<h5>Class:</h5>
<p>{{ class }}</p>
```

- [x] Membuat sebuah routing pada urls.py aplikasi main untuk memetakan fungsi yang telah dibuat pada views.py

untuk membuat routing pada aplikasi main yaitu dengan membuat routes.py pada direktori aplikasi main kemudian menghubungkan juga dengan fungsi show_main

```
from django.urls import path
from main.views import show_main

app_name = 'main'

urlpatterns = [
    path('', show_main, name='show_main'),
]
```

- [x] Melakukan deployment ke PWS terhadap aplikasi yang sudah dibuat sehingga nantinya dapat diakses oleh teman-temanmu melalui Internet.
- [x]  Membuat sebuah README.md yang berisi tautan menuju aplikasi PWS yang sudah di-deploy, serta jawaban dari beberapa pertanyaan berikut. 


 ## Soal

- Buatlah bagan yang berisi request client ke web aplikasi berbasis Django beserta responnya dan jelaskan pada bagan tersebut kaitan antara urls.py, views.py, models.py, dan berkas html.

```

```

- Jelaskan mengapa kita menggunakan virtual environment? Apakah kita tetap dapat membuat aplikasi web berbasis Django tanpa menggunakan virtual environment?

> Virtual environtment digunakan untuk mengisolasi depedensi proyek yang mana setiap proyek python memiliki depedensi dan library sendiri yang mungkin berbeda dengan proyek lainnya, yang mana hal ini berguna untuk menghindari konflik depedensi antara proyek satu dengan proyek lain, dalam menjalankan aplikasi web berbasis django tanpa menggunakan virtual environtment itu memungkinkan yaitu dengan menginstall django package secara systemwide yang tidak direkomendasikan karena akan konflik versi dan permasalahan pada depedensi system-level, caranya yaitu dengan mengetikkan "python -m install Django" dan membuat projek dengan mengetikkan perintah "django-admin startproject 'nama proyek' "

- Jelaskan apakah itu MVC, MVT, MVVM dan perbedaan dari ketiganya.

> MVC, MVT, dan MVVM merupakan pola design yang dirancang untuk memisahkan beberapa bagian dan bagian-bagian tersebut menangani masalah-masalah tertentu.

> MVC (Model View Controller) adalah pola design dengan Model sebagai bagian yang mengatur dan melakukan proses manajemen data, View sebagai bagian yang akan menampilkan visual atau tampilan kepada user atau client, dan Controller sebagai bagian yang memanipulasi Model dan menampilkan data ke bagian View atau menjembatani antara Model dan View

> MVT (Model View Template) adalah pola design dari django yang memiliki hampir sama dengan MVC, perbedaan yang kontras antara MVT dan MVC adalah Controller dari MVT dikelola oleh framework django itu sendiri. 
> <br> <br> Model pada MVT berperan sebagai antarmuka dan manajamen data pada aplikasi pada web application, bagian ini akan dihubungkan dengan database seperti MySql ataupun PostgreSQL,
> <br> <br> View pada MVT berinteraksi dengan Model dan akan melakukan proses render ke bagian Template sehingga View pada MVT itu merupakan controller dalam pola design MVC, yang mana akan menerima HTTP Request dan melakukan HTTP Response
> <br><br> Templates pada MVT merupakan bagian yang memberikan visual atau tampilan pada aplikasi, Template merupakan file HTML yang bersifat stasis ataupun dinamis

> MVVM (Model View ViewModel) adalah pola design aplikasi yang berbasis GUI, biasanya digunakan pada pembuatan aplikasi mobile
> <br> <br> Model pada MVVM merupakan bagian yang merepresentasikan data yang didalamnya terdapat kelas-kelas data
> <br> <br> View pada MVVM merupakan layer yang berisi UI (User Interface) atau yang mengatur bagaimana informasi ditampilka ke client atau user
> <br> <br> ViewModel pada MVVM bertugas untuk interaksi dengan model dan meneruskan data ke bagian View

### MVC VS MVT

| MVC                                                              | MVT                                                                                                                               |
| ---------------------------------------------------------------- | --------------------------------------------------------------------------------------------------------------------------------- |
| **Controller** berperan sebagai penghubung antara Model dan View | **View** berperan sebagai penghubung antara Model dan Template, yang mana akan menerima HTTP Request dan memberikan HTTP Response |
| **View** berperan dalam menampilkan data dari model              | **Templates** berperan dalam menampilkan data dari model                                                                          |
| Sulit untuk melakukan modifikasi | Mudah untuk melakukan modifikasi |
| Tidak berkaitan dengan mapping URL | Berkaitan dengan Mapping URL |

### MVC VS MVVM

| MVC                                                              | MVVM                                                                                                                               |
| ---------------------------------------------------------------- | --------------------------------------------------------------------------------------------------------------------------------- |
|Membagi infrastuktur design menjadi 3 bagian yang terhubung satu sama lain Model, View, dan Controller| Infrastuktur design dibangun menggunakan GUI atau Graphical User Interface |
|Koneksi antara controller dan view dibangun dengan konsep multiple to single| Koneksi one to many dibangun oleh view |
**Controller** berperan dalam membangun manajemen koneksi antar View dan Model| **ViewModel** berperan dalam membangun manajemen koneksi antara View dan Model |








