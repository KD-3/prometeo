# Prometeo
Website for the Technical fest of IIT Jodhpur.
# Setting up the project
1. git init
2. git clone https://github.com/KD-3/prometeo.git
3. git remote add origin https://github.com/KD-3/prometeo.git
4. git remote add upstream https://github.com/KD-3/prometeo.git
5. git fetch upstream master
6. git pull upstream  master
7. python manage.py makemigrations users
8. python manage.py migrate
9. pthon manage.py runserver
