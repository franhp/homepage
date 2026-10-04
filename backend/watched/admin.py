from django.contrib import admin, messages
from django.http import HttpResponseRedirect
from django.urls import path
from django.utils.decorators import method_decorator
from django.views.decorators.http import require_POST

from watched.models import Title
from watched.tracking import TrackingError


class TrackingMatchFilter(admin.SimpleListFilter):
    title = "Floppy match"
    parameter_name = "floppy_match"

    def lookups(self, request, model_admin):
        return (("unmatched", "Unmatched"), ("matched", "Matched"))

    def queryset(self, request, queryset):
        if self.value() == "unmatched":
            return queryset.filter(tracking_id__isnull=True)
        if self.value() == "matched":
            return queryset.exclude(tracking_id__isnull=True)
        return queryset


@admin.register(Title)
class CustomTitle(admin.ModelAdmin):
    list_display = (
        "name",
        "title_type",
        "tracking_status",
        "site_rating",
        "my_rating",
        "ranking_order",
    )
    list_filter = ("title_type", "tracking_status", TrackingMatchFilter)
    search_fields = ("name", "tracking_id")

    def get_urls(self):
        urls = super().get_urls()
        new_urls = [
            path("sync_tracking/", self.admin_site.admin_view(self.sync_tracking)),
        ]
        return new_urls + urls

    @method_decorator(require_POST)
    def sync_tracking(self, request):
        try:
            summary = Title.sync_tracking()
        except TrackingError as error:
            self.message_user(request, str(error), messages.ERROR)
        else:
            self.message_user(
                request,
                "Synchronized {fetched} titles from Floppy: {created} "
                "created, {updated} updated.".format(**summary),
                messages.SUCCESS,
            )
        return HttpResponseRedirect(request.headers.get("referer", "../"))
