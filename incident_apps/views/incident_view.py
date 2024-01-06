from rest_framework import status
from rest_framework.generics import ListCreateAPIView, UpdateAPIView, CreateAPIView
from rest_framework.response import Response
from rest_framework.views import APIView

from incident_apps.controllers import prioritize_and_assign_incident, escalate_incedents, update_incident
from incident_apps.models.task import Incidents
from incident_apps.serializers.incedent_serializer import IncidentSerializer, HandlerSerializer


# using list and create api in same class. we can separate it to achieve more flexibility
class IncidentListCreateView(ListCreateAPIView):
    queryset = Incidents.objects.all()
    serializer_class = IncidentSerializer

    def create(self, request, *args, **kwargs):
        response = super().create(request, *args, **kwargs)
        prioritize_and_assign_incident()
        return response


class IncidentUpdateView(APIView):

    def put(self, request, pk, *args, **kwargs):
        data = request.data
        _status, response = update_incident(pk, data)
        return Response(response, status=status.HTTP_400_BAD_REQUEST if not _status else status.HTTP_200_OK)


class AddHandler(CreateAPIView):
    serializer_class = HandlerSerializer








