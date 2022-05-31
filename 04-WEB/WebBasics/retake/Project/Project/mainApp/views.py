from django.views.generic import TemplateView, ListView

from Project.gameApp.models import Game
from Project.profileApp.models import Profile


class HomePage(TemplateView):
    template_name = 'home-page.html'

    def get_context_data(self, **kwargs):
        ctx = super().get_context_data(**kwargs)
        ctx['profile'] = Profile.objects.first()
        return ctx


class DashPage(ListView):
    template_name = 'dashboard.html'
    model = Game

    def get_context_data(self, **kwargs):
        ctx = super().get_context_data(**kwargs)
        ctx['profile'] = Profile.objects.first()
        return ctx