from django.contrib import admin

from shop.models import Item

# admin.site.register(Post)


@admin.register(Item)
class ItemAdmin(admin.ModelAdmin):
    list_display = ["name", "desc", "created_at", "updated_at"]