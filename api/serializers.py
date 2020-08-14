from rest_framework import serializers
from .models import review


class ReviewSerializer(serializers.ModelSerializer):
    class Meta:
        model = review
        fields = ('productId', 'userId', 'profileName', 'helpfulness', 'score', 'time', 'summary', 'text')
        read_only_fields = ('productId', 'userId', 'profileName', 'helpfulness', 'score', 'time', 'summary', 'text')