from django.urls import path
from .views import index,lessonfour,top_sellers

urlpatterns =[
    path('',index, name = 'main-page'),
    path('lesson4/',lessonfour),
    path('top-sellers/',top_sellers, name = 'top-sellers')
]
