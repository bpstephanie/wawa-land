from django.shortcuts import render, get_object_or_404, reverse
from django.views import generic
from django.views.generic import TemplateView
from django.contrib import messages
from django.http import HttpResponseRedirect
from .models import Event, Review
from .forms import ReviewForm


class EventList(generic.ListView):
    """
    Display a list of events to the user
    """
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
    reviews = event.reviews.all().order_by("-created_on")
    review_count = event.reviews.filter(approved=True).count()
    if request.method == "POST":
        review_form = ReviewForm(data=request.POST)
        if review_form.is_valid():
            review = review_form.save(commit=False)
            review.author = request.user
            review.event = event
            review.save()
            messages.add_message(
                request, messages.SUCCESS,
                'Review submitted and awaiting approval')

    review_form = ReviewForm()

    return render(
        request,
        "event/event_detail.html",
        {
            "event": event,
            "reviews": reviews,
            "review_count": review_count,
            "review_form": review_form,
        },
    )


def review_edit(request, slug, review_id):
    """
    view to edit reviews
    """
    if request.method == "POST":

        queryset = Event.objects.all()
        event = get_object_or_404(queryset, slug=slug)
        review = get_object_or_404(Review, pk=review_id)
        review_form = ReviewForm(data=request.POST, instance=review)

        if review_form.is_valid() and review.author == request.user:
            review = review_form.save(commit=False)
            review.event = event
            review.approved = False
            review.save()
            messages.add_message(
                request, messages.SUCCESS, 'Review Updated!')
        else:
            messages.add_message(
                request, messages.ERROR, 'Error updating review!')

    return HttpResponseRedirect(reverse('event_detail', args=[slug]))


def review_delete(request, slug, review_id):
    """
    view to delete review
    """
    queryset = Event.objects.all()
    event = get_object_or_404(queryset, slug=slug)
    review = get_object_or_404(Review, pk=review_id)

    if review.author == request.user:
        review.delete()
        messages.add_message(request, messages.SUCCESS, 'Review deleted!')
    else:
        messages.add_message(
            request, messages.ERROR, 'You can only delete your own reviews!')

    return HttpResponseRedirect(reverse('event_detail', args=[slug]))
