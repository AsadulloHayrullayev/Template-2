from django.urls import path # type: ignore
from . import views

urlpatterns = [
    path('',views.index_view, name ='index'),
    path('',views.holder_view, name='holder')
]