from django.conf.urls import include, url
from django.contrib import admin


def trigger_error(request):
    division_by_zero = 1 / 0


urlpatterns = [
    url(r"^sentry-debug/$", trigger_error),
    url("admin/", admin.site.urls),
    url(r"^store/", include("store.urls")),
]
