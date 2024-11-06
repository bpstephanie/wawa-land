from django.views import generic
from django.views.generic import TemplateView
from .models import Event

class EventList(generic.ListView):
    queryset = Event.objects.all()
    template_name = "event_list.html"
    paginate_by = 12