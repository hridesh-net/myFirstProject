from rest_framework import serializers
from . models import Candidates

# class CandidatesSerializer(serializers.Serializer):
#     name = serializers.CharField()
#     email = serializers.EmailField()
#     phone = serializers.CharField()
#     date = serializers.DateField()

class CandidatesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Candidates
        fields = '__all__'