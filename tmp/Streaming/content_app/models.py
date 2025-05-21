from django.db import models
from django.contrib.auth.models import User

class Content(models.Model):
    CONTENT_TYPES = [
        ('audio', 'Áudio'),
        ('video', 'Vídeo'),
    ]
    
    
    title = models.CharField(max_length=255)
    description = models.TextField()
    file_url = models.URLField()
    thumbnail_url = models.URLField(blank=True, null=True)
    content_type = models.CharField(max_length=10, choices=CONTENT_TYPES)
    upload_date = models.DateTimeField(auto_now_add=True)
    views = models.IntegerField(default=0)
    likes = models.IntegerField(default=0)
    is_public = models.BooleanField(default=True)
    status = models.CharField(max_length=20, default='published')
    creator = models.ForeignKey(User, related_name='contents', on_delete=models.CASCADE)

    def __str__(self):
        return self.title
    

 
# criar um relacionamento manytomany
class Playlist(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField()
    contents = models.ManyToManyField(Content)

    def __str__(self):
        return self.title

"""
# criar um relacionamento onetomany
#criar um relacionamento onetoone
class Comment(models.Model):
    content = models.ForeignKey(Content, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    text = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

# 1. ASSOCIAÇÃO (Association) - Relacionamento mais básico onde objetos podem se comunicar
class Like(models.Model):
    content = models.ForeignKey(Content, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)

# 2. AGREGAÇÃO (Aggregation) - Relação "tem-um" onde o objeto parte pode existir sem o todo
class ViewHistory(models.Model):
    content = models.ForeignKey(Content, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)

# 3. COMPOSIÇÃO (Composition) - Relação "parte-de" onde a parte não existe sem o todo
  

# 4. HERANÇA (Inheritance) - Relação "é-um" (especialização)


# 5. DEPENDÊNCIA (Dependency) - Uma classe depende de outra para realizar uma operação
  

# 6. REALIZAÇÃO (Realization) - Implementação de interface (em Python, usamos ABC)
       

# 7. ASSOCIAÇÃO BIDIRECIONAL (Bidirectional Association)

    def __str__(self):
        return self.text 
        
"""
