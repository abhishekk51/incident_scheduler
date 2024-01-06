from rest_framework import serializers
from incident_apps.models.task import Incidents, Handler


class HandlerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Handler
        fields = '__all__'


class IncidentSerializer(serializers.ModelSerializer):
    assigned_to = HandlerSerializer(read_only=True)

    class Meta:
        model = Incidents
        fields = '__all__'


class IncidentStatusUpdateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Incidents
        fields = ['status']


