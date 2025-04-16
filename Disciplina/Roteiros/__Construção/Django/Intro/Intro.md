# Introdução ao Django

Roteiro para Desenvolvimento de Aplicação Web Django com SQLite no VS Code

## Pré-requisitos

- Visual Studio Code instalado
- Python instalado (versão 3.8 ou superior)
- Extensão Python para VS Code (recomendado)

## Passo 1: Configurar Ambiente Virtual

1. Abra o terminal no VS Code (`Ctrl+` ou Terminal > Novo Terminal)
2. Navegue até a pasta onde deseja criar o projeto
3. Crie o ambiente virtual:

   ```
   ctrl +shift + P
   Python Create Enviroment
   ```

ou 

   ```bash
   python -m venv venv
   ```

4. Ative o ambiente virtual:
   - Windows:

     ```bash
     .\venv\Scripts\activate
     ```

   - Linux/MacOS:

     ```bash
     source venv/bin/activate
     ```

5. Verifique que o ambiente está ativo (deve aparecer `(venv)` no início da linha do terminal)

## Passo 2: Instalar Django e Dependências

1. Com o ambiente virtual ativo, instale o Django:

   ```bash
   pip install django
   ```

## Passo 3: Criar Projeto Django

1. Crie o projeto Django:

   ```bash
   django-admin startproject myproject .
   ```

   (O ponto no final cria o projeto no diretório atual)

2. Verifique a estrutura criada:

   ```
   myproject/
     __init__.py
     settings.py
     urls.py
     wsgi.py
   manage.py
   ```

## Passo 4: Configurar o Banco de Dados SQLite

1. O Django já vem configurado para usar SQLite por padrão (verifique em `myproject/settings.py`):

   ```python
   DATABASES = {
       'default': {
           'ENGINE': 'django.db.backends.sqlite3',
           'NAME': BASE_DIR / 'db.sqlite3',
       }
   }
   ```

2. Execute as migrações iniciais:

   ```bash
   python manage.py migrate
   ```

## Passo 5: Criar uma Aplicação Django

1. Crie uma nova aplicação:

   ```bash
   python manage.py startapp minhaapp
   ```

2. Adicione a aplicação ao `INSTALLED_APPS` em `myproject/settings.py`:

   ```python
   INSTALLED_APPS = [
       ...
       'minhaapp',
   ]
   ```

## Passo 6: Configurar URLs e Views Básicas

1. Crie um arquivo `urls.py` na pasta `minhaapp`:

   ```python
   from django.urls import path
   from . import views

   urlpatterns = [
       path('', views.home, name='home'),
   ]
   ```

2. Inclua as URLs da aplicação no projeto principal (`myproject/urls.py`):

   ```python
   from django.contrib import admin
   from django.urls import path, include

   urlpatterns = [
       path('admin/', admin.site.urls),
       path('', include('minhaapp.urls')),
   ]
   ```

3. Crie uma view básica em `minhaapp/views.py`:

   ```python
   from django.shortcuts import render
   from django.http import HttpResponse

   def home(request):
       return HttpResponse("Bem-vindo ao meu site!")
   ```

## Passo 7: Criar Modelos e Migrações

1. Defina um modelo em `minhaapp/models.py`:

   ```python
   from django.db import models

   class Produto(models.Model):
       nome = models.CharField(max_length=100)
       preco = models.DecimalField(max_digits=6, decimal_places=2)
       descricao = models.TextField()
       disponivel = models.BooleanField(default=True)

       def __str__(self):
           return self.nome
   ```

2. Crie e aplique as migrações:

   ```bash
   python manage.py makemigrations
   python manage.py migrate
   ```

## Passo 8: Configurar o Painel de Administração

1. Crie um superusuário:

   ```bash
   python manage.py createsuperuser
   ```

2. Registre o modelo no admin (`minhaapp/admin.py`):

   ```python
   from django.contrib import admin
   from .models import Produto

   admin.site.register(Produto)
   ```

## Passo 9: Executar o Servidor de Desenvolvimento

1. Inicie o servidor:

   ```bash
   python manage.py runserver
   ```

2. Acesse no navegador:

   - http://localhost:8000/ (página inicial)
   - http://localhost:8000/admin/ (painel admin)
