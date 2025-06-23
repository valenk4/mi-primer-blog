from django.urls import path
from . import views

urlpatterns = [
path('', views.artistas, name='artistas'),
path('pintor/<int:pk>/', views.detalle_pintor, name='detalle_pintor'),
]