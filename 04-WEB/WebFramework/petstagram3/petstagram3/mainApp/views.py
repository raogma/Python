from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render, redirect
from django.views.generic import TemplateView, ListView
from petstagram3.mainApp.models import PetPhoto


class HomeView(TemplateView):
    template_name = 'home_page.html'

    def dispatch(self, *args, **kwargs):
        res = super().dispatch(*args, **kwargs)
        if self.request.user.is_authenticated:
            return redirect('dashPath')
        return res

    def get_context_data(self, **kwargs):
        ctx = super().get_context_data(**kwargs)
        ctx['hide_bonus_btns'] = True
        return ctx


# def home_page(req):
#     ctx = {
#         'hide_bonus_btns': True,
#     }
#     return render(req, 'home_page.html', ctx)

class DashView(ListView):
    template_name = 'dashboard.html'
    model = PetPhoto

    def dispatch(self, request, *args, **kwargs):
        res = super().dispatch(request, *args, **kwargs)
        if not self.request.user.is_authenticated:
            return redirect('login')

        return res

# def dash_page(req):
#     pet_photos = PetPhoto.objects.prefetch_related('tagged_pets').all()
#     ctx = {
#         'pet_photos': pet_photos,
#     }
#     return render(req, 'dashboard.html', ctx)
