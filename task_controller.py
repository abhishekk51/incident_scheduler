from incident_apps.serializers.incedent_serializer import IncidentSerializer


class TaskController:

    def create_task(self, payload):

        serializer = IncidentSerializer(data=payload)
        if serializer.is_valid():
            serializer.save()
            return True, None
        else:
            return False, serializer.errors
