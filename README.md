🛠️ *Tecnologias Utilizadas*
Backend: Python, HTML, Css, Javascript Django, Django REST Framework

Servidor de Aplicação: Django (Python manage.py runserver)


Banco de Dados: SQLITE (Teste)

Autenticação: djangorestframework-simplejwt

Documentação: drf-spectacular

Admin: django-jazzmin


<img width="150" height="150" alt="Python-logo-notext svg" src="https://github.com/user-attachments/assets/50b2cf26-6a19-408a-b1a7-f37d1782beb5" />

<img width="250" height="250" alt="1710173183065" src="https://github.com/user-attachments/assets/884e24b8-9ee2-4e02-b860-5efcc8a04703" />

--------------------------------------------------
Pré-requisitos:
Python

Django

IDE

Git

--------------------------------------------------

(TUDO A BAIXO PRECISA SER DIGITADO NO TERMINAL)

python -m venv venv

.\venv\Scripts\Activate.ps1

se der erro:

venv\Scripts\activate.bat

ou:

source venv/Scripts/activate

e caso de linux ou macOS:

source venv/bin/activate

git clone -b main https://github.com/cauaunit/petguard.git

no mesmo nível do manage.py(arquivo do backend), rodar:

(para chegar no nível do manage.py, digitamos cd backend e depois, cd backend-jotanunes)

pip install django

pip freeze > requirements.txt

pip install -r requirements.txt

python manage.py migrate

python manage.py createsuperuser

python manage.py runserver

teremos http://127.0.0.1:8000/
(essa é a tela de login do sistema)

http://127.0.0.1:8000/admin
(essa é a tela de administração)

http://127.0.0.1:8000/api
(onde buscamos os endpoints)
