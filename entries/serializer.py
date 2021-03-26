from rest_framework import serializers
from .models import Entry

class EntrySerializer(serializers.ModelSerializer):
    class Meta:
        fields = ('id','owner','classification','tier','created_at')
        model = Entry