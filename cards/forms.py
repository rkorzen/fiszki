from django import forms

from .models import Card


class CardForm(forms.ModelForm):
    class Meta:
        model = Card
        fields = ["question", "answer", "box"]


class CardCheckForm(forms.Form):
    card_id = forms.IntegerField(required=True)
    solved = forms.BooleanField(required=False)
