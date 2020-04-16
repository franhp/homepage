from django.contrib import admin

from bookmarks.models import Bookmark, Category


class CustomBookmark(admin.ModelAdmin):
    list_display = (
        "name",
        "link_type",
        "url",
        "year",
    )
    list_filter = ("link_type",)


class CustomCategory(admin.ModelAdmin):
    list_display = ("name", "slug", "order")


admin.site.register(Bookmark, CustomBookmark)
admin.site.register(Category, CustomCategory)
