from django.shortcuts import render
from django.views.generic import TemplateView, ListView, View
from .models import Post

# Create your views here.
class Home(TemplateView):
    template_name = 'index.html'

class PostList(ListView):
    queryset = Post.objects.filter(status=1)
    template_name = "blog.html"
    paginate_by = 6

