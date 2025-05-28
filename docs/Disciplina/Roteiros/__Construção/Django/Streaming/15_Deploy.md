# 15 - Deploy

O **deploy mais simples** de um projeto **Django REST com SQLite** é usando o **[Render.com](https://render.com/)** — ideal para testes, MVPs ou protótipos.

---

## ✅ 1. **Pré-requisitos**

* Conta no [GitHub](https://github.com/)
* Conta no [Render](https://render.com/)
* Projeto Django REST funcional (com `requirements.txt`, `manage.py`, etc.)

---

## ✅ 2. **Prepare o projeto Django**

### 2.1. Instale pacotes necessários:

```bash
pip install gunicorn dj-database-url python-dotenv
```

### 2.2. Adicione ao `requirements.txt`:

```bash
pip freeze > requirements.txt
```

### 2.3. Crie o arquivo `Procfile` (sem extensão):

```procfile
web: gunicorn nome_do_projeto.wsgi
```

Substitua `nome_do_projeto` pelo nome da pasta principal do seu Django (onde está o `settings.py`).

---

## ✅ 3. **Configurações no `settings.py`**

### 3.1. Altere `ALLOWED_HOSTS`:

```python
import os
ALLOWED_HOSTS = ['*']  # Em produção, use o domínio real
```

### 3.2. Use o SQLite apenas se quiser simplicidade (Render permite isso). Para uso mais sério, use PostgreSQL.

---

## ✅ 4. **Configurar arquivos estáticos**

No final do `settings.py`:

```python
STATIC_URL = '/static/'
STATIC_ROOT = os.path.join(BASE_DIR, 'staticfiles')
```

---

## ✅ 5. **Comitar no Git e subir no GitHub**

```bash
git init
git add .
git commit -m "first commit"
git remote add origin https://github.com/seuusuario/seurepo.git
git push -u origin main
```

---

## ✅ 6. **Criar app no Render**

1. Vá para [Render Dashboard](https://dashboard.render.com/)

2. Clique em **"New Web Service"**

3. Conecte-se ao GitHub e selecione o repositório

4. Configure:

   * **Name**: nome do app
   * **Runtime**: Python
   * **Build Command**: `pip install -r requirements.txt`
   * **Start Command**: `gunicorn nome_do_projeto.wsgi`
   * **Environment**: `Python 3`
   * **Environment Variables**:

     * `DJANGO_SECRET_KEY` = sua chave secreta
     * `DEBUG` = False
     * `PYTHON_VERSION` = 3.10 (ou similar)

5. Clique em **Create Web Service**

---

## ✅ 7. **Coletar arquivos estáticos e migrar banco**

Após o deploy, vá no painel do serviço → aba **Shell**:

```bash
python manage.py collectstatic --noinput
python manage.py migrate
```

---

## ✅ 8. **Acessar o site**

Seu app Django REST estará publicado no domínio `.onrender.com`.

---

## 📝 Observações

* O SQLite funciona, mas é **volátil**: ao reiniciar o container, os dados são perdidos.
* Para persistência real, use PostgreSQL (Render oferece serviço de banco gratuito).

---

