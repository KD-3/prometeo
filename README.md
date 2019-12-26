# Prometeo
Website for the Technical fest of IIT Jodhpur.
# Setting up the project
1. git init
2. git clone https://github.com/KD-3/prometeo.git
3. git remote add origin https://github.com/KD-3/prometeo.git
4. git remote add upstream https://github.com/KD-3/prometeo.git
5. git fetch upstream master
6. git pull upstream  master
7. pip install -r requirements.txt
8. python manage.py makemigrations users
9. python manage.py makemigrations events
10. python manage.py makemigrations home 
11. python manage.py migrate
12. python manage.py runserver
