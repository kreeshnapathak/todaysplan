from rest_framework import fields, serializers
from .models import Plan

class PlanSerializers(serializers.ModelSerializer):
    class Meta:
        model=Plan
        fields=['id','item']