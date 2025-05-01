from rest_framework import serializers
from .models import CandidateResponse

class CandidateResponseSerializer(serializers.Serializer):
    class Meta:
        model = CandidateResponse
        fields = '__all__'