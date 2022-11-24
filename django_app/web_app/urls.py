from django.conf import settings
from django.contrib import admin
from django.urls import include, path
from drf_yasg import openapi
from drf_yasg.views import get_schema_view
from rest_framework import permissions, routers
from rest_framework.authtoken import views

router = routers.DefaultRouter()

schema_view = get_schema_view(
    openapi.Info(title="TODO API", default_version="v1"),
    public=True,
    permission_classes=(permissions.AllowAny, permissions.BasePermission),
)

urlpatterns = [
    path("admin/", admin.site.urls),
    path("api/", include("notes.urls")),
    path("token-auth/", views.obtain_auth_token),
]

if settings.DEBUG:
    urlpatterns += [
        path("api/docs/", schema_view.with_ui(), name="schema-swagger-ui"),
    ]
