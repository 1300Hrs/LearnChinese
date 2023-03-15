from django.contrib import admin
from .models import Lesson, Reading, Listening


class LessonAdmin(admin.ModelAdmin):
    list_display = ("title", "description", "created_at", "updated_at")


class ReadingAdmin(admin.ModelAdmin):
    list_display = ("title", "chinese_characters", "audio_clip",)


class ListeningAdmin(admin.ModelAdmin):
    list_display = ("phrase", "hanzi", "yingzi", "audio_clip")


# Register your models here.
admin.site.register(Lesson, LessonAdmin)
admin.site.register(Reading, ReadingAdmin)
admin.site.register(Listening, ListeningAdmin)
