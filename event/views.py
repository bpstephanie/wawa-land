from django.shortcuts import render, get_object_or_404
from django.views import generic
from django.views.generic import TemplateView
from .models import Event

class EventList(generic.ListView):
    queryset = Event.objects.all()
    template_name = "event_list.html"
    paginate_by = 12

def event_detail(request, slug):
    """
    Display an individual :model:`event.Event`.

    **Context**

    ``event``
        An instance of :model:`event.Event`.

    **Template:**

    :template:`event/event_list.html`
    """

    queryset = Event.objects.all()
    event = get_object_or_404(queryset, slug=slug)

    return render(
        request,
        "event/event_detail.html",
        {"event": event},
    )