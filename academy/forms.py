from django import forms
from .models import *

class ProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ['profile_picture', 'bio']
        widgets = {
            'profile_picture': forms.TextInput(attrs={'placeholder': 'Enter the URL here', 'size':40}),
            'bio': forms.Textarea(attrs={'placeholder': 'Enter you bio here...', 'rows': 3, 'cols': 40})
        }
        labels ={
            'profile_picture': 'Profile picture URL',
            'bio': 'Bio Description',
        }

class ReviewForm(forms.ModelForm):
    RATING_CHOICES = [
        (1, '1 Star'),
        (2, '2 Stars'),
        (3, '3 Stars'),
        (4, '4 Stars'),
        (5, '5 Stars'),
    ]

    rating = forms.ChoiceField(label='Rating', choices=RATING_CHOICES, widget=forms.RadioSelect)
    comment = forms.CharField(label='Comment', widget=forms.Textarea(attrs={'rows': 4}))

    class Meta:
        model = Review
        fields = ['rating', 'comment']


class ForumTopicForm(forms.ModelForm):
    class Meta:
        model = ForumTopic
        fields = ['title', 'description']
        widgets = {
            'title': forms.TextInput(attrs={'placeholder': 'Title', 'size':70}),
            'description': forms.Textarea(attrs={'placeholder': 'Description', 'rows': 4, 'cols': 70}),
        }
        # Removing the labels, not aesthetic 
        labels = {
            'title': '',
            'description': '',
        }

class ForumPostForm(forms.ModelForm):
    class Meta:
        model = ForumPost
        fields = ['content']
        widgets = {
            'content': forms.Textarea(attrs={'placeholder':'Write your reply here...', 'cols': 95, 'rows':3}),  
        }
        labels = {
            'content': ''
        }

class QuizAttemptForm(forms.Form):
    def __init__(self, *args, **kwargs):
        question = kwargs.pop('question')
        super().__init__(*args, **kwargs)
        options = Option.objects.filter(question=question)
        choices = [(option.id, option.text) for option in options]
        self.fields['options'] = forms.ChoiceField(widget=forms.RadioSelect, choices=choices)

