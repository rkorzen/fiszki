from django.shortcuts import render
from django.urls import reverse_lazy

from .forms import CardForm
from .models import Card
from django.views.generic import ListView, CreateView, UpdateView

# widok funkcyjny
def card_list(request):
    cards = Card.objects.all().order_by("box", "-date_created")  # all jest tu zbędne
    return render(request, "cards/card_list.html", {"card_list": cards})


# wido klasowy - analog dla powyższego:
class CardListView(ListView):
    model = Card
    ordering = ("box", "-date_created")  # ordering przy pomocy atrybuty
    # queryset = Card.objects.order_by("box", "-date_created")   # modyfikacja queryset


# widok funkcyjny


def card_create(request):
    if request.method == "POST":
        form = CardForm(request.POST)
        if form.is_valid():
            form.save()
    form = CardForm()
    return render(request, "cards/card_form.html", {"form": form})


class CardCreateView(CreateView):
    model = Card
    fields = ["question", "answer", "box"]
    success_url = reverse_lazy("card-create")


# update

# widok funkcyjny


def update_view(request, pk):
    card = Card.objects.get(pk=pk)
    form = CardForm(instance=card)
    if request.method == "POST":
        form = CardForm(data=request.POST, instance=card)
        if form.is_valid():
            form.save()
    return render(request, "cards/card_form.html", {"form": form})


class CardUpdateView(UpdateView):
    pass
