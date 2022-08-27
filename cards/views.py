from django.shortcuts import render
from .models import Card
from django.views.generic import (
    ListView,
)

# widok funkcyjny
def card_list(request):
    cards = Card.objects.all().order_by("box", "-date_created")  # all jest tu zbędne
    return render(request, "cards/card_list.html", {"card_list": cards})


# wido klasowy - analog dla powyższego:
class CardListView(ListView):
    model = Card
    ordering = ("box", "-date_created")  # ordering przy pomocy atrybuty
    # queryset = Card.objects.order_by("box", "-date_created")   # modyfikacja queryset
