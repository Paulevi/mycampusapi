from django.urls import path
from .views import ActuListCreateAPIView, ActuRetrieveUpdateDestroyAPIView

urlpatterns = [
    path('actu/', ActuListCreateAPIView.as_view(), name='actu-list-create'),
    path('actu/<int:pk>/', ActuRetrieveUpdateDestroyAPIView.as_view(), name='actu-detail'),
]
