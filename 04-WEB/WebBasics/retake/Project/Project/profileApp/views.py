from django.urls import reverse_lazy
from django.views.generic import TemplateView, CreateView, UpdateView, DeleteView, DetailView

from Project.gameApp.models import Game
from Project.profileApp.forms import CreateProfileForm, EidtProfileForm, DeleteProfileForm
from Project.profileApp.models import Profile


class ProfileDetailsPage(DetailView):
    template_name = 'profile/details-profile.html'
    model = Profile

    def get_context_data(self, **kwargs):
        ctx = super().get_context_data(**kwargs)
        ctx['profile'] = Profile.objects.first()
        games = Game.objects.all()
        total_games = len(games)
        ctx['total_games'] = total_games
        average_rating = '0.0'
        if total_games != 0:
            average_rating = sum([x.rating for x in games]) / total_games
        ctx['average_rating'] = average_rating
        return ctx


class ProfileCreatePage(CreateView):
    template_name = 'profile/create-profile.html'
    form_class = CreateProfileForm
    success_url = reverse_lazy('home')

    def get_context_data(self, **kwargs):
        ctx = super().get_context_data(**kwargs)
        ctx['profile'] = Profile.objects.first()
        return ctx


class ProfileEditPage(UpdateView):
    template_name = 'profile/edit-profile.html'
    model = Profile
    form_class = EidtProfileForm

    def get_success_url(self):
        return reverse_lazy('profile-details', kwargs={'pk': self.object.pk})

    def get_context_data(self, **kwargs):
        ctx = super().get_context_data(**kwargs)
        ctx['profile'] = Profile.objects.first()
        return ctx


class ProfileDeletePage(DeleteView):
    template_name = 'profile/delete-profile.html'
    model = Profile
    form_class = DeleteProfileForm
    success_url = reverse_lazy('home')

    def form_valid(self, form):
        form = super().form_valid(form)
        [x.delete() for x in Game.objects.all()]
        return form

    def get_context_data(self, **kwargs):
        ctx = super().get_context_data(**kwargs)
        ctx['profile'] = Profile.objects.first()
        return ctx
