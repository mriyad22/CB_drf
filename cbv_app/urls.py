from django.urls import path
from .views import *


urlpatterns = [
    path("all-data/", PersionApiView.as_view(), name="data"),
    path("detail/<int:pk>/", PersionDetailApiView.as_view(), name="detail"),
]
