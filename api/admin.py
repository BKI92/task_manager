from django.contrib import admin
from .models import Task, History


class TaskAdmin(admin.ModelAdmin):
    list_display = (
        'id', 'author', 'title', 'description', 'created', 'status',)
    search_fields = ("title", "author")
    list_filter = ("created",)
    empty_value_display = '-пусто-'


class HistoryAdmin(admin.ModelAdmin):
    list_display = ('id', 'author', 'task', 'status', 'created')
    search_fields = ('id', 'task', 'status')
    list_filter = ('created',)


admin.site.register(Task, TaskAdmin)
admin.site.register(History, HistoryAdmin)
