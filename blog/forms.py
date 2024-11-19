from django import forms
from django_summernote.widgets import SummernoteWidget
from .models import Post, Comment


class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ('body',)


class LikeForm(forms.Form):
    pass


class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ('title', 'post_content', 'featured_image')
        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control'}),
            'post_content': SummernoteWidget(
                attrs={
                    'class': 'form-control',
                    'placeholder': 'Enter post text here...'
                }
            ),
            'featured_image': forms.ClearableFileInput(
                attrs={'class': 'form-control'}),
            }
