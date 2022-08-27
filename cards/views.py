from django.shortcuts import render
from .models import Card
from django.views.generic import (
    ListView,
)

# widok funkcyjny
def card_list(request):
    cards = Card.objects.all()
    return render(request, "cards/card_list.html", {"card_list": cards})


# wido klasowy - analog dla powyższego:
class CardListView(ListView):
    model = Card
