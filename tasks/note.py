del db.sqlite3
python manage.py makemigrations
python manage.py migrate


npm run build:tailwind 
npm run watch:tailwind 

python manage.py shell

from tasks.models import Company


Company.objects.create(name="Bn HQ") 

or

python manage.py createsuperuser
python manage.py runserver
 

