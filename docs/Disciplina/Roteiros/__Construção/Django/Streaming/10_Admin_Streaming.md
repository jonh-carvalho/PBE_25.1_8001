# 10 - **Django Admin**

## Introdução

O **Django Admin** é uma ferramenta robusta e personalizável, que permite gerenciar os dados do banco e configurar o backend da aplicação através de uma interface administrativa. A seguir, estão algumas das principais características de personalização do Django Admin, que tornam a ferramenta ainda mais poderosa para desenvolvedores e administradores:

### 1. **ModelAdmin: Customização de Exibição dos Modelos**

Através do `ModelAdmin`, você pode controlar a forma como cada modelo é exibido no Django Admin. Algumas personalizações incluem:

- **`list_display`**: Define os campos que serão exibidos na lista de registros do modelo. Por exemplo:

```python
class ContentAdmin(admin.ModelAdmin):
    list_display = ('title', 'content_type', 'is_public')
```

- **`list_filter`**: Adiciona filtros laterais para facilitar a segmentação dos registros. Exemplo:

```python
list_filter = ('content_type', 'is_public')
```

- **`search_fields`**: Permite adicionar um campo de busca para procurar registros específicos. Exemplo:

```python
search_fields = ('title', 'description')
```

### 2. **Campos de Ordenação**

Com a opção `ordering`, você pode definir a ordem padrão em que os registros serão exibidos.

```python
ordering = ['-updated_at']
```

### 3. **Campos de Edição Inline**

Django Admin permite editar objetos relacionados dentro de um formulário de outro objeto, usando **inlines**. Por exemplo, se você tem um modelo `Comment` relacionado a um `Content`, pode configurar o `Comment` como inline no `ContentAdmin`.

```python
class CommentInline(admin.TabularInline):
    model = Comment
    extra = 1  # Número de campos de comentário exibidos inicialmente

class ContentAdmin(admin.ModelAdmin):
    inlines = [CommentInline]
```

### 4. **Personalização dos Formulários de Edição**

Você pode definir quais campos serão exibidos na página de edição, bem como organizá-los em seções:

- **`fields`**: Define os campos que estarão disponíveis no formulário.
  
```python
fields = ('title', 'description', 'file_url', 'thumbnail_url')
```

- **`fieldsets`**: Agrupa os campos em seções, permitindo adicionar cabeçalhos de seção:

```python
fieldsets = (
    ('Informações Básicas', {'fields': ('title', 'description')}),
    ('Detalhes do Arquivo', {'fields': ('file_url', 'thumbnail_url')}),
  )
```

### 5. **Ações Personalizadas**

Com o Django Admin, você pode definir ações customizadas para executar operações em lote nos registros selecionados. Por exemplo, uma ação para marcar conteúdos como públicos:

```python
def make_public(modeladmin, request, queryset):
    queryset.update(is_public=True)
    make_public.short_description = "Marcar conteúdos como públicos"

class ContentAdmin(admin.ModelAdmin):
    actions = [make_public]
```

### 6. **Filtros e Campos de Busca Personalizados**

Além dos filtros de lista, você pode criar filtros personalizados para necessidades específicas e adicionar campos de busca dinâmicos.

- **Filtros Personalizados**: Use o `SimpleListFilter` para definir filtros avançados.
  
```python
from django.contrib.admin import SimpleListFilter

class PublicContentFilter(SimpleListFilter):
    title = 'public'
    parameter_name = 'is_public'

    def lookups(self, request, model_admin):
        return [('yes', 'Public'), ('no', 'Private')]

    def queryset(self, request, queryset):
        if self.value() == 'yes':
            return queryset.filter(is_public=True)
        if self.value() == 'no':
            return queryset.filter(is_public=False)

class ContentAdmin(admin.ModelAdmin):
    list_filter = (PublicContentFilter,)
```

### 7. **Edição em Lote**

A edição em lote facilita a atualização rápida de registros selecionados ao permitir que se aplique ações de uma só vez.

### 8. **Customização de Templates e CSS**

O Django permite que você substitua os templates do admin ou altere o CSS para refletir um estilo específico, modificando o visual da interface administrativa.

### Exemplo Completo

```python
from django.contrib import admin
from .models import Content, Comment

class CommentInline(admin.TabularInline):
    model = Comment
    extra = 1

class ContentAdmin(admin.ModelAdmin):
    list_display = ('title', 'content_type', 'is_public')
    list_filter = ('content_type', 'is_public')
    search_fields = ('title', 'description')
    ordering = ['-updated_at']
    inlines = [CommentInline]
    actions = [make_public]
    fieldsets = (
        ('Informações Básicas', {'fields': ('title', 'description')}),
        ('Detalhes do Arquivo', {'fields': ('file_url', 'thumbnail_url')}),
    )

admin.site.register(Content, ContentAdmin)
```

Com essas configurações, o Django Admin se torna uma interface poderosa para a administração do seu app de streaming, com filtros, personalizações e uma aparência adaptada ao fluxo de trabalho. Isso otimiza o gerenciamento de conteúdo, facilitando a navegação e a organização dos registros.

### 9. **Permissões e Controle de Acesso**

O Django Admin permite definir permissões específicas por modelo e campo, como:

- **Permissões por modelo**: No `ModelAdmin`, você pode restringir quem pode visualizar, adicionar, editar ou excluir registros.
- **Controle de campos específicos**: Restringe quem pode ver ou editar campos específicos. Isso é feito criando métodos como `has_change_permission`.


---

## 🧩 **Modelo Content (exemplo base)**

```python
# models.py
from django.db import models
from django.contrib.auth.models import User

class Content(models.Model):
    CONTENT_TYPE_CHOICES = (
        ('audio', 'Áudio'),
        ('video', 'Vídeo'),
    )

    title = models.CharField(max_length=255)
    description = models.TextField()
    file_url = models.URLField()
    thumbnail_url = models.URLField()
    content_type = models.CharField(max_length=10, choices=CONTENT_TYPE_CHOICES)
    created_at = models.DateTimeField(auto_now_add=True)
    owner = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.title
```

---

## 🛠️ **Admin personalizado**

```python
# admin.py
from django.contrib import admin
from .models import Content

@admin.register(Content)
class ContentAdmin(admin.ModelAdmin):
    list_display = ('title', 'owner', 'content_type', 'created_at')
    list_filter = ('content_type', 'created_at')
    search_fields = ('title', 'description')

    def has_view_permission(self, request, obj=None):
        return request.user.has_perm("app.view_content") or request.user.is_superuser

    def has_add_permission(self, request):
        return request.user.groups.filter(name='Criadores').exists()

    def has_change_permission(self, request, obj=None):
        if obj and obj.owner != request.user and not request.user.is_superuser:
            return False
        return True

    def has_delete_permission(self, request, obj=None):
        return request.user.is_superuser

    def get_fields(self, request, obj=None):
        fields = ['title', 'description', 'file_url', 'thumbnail_url', 'content_type']
        if request.user.is_superuser:
            fields.append('owner')
        return fields

    def get_readonly_fields(self, request, obj=None):
        readonly = ['created_at']
        if not request.user.is_superuser:
            readonly.extend(['owner'])
        return readonly

    def save_model(self, request, obj, form, change):
        if not obj.pk:  # Se for criação
            obj.owner = request.user
        super().save_model(request, obj, form, change)
```

---

## ✅ Regras aplicadas:

* Apenas usuários do grupo "Criadores" podem adicionar.
* Somente o **criador do conteúdo** ou um **superusuário** pode editar.
* Apenas **superusuários** podem excluir conteúdos.
* Campos como `owner` e `created_at` são apenas leitura.
* Filtros e buscas estão ativados por `content_type`, `created_at`, `title`, `description`.

---

