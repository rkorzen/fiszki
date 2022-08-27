from django.shortcuts import render
from .models import Card

# widok funkcyjny
def card_list(request):
    cards = Card.objects.all()
    return render(
        request,
        "cards/card_list.html",
        {"card_list": cards}
    )
