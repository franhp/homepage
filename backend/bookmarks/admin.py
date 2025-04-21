from django.contrib import admin

from bookmarks.models import Bookmark, Category


@admin.register(Bookmark)
class CustomBookmark(admin.ModelAdmin):
    list_display = (
        "name",
        "link_type",
        "url",
        "year",
    )
    list_filter = ("link_type",)


@admin.register(Category)
class CustomCategory(admin.ModelAdmin):
    list_display = ("name", "slug", "order")
