
from django.contrib import admin
from django.urls import path, include
from drf_yasg.views import get_schema_view
from drf_yasg import openapi
from .views import RootView
# Swagger UI
schema_view = get_schema_view(
   openapi.Info(
      title="Django API Hub",
      default_version='v1',
      description="APIs",
      terms_of_service="https://www.google.com/policies/terms/",
      contact=openapi.Contact(email="mhgn0001@gmail.com"),
      license=openapi.License(name="Public Licence"),
   ),
   public=True,
)

urlpatterns = [
    path('', RootView.as_view(), name='root'), 
    path('admin/', admin.site.urls),
    path('authentication/', include('authentication.urls')),
    path('swagger/', schema_view.with_ui('swagger', cache_timeout=0), name='swagger-ui'),
]
