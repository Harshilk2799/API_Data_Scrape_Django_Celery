from django.contrib import admin
from .models import Comments
# Register your models here.

@admin.register(Comments)
class CommentsModelAdmin(admin.ModelAdmin):
    list_display = ["id", "name", "email", "description"]