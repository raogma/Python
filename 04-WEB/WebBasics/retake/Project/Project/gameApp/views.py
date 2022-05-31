from django.urls import reverse_lazy
from django.views.generic import CreateView, UpdateView, DeleteView, DetailView

from Project.gameApp.forms import GameForm, DeleteGameForm
from Project.gameApp.models import Game
from Project.profileApp.models import Profile


class GameDetailsPage(DetailView):
    template_name = 'game/details-game.html'
    model = Game

    def get_context_data(self, **kwargs):
        ctx = super().get_context_data(**kwargs)
        ctx['profile'] = Profile.objects.first()
        return ctx


class GameCreatePage(CreateView):
    template_name = 'game/create-game.html'
    form_class = GameForm
    success_url = reverse_lazy('dashboard')

    def get_context_data(self, **kwargs):
        ctx = super().get_context_data(**kwargs)
        ctx['profile'] = Profile.objects.first()
        return ctx


class GameEditPage(UpdateView):
    template_name = 'game/edit-game.html'
    form_class = GameForm
    model = Game
    success_url = reverse_lazy('dashboard')

    def get_context_data(self, **kwargs):
        ctx = super().get_context_data(**kwargs)
        ctx['profile'] = Profile.objects.first()
        return ctx


class GameDeletePage(DeleteView):
    template_name = 'game/delete-game.html'
    form_class = DeleteGameForm
    model = Game
    success_url = reverse_lazy('dashboard')

    def get_context_data(self, **kwargs):
        ctx = super().get_context_data(**kwargs)
        ctx['profile'] = Profile.objects.first()
        return ctx

    def get_initial(self):
        return {
            'title': "'" + self.object.title + "'",
            'category': self.object.category,
            'rating': self.object.rating,
            'max_level': self.object.max_level,
            'image_URL': self.object.image_URL,
            'summary': self.object.summary,
        }
