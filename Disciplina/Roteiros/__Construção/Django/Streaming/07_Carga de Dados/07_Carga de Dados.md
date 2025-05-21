# 07 - **Cargas de Dados**


## ✅ 1. Estrutura do JSON (`contents.json`)

Salve este conteúdo como `contents.json` na raiz do projeto ou em um diretório de sua escolha:

```json
[
  {
    "username": "criador1",
    "title": "Título Vídeo 1",
    "description": "Descrição do vídeo 1",
    "content_type": "video",
    "file_url": "https://example.com/media/video1.mp4",
    "thumbnail_url": "https://example.com/media/thumb1.jpg"
  },
  {
    "username": "criador2",
    "title": "Título Áudio 2",
    "description": "Descrição do áudio 2",
    "content_type": "audio",
    "file_url": "https://example.com/media/audio2.mp3",
    "thumbnail_url": "https://example.com/media/thumb2.jpg"
  }
]
```

---

## ✅ 2. Comando Customizado Adaptado

Crie o comando:

📁 `seu_app/management/commands/load_contents_json.py`

```python
import json
from django.core.management.base import BaseCommand
from content.models import Content
from django.contrib.auth.models import User
from pathlib import Path

class Command(BaseCommand):
    help = 'Carrega conteúdos a partir de um arquivo JSON'

    def add_arguments(self, parser):
        parser.add_argument('json_path', type=str, help='Caminho para o arquivo JSON')

    def handle(self, *args, **kwargs):
        json_path = kwargs['json_path']
        json_file = Path(json_path)

        if not json_file.exists():
            self.stderr.write(self.style.ERROR(f"Arquivo não encontrado: {json_path}"))
            return

        with open(json_file, 'r', encoding='utf-8') as f:
            data = json.load(f)

        for item in data:
            try:
                user = User.objects.get(username=item['username'])
                Content.objects.create(
                    title=item['title'],
                    description=item['description'],
                    content_type=item['content_type'],
                    file_url=item['file_url'],
                    thumbnail_url=item['thumbnail_url'],
                    owner=user
                )
                self.stdout.write(self.style.SUCCESS(f"Conteúdo criado: {item['title']}"))
            except User.DoesNotExist:
                self.stderr.write(self.style.WARNING(f"Usuário não encontrado: {item['username']}"))
            except Exception as e:
                self.stderr.write(self.style.ERROR(f"Erro ao criar conteúdo: {e}"))

        self.stdout.write(self.style.SUCCESS('Importação finalizada.'))
```

---

## ✅ 3. Executar o Comando

Coloque o arquivo `contents.json` no diretório do projeto ou informe o caminho correto.

Execute com:

```bash
python manage.py load_contents_json contents.json
```
