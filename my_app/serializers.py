from rest_framework import serializers
from my_app.models import *


class GYMSerializer(serializers.ModelSerializer):
    class Meta:
        model = GYM
        fields = "__all__"


class TrainerSerializer(serializers.ModelSerializer):
  
    class Meta:
        model = Trainer
        fields = "__all__"

class ClientSerializer(serializers.ModelSerializer):
  
    class Meta:
        model = Client
        fields = "__all__"

class WorkoutSessionSerializer(serializers.ModelSerializer):
  
    class Meta:
        model = WorkoutSession
        fields = "__all__"