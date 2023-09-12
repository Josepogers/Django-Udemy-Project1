from recipes.views import home
from django.urls import path

#Client: HTTP request <- server return a HTTP response

urlpatterns = [
    path('', home),
]