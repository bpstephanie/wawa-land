from django.shortcuts import render, get_object_or_404, reverse
from django.urls import reverse_lazy
from django.views import generic
from django.views.generic import TemplateView, ListView, View, CreateView
from django.contrib import messages
from django.http import HttpResponseRedirect
from slugify import slugify
from .models import Post, Comment
from .forms import CommentForm, PostForm

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
    """

    queryset = Post.objects.filter(status=1)
    post = get_object_or_404(queryset, slug=slug)
    comments = post.comments.all().order_by("-created_on")
    comment_count = post.comments.filter(approved=True).count()
    liked = False
    if request.user.is_authenticated:
        user = request.user
        if post.likes.filter(id=user.id).exists():
            liked = True

    if request.method == "POST":

        if request.user.is_authenticated:
            user = request.user

            if post.likes.filter(id=user.id).exists():
                post.likes.remove(user)
                messages.add_message(
                    request, messages.ERROR,
                    'You just unliked this post'
                )
            else:
                post.likes.add(user)
                liked = True
                messages.add_message(
                    request, messages.SUCCESS,
                    'You just liked this post'
                )



        comment_form = CommentForm(data=request.POST)
        if comment_form.is_valid():
            comment = comment_form.save(commit=False)
            comment.author = request.user
            comment.post = post
            comment.save()
            messages.add_message(
            request, messages.SUCCESS,
            'Comment submitted and awaiting approval'
        )

    comment_form = CommentForm()


    return render(
        request,
        "blog/post_detail.html",
        {
            "post": post,
            "comments": comments,
            "comment_count": comment_count,
            "comment_form": comment_form,
            "liked": liked,
        },
    )


def comment_edit(request, slug, comment_id):
    """
    view to edit comments
    """
    if request.method == "POST":

        queryset = Post.objects.filter(status=1)
        post = get_object_or_404(queryset, slug=slug)
        comment = get_object_or_404(Comment, pk=comment_id)
        comment_form = CommentForm(data=request.POST, instance=comment)

        if comment_form.is_valid() and comment.author == request.user:
            comment = comment_form.save(commit=False)
            comment.post = post
            comment.approved = False
            comment.save()
            messages.add_message(request, messages.SUCCESS, 'Comment Updated!')
        else:
            messages.add_message(request, messages.ERROR, 'Error updating comment!')

    return HttpResponseRedirect(reverse('post_detail', args=[slug]))

def comment_delete(request, slug, comment_id):
    """
    view to delete comment
    """
    queryset = Post.objects.filter(status=1)
    post = get_object_or_404(queryset, slug=slug)
    comment = get_object_or_404(Comment, pk=comment_id)

    if comment.author == request.user:
        comment.delete()
        messages.add_message(request, messages.SUCCESS, 'Comment deleted!')
    else:
        messages.add_message(request, messages.ERROR, 'You can only delete your own comments!')

    return HttpResponseRedirect(reverse('post_detail', args=[slug]))

"""
class AddNewPost(CreateView):
    
    View to add a new blog post.
    
    model = Post
    form_class = PostForm
    template_name = 'add_post.html'
    success_url = reverse_lazy('blog')

    def form_valid(self, form):
        
        Set the author of the post to the current user before saving.
        
        form.instance.author = self.request.user
        return super().form_valid(form)"""

def add_post(request):
    if request.method == 'POST':
        #a post was added
        post_form = PostForm(data=request.POST)
        if post_form.is_valid():
            #create a post object but don't save to database yet
            new_post = post_form.save(commit=False)
            #assign the current slug and user to the post
            new_post.author = request.user
            new_post.slug = slugify(new_post.title)
            #save post to database
            new_post.save()
            return HttpResponsePermanentRedirect(reverse('blog'))
    else:
        post_form = PostForm()
        return render(request, 'add_post.html', {'post_form': post_form})
