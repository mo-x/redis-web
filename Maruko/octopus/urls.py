from django.urls import path

from . import views

urlpatterns = [
    # ex: /polls/
    path('keys', views.keys, name='keys'),
    path('db/size', views.db_size, name='db_size'),
    path('get/<str:key>', views.get_value, name="get_value"),
    path('set/<str:key>/<str:value>', views.set_value, name="set_value"),
]
