# JAPANESE Kanji Driller:

I made this Django app for drilling and memorizing JLPT N2 Kanjis, based on christhemart's app (https://github.com/christhemart/jpdriller).

<a href='https://www.casimages.com/i/201123074551498499.png.html' target='_blank' title='Mon image'><img src='https://nsa40.casimages.com/img/2020/11/23/201123074551498499.png' border='0' alt='Mon image' /></a>

The app requires python and django.


# Features:

- From christhemart's app:
	- Contains all hiragana and katakana as well as nearly 1,000 Japanese vocabulary, mainly kanji.
	- Read wiki for main features.

- NEW: JLPT N2 Kanjis database (advance Japanese)  /!\ French-Japanese /!\

- Musics and Sounds

- Quiz Statistics

- Planning on improving the app, and updating the N2 Database


# How to run the app:

- Connect to jpdriller locally http://127.0.0.1:8000/jpdriller/:
	- run batch file 1 (opens a browser to localhost)
	- run batch file 2 (activate virtualenv)
	- run batch file 3 (python manage.py runserver)

- Create account/login as admin http://127.0.0.1:8000/admin/


# Make your own quiz: 

- You can add your own Kanjis, one by one, within the Django admin panel.

<a href='https://www.casimages.com/i/201120032615877485.png.html' target='_blank' title='Mon image'><img src='https://nsa40.casimages.com/img/2020/11/20/201120032615877485.png' border='0' alt='Mon image' /></a>

- You can also use the 'create_instances.py' script to add multiple Kanjis in a single call (Call bulk_create to create records in a single call).

<a href='https://www.casimages.com/i/201120032213476955.png.html' target='_blank' title='Mon image'><img src='https://nsa40.casimages.com/img/2020/11/20/201120032213476955.png' border='0' alt='Mon image' /></a>
