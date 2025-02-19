from django.urls import reverse_lazy

from django.views.generic import CreateView, DeleteView,DetailView, ListView, UpdateView

from jokes.forms import JokeForm

from .models import Joke

class JokeCreateView(CreateView):
    model = Joke
    # fields = ['question', 'answer']
    form_class = JokeForm

class JokeDetailView(DetailView):
    model = Joke

class JokeDeleteView(DeleteView):
    model = Joke
    success_url = reverse_lazy('jokes:list')

class JokeListView(ListView):
    model = Joke

class JokeUpdateView(UpdateView):
    model = Joke
    # fields = ['question', 'answer']
    form_class = JokeForm

# Create your views here.
