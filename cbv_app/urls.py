from django.urls import path
from .views import *


urlpatterns = [
    path("all-data/", PersionApiView.as_view(), name="data"),
    path("all-data/<int:pk>/", PersionApiView.as_view(), name="data"),
]
