---
hide:
  - navigation
---

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

```bash
ctrl +shift + P
Python Create Enviroment
```

ou

   ```bash
   python -m venv venv
   ```

4./ Ative o ambiente virtual:

- Windows:

```bash
   .\venv\Scripts\activate
```

- Linux/MacOS:

```bash
   source venv/bin/activate
```

5./ Verifique que o ambiente está ativo (deve aparecer `(venv)` no início da linha do terminal)

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

2./ Verifique a estrutura criada:

   ```bash
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
   python manage.py startapp myapp
   ```

2. Adicione a aplicação ao `INSTALLED_APPS` em `myproject/settings.py`:

   ```python
   INSTALLED_APPS = [
       ...
       'myapp',
   ]
   ```

## Passo 6: Configurar URLs e Views Básicas

1. Crie um arquivo `urls.py` na pasta `myapp`:

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
       path('', include('myapp.urls')),
   ]
   ```

3. Crie uma view básica em `myapp/views.py`:

   ```python
   from django.shortcuts import render
   from django.http import HttpResponse

   def home(request):
       return HttpResponse("Bem-vindo ao meu site!")
   ```

## Passo 7: Criar Modelos e Migrações

1. Defina um modelo em `myapp/models.py`:

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

2. Registre o modelo no admin (`myapp/admin.py`):

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

## Passo 10: Adicionar Templates

1. Crie uma pasta `templates` dentro da pasta `myapp` e, dentro dela, outra pasta chamada `myapp` (ou seja, `myapp/templates/myapp`):

```bash
   mkdir templates
```

2. Crie um arquivo `base.html` na pasta `templates`:

```html
   <html>
      <head>
         <title>{% block title %}{% endblock %}</title>
      </head>
      <  body>
         {% block content %}{% endblock %}      
      </body></html>
```

3. Crie um arquivo `home.html` na pasta `myapp/templates/myapp`:  

```html
   <h1>Bem-vindo ao meu site!</h1>
```

4. Crie um arquivo `index.html` na pasta `templates`:

```html
   {% extends "base.html" %}
   {% block title %}Home{% endblock %}
   {% block content %}{% include "home.html" %}{% endblock %}
```

5. Certifique-se de incluir as URLs da aplicação no projeto principal (`myproject/urls.py`):

```python
   from django.contrib import admin
   from django.urls import path, include

   urlpatterns = [
       path('admin/', admin.site.urls),
       path('', include('myapp.urls')),
       path('api/', include('myapp.api_urls')),

   ]
```

## Passo 11: Adicionar urls para o template acima

```python
   from django.urls import path  

   urlpatterns = [
       path('', views.home, name='home'), 
   ]
```

## Passo 12: Adicionar Views para template acima

```python   
   from django.shortcuts import render 
   from django.http import HttpResponse   

   def home(request):   
       return render(request, 'index.html')  
```


11. Crie um arquivo `forms.py` na pasta `myapp`:

```python   
   from django import forms
   from .models import Produto   

   class ProdutoForm(forms.ModelForm):   
       class Meta:       
           model = Produto           
           fields = ['nome', 'preco', 'descricao', 'disponivel']   
```

12. Crie um arquivo `admin.py` na pasta `myapp`:

```python
   from django.contrib import admin    
   from .models import Produto       

   admin.site.register(Produto)   
```   

13. Crie um arquivo `tests.py` na pasta `myapp`:   

```python
   from django.test import TestCase
from .models import Produto

class ProdutoModelTest(TestCase):
    def setUp(self):
        Produto.objects.create(
            nome="Camiseta",
            preco=49.90,
            descricao="Camiseta 100% algodão",
            disponivel=True
        )

    def test_criacao_produto(self):
        produto = Produto.objects.get(nome="Camiseta")
        self.assertEqual(produto.preco, 49.90)
        self.assertTrue(produto.disponivel)
        self.assertEqual(str(produto), "Camiseta")
```   

14. Execute as migrações iniciais:

```bash
   python manage.py migrate
```   

15. Execute os testes:

```bash   
   python manage.py test
```      

16. Crie um arquivo `wsgi.py` na pasta `myproject`:

```python       
   from django.core.wsgi import get_wsgi_application   
   os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'myproject.settings')   
   application = get_wsgi_application()
```   

17. Crie um arquivo `settings.py` na pasta `myproject`:  
18. Crie um arquivo `urls.py` na pasta `myproject`:
19. Crie um arquivo `asgi.py` na pasta `myproject`:

```python   
   from django.core.asgi import get_asgi_application

   os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'myproject.settings')

   application = get_asgi_application()
```

20. Execute as migrações iniciais:

```bash
   python manage.py migrate
```

21. Execute os testes:

```bash   
   python manage.py test
```         