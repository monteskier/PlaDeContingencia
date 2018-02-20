from django.urls import path
from . import views
urlpatterns = [
    path('',views.index, name='index'),
    path('<int:servei_id>/test', views.test, name="test"),
    path('<int:servei_id>/getSeguimentsServei', views.getSeguimentsServei, name="getSeguimentsServei"),
    path('<int:servei_id>/', views.getSeguimentsActiu, name="getSeguimentsActiu"),
]
