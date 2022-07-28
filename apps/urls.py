from django.urls import path
from .api import Hotel_List, Hotel_Detail

from rest_framework import permissions
from drf_yasg.views import get_schema_view
from drf_yasg import openapi


schema_view = get_schema_view(
   openapi.Info(
      title="Hotel API",
      default_version='v1',
      description="Hotel ",
      terms_of_service="https://www.google.com/policies/terms/",
    #   contact=openapi.Contact(email="contact@snippets.local"),
      license=openapi.License(name="BSD License"),
   ),
   public=True,
   permission_classes=[permissions.AllowAny],
)

urlpatterns = [
    path('hotel-list/', Hotel_List.as_view(), name='list'),
    path('hotel-detail/<int:pk>/', Hotel_Detail.as_view(), name='details'),
    path('swagger/', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),

]
