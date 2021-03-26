from django.shortcuts import render
from rest_framework import generics
from .serializer import EntrySerializer
from .models import Entry
from rest_framework.permissions import IsAuthenticatedOrReadOnly

# Create your views here.
class EntryList(generics.ListCreateAPIView):
    permission_classes = (IsAuthenticatedOrReadOnly,)
    queryset = Entry.objects.all()
    serializer_class = EntrySerializer

class EntryDetail(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = (IsAuthenticatedOrReadOnly,)
    queryset = Entry.objects.all()
    serializer_class = EntrySerializer