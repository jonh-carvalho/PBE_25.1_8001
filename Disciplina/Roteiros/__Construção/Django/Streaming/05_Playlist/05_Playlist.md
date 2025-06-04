# 05 - Playlist -Relacionamento NxN

## Playlist

Para criar o modelo `Playlist` conforme a modelagem mencionada, ele deve ter relacionamentos com as classes `Content` e `User`. A `Playlist` representará uma coleção de conteúdos (áudios ou vídeos) que pertence a um usuário específico.

Abaixo está o código para definir o modelo `Playlist` no Django, assumindo que você já possui as classes `Content` e `User` configuradas.

### Modelo `Playlist`

```python
from django.db import models
from django.contrib.auth.models import User
from content.models import Content  # Assumindo que o modelo Content está no app 'content'

class Playlist(models.Model):
    title = models.CharField(max_length=255)  # Título da playlist
    description = models.TextField(blank=True, null=True)  # Descrição opcional da playlist
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='playlists')  # Proprietário da playlist
    contents = models.ManyToManyField(Content, related_name='playlists')  # Conteúdos incluídos na playlist
    created_at = models.DateTimeField(auto_now_add=True)  # Data de criação
    updated_at = models.DateTimeField(auto_now=True)  # Data de última atualização

    class Meta:
        ordering = ['-created_at']
        verbose_name = 'Playlist'
        verbose_name_plural = 'Playlists'

    def __str__(self):
        return self.title
```

### Explicação dos Campos

1. **`title`**: Nome da playlist.
2. **`description`**: Descrição opcional, para explicar o propósito da playlist ou a seleção de conteúdos.
3. **`user`**: Chave estrangeira que faz referência ao modelo `User`, representando o dono da playlist.
4. **`contents`**: Relacionamento `ManyToMany` com `Content`, permitindo que vários conteúdos sejam adicionados à playlist.
5. **`created_at`** e **`updated_at`**: Campos de data para registrar a criação e a última atualização da playlist.

### Exemplo de Uso no Django Shell

Com esse modelo, é possível realizar operações no Django Shell para criar playlists, adicionar conteúdos e verificar quais playlists pertencem a um usuário ou contêm um conteúdo específico.

```bash
python manage.py shell
```

```python
from content.models import Content
from myapp.models import Playlist  # Substitua 'myapp' pelo nome do seu app
from django.contrib.auth.models import User

# Criando um usuário para teste
user = User.objects.create(username="testuser")

# Criando alguns conteúdos
content1 = Content.objects.create(title="Video 1", file_url="https://example.com/video1.mp4")
content2 = Content.objects.create(title="Audio 1", file_url="https://example.com/audio1.mp3")

# Criando uma playlist e adicionando conteúdos
playlist = Playlist.objects.create(title="Minha Playlist", user=user)
playlist.contents.add(content1, content2)

# Verificando os conteúdos na playlist
for content in playlist.contents.all():
    print(content.title)
```

Com essa estrutura, você pode facilmente gerenciar playlists associadas a conteúdos e usuários.
