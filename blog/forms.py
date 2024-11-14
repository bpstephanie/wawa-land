from .models import Post, Comment
from django import forms

class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ('body',)

class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ('title', 'post_content', 'featured_image')
        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control'}),
            'post_content': forms.Textarea(
                attrs={
                    'class': 'form-control',
                    'placeholder': 'Enter post text here...'
                }
            ),
            'featured_image': forms.ClearableFileInput(attrs={'class': 'form-control'}),
            }