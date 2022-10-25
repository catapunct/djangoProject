1.	Pentru a va crea o aplicatie noua intr-un proiect Django trebuie sa rulati linia de comanda: python manage.py startapp app_name


2.	In fisierul settings.py din proiect trebuie sa adaugati in lista Installed_apps numele aplicatiei.


3.	In aplicatia noua creata trebuie sa creati un fisier nou .py numit urls, unde se vor regasi toate url-urile pentru respectiva aplicatie. De asemenea, dupa cea ati facut acest lucru trebuie sa adaugati in fisierul urls.py DIN FOLDERUL PROIECTULUI calea catre fisierul urls.py din cadrul aplicatiei noi create. (hint: path(‘’, include(’app_name.urls)


! Dupa ce v-ati creat modelul in fisierul models.py din aplicatia voastra trebuie sa rulati urmatoarele comenzi.
-	python manage.py makemigrations -> makemigrations generează comenzile SQL pentru aplicațiile preinstalate (care pot fi vizualizate în aplicațiile instalate în settings.py) și modelul de aplicații nou create pe care le adăugați în aplicațiile instalate. Nu execută acele comenzi în fișierul bazei de date. Deci tabelele nu sunt create după migrări.
-	python manage.py migrate -> migrate execută acele comenzi SQL din fișierul bazei de date. Deci, după executarea migrării, toate tabelele aplicațiilor instalate sunt create în fișierul bazei de date. Folosind comanda mentionata, tabelul va fi creat în baza de date atunci când vom utiliza migrate.

`TemplateView` este un view generic pentru a randa o pagina HTML.

Pentru a sterge corect un model, mergem pe modelul dorit, comentam sau stergem codul din interior si rulam din nou
liniile de cod din terminal:
- python manage.py makemigrations
- python manage.py migrate
- 
NU stergem niciodata un model din database cu DROP!

Pentru update la tabela, modificam campul dorit si rulam in terminal linia de cod makemigrations 
si se va crea un fisier py nou in folderul migrations din proiect (un fel de istoric).

`makemigrations` - Va cauta modificarile facute in baza de date.
`migrate` - Executa efectiv modificarile facute.

Nu se recomanda sa se stearga fisiere istoric din migration `0001_nume.py; 0002_nume.py`.

`python manage.py makemigrations nume_aplicatie` - pentru a rula doar ce aplicatie 
dorim noi fara sa se mai ruleze global.

In database se creaza tabel de forma: `numetabel_numemodel`.

In DJANGO definim modelul in database cream tabelul.

`{% csrf_token %}` - Cross Site Request Forgery protection (se foloseste acest tag de django impreuna cu method="post")


# Folosim CreateView (view generic in django) pentru a adauga si sa salvam date intr-o tabela, pe baza unui formular.

Prin `context_object_name = ''` luam toate inregistrarile din tabela.

`<td>{{ student.start_date|date:"d-m-y" }}</td>` -> este diferenta intre 'd-m-y' si 'D-M-Y' (si alte forme), 
avand moduri diferite de afisare a datei in tabel.


---

# Exercitiu
1. Veți adaugă în proiect o aplicație noua numita trainer ( hint: 3pasi)
2. In cadrul aplicației trainer, în fișierul models.py veți adăuga un model nou numit Trainer
Campurile: first_name(charfield), last_name(charfield), course(charfield), description (textfield), start_date si end_date si campanile auxiliare active, created_at, updated_at
3.In cadrul aplicație trainer în fișierul views.py veți adaugă o noua clasa numita TrainerCreateView unde veți completa pentru template_name, model, form_class și success_url. Veti adauga un fisier nou forms.py unde veti customiza fieldurile.
4. Va adăugați în urls.py din aplicația trainer, url pentru clasa definita în views.py
5. Va adăugați 2 înregistrări și verificați dacă au fost salvate în tabela

Nu uitati pentru generarea tabelei: python manage.py makemigrations si apoi python manage.py migrate


Cand avem in html pk(primary key) putem accesa doar un singur element.


Pentru partea de translate putem pune (_("last_name")) in field-uri - si asa django stie ca atunci cand schimbam limba, 
engleza -> romana, exita corespondent in limba aleasa.


!!! Atunci cand vrem sa restrictionam acces la ceva anume trebuie facut si din frontend (adica ascundem butonul din interfata)
cat si din backend (functionalitatea si accesul din url).


`*args` -> pentru mai multe argumente.
`*kwargs` -> pentru mai multe argumente de tipul cheie, valoare.

Atunci cand un user este `SUPERUSER` el nu tine cont de permisiuni si le ignora pe toate. Are acces la tot site-ul
si trebuie avut grija cui i se va da acest statut de 'SUPERUSER'.