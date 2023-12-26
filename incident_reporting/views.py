# incident_reporting/views.py

from django.shortcuts import render
from .models import Incident

def incident_list(request):
    incidents = Incident.objects.all()
    return render(request, 'incident_reporting/incident_list.html', {'incidents': incidents})

# Ajoutez d'autres vues pour la création, la mise à jour, la suppression des signalements, etc.
