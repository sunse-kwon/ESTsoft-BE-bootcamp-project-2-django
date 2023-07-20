from django import forms
from .models import Post, Comment, Hashtag, Reply


class Postform(forms.ModelForm):

    class Meta:
        model = Post
        fields = ['title', 'content']


class CommentForm(forms.ModelForm):

    class Meta:
        model = Comment
        fields = ['content']
        widgets = {
            'content':  forms.Textarea(attrs={'rows': '3', 'cols': '40'})
        }


class HashtagForm(forms.ModelForm):

    class Meta:
        model = Hashtag
        fields = ['name']


class ReplyForm(forms.ModelForm):

    class Meta:
        model = Reply
        fields = ['content']
        widgets = {
            'content':  forms.Textarea(attrs={'rows': '3', 'cols': '40'})
        }
