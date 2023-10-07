from .views import *
from django.urls import path
from . import views

urlpatterns = [
    path('', index, name='index'),
    path('blog/', index2, name='index2'),
    path('blog2/', index3, name='index3'),
    path('categ/<int:catid>/', views.categ, name='categ')
]