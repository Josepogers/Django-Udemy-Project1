from recipes.views import home, contato, sobre
from django.urls import path

#Client: HTTP request <- server return a HTTP response

urlpatterns = [
    path('', home),
    path('contato', contato),
    path('sobre', sobre)
]