from django.db.models.base import Model

from django.forms import ModelForm
from .models import Tutorial, Review



class TutorialForm(ModelForm):

    class Meta:
        model = Tutorial
        fields = ['name', 'description', 'image', 'specialty', 'tags', 'price']

    def __init__(self, *args, **kwargs):
        super(TutorialForm, self).__init__(*args, **kwargs)

        self.fields['name'].widget.attrs['class'] = 'form-control'
        self.fields['description'].widget.attrs['class'] = 'form-control'
        self.fields['image'].widget.attrs['class'] = 'form-control'
        self.fields['specialty'].widget.attrs['class'] = 'form-control'
        self.fields['tags'].widget.attrs['class'] = 'form-control'
        self.fields['price'].widget.attrs['class'] = 'form-control'




class ReviewForm(ModelForm):
    class Meta:
        model = Review
        fields = ['name', 'body', 'like']
        labels = {
            'name': 'Name',
            'body': 'Comment',
            'like': 'vote'
        }

    def __init__(self, *args, **kwargs):
        super(ReviewForm, self).__init__(*args, **kwargs)

        self.fields['name'].widget.attrs['class'] = 'form-control'
        self.fields['body'].widget.attrs['class'] = 'form-control'
        self.fields['like'].widget.attrs['class'] = 'form-control'

    