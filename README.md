🐾 PetGuard — Sistema de Gerenciamento de Animais

PetGuard é um sistema web desenvolvido com Django, HTML, CSS e JavaScript, projetado para facilitar o cadastro, controle e acompanhamento de animais.
A aplicação permite que usuários e administradores registrem informações detalhadas sobre cada animal, como espécie, raça, idade, status e observações, oferecendo uma interface moderna, intuitiva e responsiva.

⚙️ Funcionalidades principais

🐕 Cadastro de animais:
Registre animais com apelido, espécie, raça, idade (anos e meses), status e observações.
É possível adicionar novas raças diretamente durante o cadastro.

📋 Listagem e busca:
Visualize todos os animais cadastrados em uma tabela dinâmica.
Utilize a barra de pesquisa para buscar por apelido, com filtros por espécie, raça e status.

🎨 Interface moderna:
Design limpo e adaptável, com botões e ícones intuitivos.
Filtros de status representados por bolinhas coloridas:

🟢 Disponível

🟠 Em tratamento

🔴 Adotado

🔐 Controle de acesso:
Usuários autenticados podem acessar o sistema; administradores têm permissões ampliadas para cadastro e gerenciamento.

🗂️ Administração Django:
Painel administrativo completo para gerenciar espécies, raças e animais com poucos cliques.
Autenticação: djangorestframework-simplejwt

------------------------------------------------

🛠️ *Tecnologias Utilizadas*
Backend: Python, HTML, Css, Javascript, Django, Django REST Framework

Servidor de Aplicação: Django (Python manage.py runserver)


Banco de Dados: SQLITE (Teste)

Documentação: drf-spectacular

Admin: django-jazzmin


<img width="150" height="150" alt="Python-logo-notext svg" src="https://github.com/user-attachments/assets/50b2cf26-6a19-408a-b1a7-f37d1782beb5" />

<img width="250" height="250" alt="1710173183065" src="https://github.com/user-attachments/assets/884e24b8-9ee2-4e02-b860-5efcc8a04703" />

<img width="250" height="250" alt="image" src="https://github.com/user-attachments/assets/9059ee60-7d9b-4660-8a73-514b659b4f48" />

--------------------------------------------------
Pré-requisitos:
Python

Django

IDE

Git

--------------------------------------------------
(BRANCH MAIN!)

(TUDO A BAIXO PRECISA SER DIGITADO NO TERMINAL)


git clone -b main https://github.com/cdantass/petguard.git

no mesmo nível do manage.py(arquivo do backend), rodar:

pip install -r requirements.txt

python manage.py makemigrations

python manage.py migrate

python manage.py createsuperuser

python manage.py runserver

teremos http://127.0.0.1:8000/
(essa é a tela de login do sistema)

http://127.0.0.1:8000/admin
(essa é a tela de administração)

http://127.0.0.1:8000/api
(onde buscamos os endpoints)
