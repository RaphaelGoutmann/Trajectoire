from django import forms
from articles.models import Comment

class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ("author", "content")
        widgets = {
            'author': forms.TextInput(attrs={'placeholder': 'Auteur...'}),
            'content': forms.Textarea(attrs={'placeholder': 'Commentaire...'}) }