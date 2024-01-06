import itertools

from django.db.models import Q, Count, F

from incident_apps.models.task import Incidents, Handler
from incident_apps.serializers.incedent_serializer import IncidentSerializer, IncidentStatusUpdateSerializer


def prioritize_and_assign_incident():
    incidents = Incidents.objects.filter(status="pending").order_by('-severity', '-timestamp')
    # Retrieve handlers who have not been assigned to any incident
    handlers = Handler.objects.annotate(
        unresolved_incidents=Count('incidents', filter=~Q(incidents__status='resolved'))
    ).filter(unresolved_incidents=0)
    print(handlers)
    handler_cycle = itertools.cycle(handlers)
    for incident in incidents:
        try:
            assigned_handler = next(handler_cycle)
            incident.assigned_to = assigned_handler
            incident.status = 'assigned'
            incident.save()
        except:
            break


def escalate_incedents():
    esc_incidents = Incidents.objects.filter(status='escalated')
    for esc_incident in esc_incidents:
        esc_incident.status = 'Pending'
        esc_incident.save()


def assign_pending_incident_to_handler(handler_id):
    incident = Incidents.objects.filter(status="pending").order_by('-severity', '-timestamp').first()
    handler = Handler.objects.annotate(
        unresolved_incidents=Count('incidents', filter=~Q(incidents__status='resolved'))
    ).filter(unresolved_incidents=0, id=handler_id.id).first()
    if handler and incident:
        incident.assigned_to = handler_id
        incident.save()
    else:
        prioritize_and_assign_incident()


def update_incident(incident_id, payload):

    incident = Incidents.objects.filter(id=incident_id).first()
    if incident is None:
        return False, {"error": "Incident not found"}

    serializer = IncidentStatusUpdateSerializer(incident, data=payload, partial=True)

    if not serializer.is_valid():
        return False, serializer.errors

    serializer.save()
    if payload.get('status') == "resolved" and incident.assigned_to:
        assign_pending_incident_to_handler(incident.assigned_to)

    return True, {}








