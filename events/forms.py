from django import forms
from .models import EventCard

class EventCardForm(forms.ModelForm):
    class Meta:
        model = EventCard
        fields = ['title', 'description', 'image', 'tag', 'created_at', 'type', 'hosted_by']
        widgets = {
            'tag': forms.Select(attrs={'class': 'form-control'}),
            'created_at': forms.DateTimeInput(attrs={'type': 'datetime-local'}),
        }
