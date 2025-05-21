from django.contrib import admin
from content_app.models import Content

class ContentAdmin(admin.ModelAdmin):
    list_display = ('title', 'content_type', 'is_public')
    list_filter = ('content_type', 'is_public', 'upload_date')
    search_fields = ('title', 'description')
    ordering = ['-upload_date']
    fieldsets = (
    ('Informações Básicas', {'fields': ('title', 'description')}),
    ('Detalhes do Arquivo', {'fields': ('file_url', 'thumbnail_url')}),
    ('Configurações', {'fields': ('content_type', 'is_public', 'status')}),
    ('Interações', {'fields': ('views', 'likes')}),
    ('Criador', {'fields': ('creator',)})
  )

admin.site.register(Content, ContentAdmin)