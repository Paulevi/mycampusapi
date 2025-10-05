from rest_framework.viewsets import ModelViewSet
from rest_framework import generics
from .models import Actu
from .api_serialiser import ActuSerializer



# Create your views here.

class ActuListCreateAPIView(generics.ListCreateAPIView):
    queryset = Actu.objects.all()
    serializer_class = ActuSerializer

class ActuRetrieveUpdateDestroyAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Actu.objects.all()
    serializer_class = ActuSerializer

class ActuViewSet(ModelViewSet):
    serializer_class = ActuSerializer
    def get_queryset(self):

        return Actu.objects.all()
