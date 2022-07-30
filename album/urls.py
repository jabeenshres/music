from django.urls import path,include

from .views import AlbumCreateView

app_name ="album"

urlpatterns = [
      path("create/", AlbumCreateView.as_view(), name='create'),
]