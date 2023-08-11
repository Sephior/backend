from django.contrib import admin
from .models import Feed

# Register your models here.
@admin.register(Feed)
class FeedAdmin(admin.ModelAdmin):
    list_display = ['id', 'content', 'content_length', 'created_at', 'updated_at', 'like', 'unlike']
    list_display_links = ['content']