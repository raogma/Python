from django.contrib.auth import logout, login
from django.contrib.auth.views import LoginView
from django.urls import reverse_lazy
from django.views.generic import CreateView, UpdateView, DetailView, DeleteView

from petstagram3.accountsApp.forms import EditProfileForm, DeleteProfileForm, CreateProfileForm
from petstagram3.accountsApp.models import AppUser
from petstagram3.mainApp.models import PetPhoto


class CreateProfileView(CreateView):
    form_class = CreateProfileForm
    template_name = 'profile_create.html'

    def get_success_url(self):
        return reverse_lazy('dashPath')

    def form_valid(self, form):
        form = super().form_valid(form)
        login(self.request, self.object)
        return form


class EditProfileView(UpdateView):
    template_name = 'profile_edit.html'
    form_class = EditProfileForm
    queryset = AppUser.objects.select_related('profile')

    def get_success_url(self):
        return reverse_lazy('dashPath')


class DeleteProfileView(DeleteView):
    template_name = 'profile_delete.html'
    form_class = DeleteProfileForm
    queryset = AppUser.objects.select_related('profile')


    # def form_valid(self, form):
    #     success_url = self.get_success_url()
    #     self.object.
    #     self.object.delete()
    #     return HttpResponseRedirect(success_url)


    def get_success_url(self):
        logout(self.request, )
        return reverse_lazy('dashPath')


class ProfileDetailsView(DetailView):
    template_name = 'profile_details.html'
    model = AppUser

    def get_context_data(self, **kwargs):
        ctx = super().get_context_data(**kwargs)
        images = PetPhoto.objects.filter(owner=self.object.pk)
        ctx['images_count'] = len(images)
        ctx['likes_count'] = sum([x.likes for x in images])

        return ctx


class UserLogin(LoginView):
    template_name = 'login_page.html'

    def get_success_url(self):
        return reverse_lazy('dashPath')

