from django.shortcuts import render, get_object_or_404
from django.views import generic
from django.views.generic import TemplateView, ListView, View
from .models import Post

# Create your views here.
class Home(TemplateView):
    template_name = 'index.html'

class PostList(generic.ListView):
    queryset = Post.objects.filter(status=1)
    template_name = "blog.html"
    paginate_by = 6

def post_detail(request, slug):
    """
    Display an individual :model:`blog.Post`.

    **Context**

    ``post``
        An instance of :model:`blog.Post`.

    **Template:**

    :template:`blog/post_detail.html`
    """

    queryset = Post.objects.filter(status=1)
    post = get_object_or_404(queryset, slug=slug)

    return render(
        request,
        "blog/post_detail.html",
        {"post": post},
    )

