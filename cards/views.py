from django.shortcuts import render, redirect
from django.urls import reverse_lazy

from .forms import CardForm
from .models import Card
from django.views.generic import ListView, CreateView, UpdateView
from django.contrib.messages.views import SuccessMessageMixin


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


class CardCreateView(SuccessMessageMixin, CreateView):
    model = Card
    fields = ["question", "answer", "box"]
    success_url = reverse_lazy("card-create")
    success_message = "Karta utworzona!"


# update

# widok funkcyjny


def update_view(request, pk):
    card = Card.objects.get(pk=pk)
    form = CardForm(instance=card)
    if request.method == "POST":
        form = CardForm(data=request.POST, instance=card)
        if form.is_valid():
            form.save()
        return redirect(reverse_lazy("card-list"))
    return render(request, "cards/card_form.html", {"form": form})


class CardUpdateView(CardCreateView, UpdateView):
    success_url = reverse_lazy("card-list")
    success_message = "Karta zaktualizowana!"


class BoxView(CardListView):
    template_name = "cards/box.html"

    def get_queryset(self):
        return Card.objects.filter(box=self.kwargs["box_num"])

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["box_number"] = self.kwargs["box_num"]
        return context
