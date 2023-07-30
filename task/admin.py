from django.contrib import admin

from task.models import Status, Task, UserTasks, Profile

# Register your models here.
class TaskInlines(admin.TabularInline):
    model = UserTasks
    extra = 0


@admin.register(Task)
class TaskAdmin(admin.ModelAdmin):
    list_display = ['title', 'owner', 'created_at']
    inlines = [TaskInlines, ]


@admin.register(Status)
class StatusAdmin(admin.ModelAdmin):

    pass

@admin.register(Profile)
class User(admin.ModelAdmin):
    pass