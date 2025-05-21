from django.contrib import admin
from .models import Content

class ContentAdmin(admin.ModelAdmin):
    list_display = ('title', 'content_type', 'is_public', 'upload_date',  'file_url', 'thumbnail_url')
    list_filter = ('content_type', 'is_public', 'upload_date')
    search_fields = ('title', 'description')
    ordering = ['-upload_date']

    fieldsets = (
        ('Informações Básicas', {'fields': ('title', 'description')}),
        ('Detalhes do Arquivo', {'fields': ('file_url', 'thumbnail_url')}),
    )

admin.site.register(Content, ContentAdmin)