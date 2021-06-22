from django.contrib.admin import ModelAdmin, register

from pypro.aperitivos.models import Video


@register(Video)
class VideoAdmin(ModelAdmin):
    list_display = ('titulo', 'slug', 'created_at', 'youtube_id')
    ordering = ('created_at',)
    prepopulated_fields = {'slug': ('titulo',)}
