from rest_framework import generics
from .models import PC
from .serializers import PCSerializer


class PCListCreateAPIView(generics.ListCreateAPIView):
    queryset = PC.objects.all()
    serializer_class = PCSerializer


class PCDetailAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = PC.objects.all()
    serializer_class = PCSerializer
