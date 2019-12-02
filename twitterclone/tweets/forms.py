from django import forms
from .models import Tweet


class Add_Tweet(forms.ModelForm):
    class Meta:
        model = Tweet
        fields = [
            'twitter_user',
            'posts',
            'time_date'
        ]
