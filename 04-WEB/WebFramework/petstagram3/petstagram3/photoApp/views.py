from django.urls import reverse_lazy
from django.views.generic import CreateView, UpdateView, DetailView

from petstagram3.mainApp.models import PetPhoto
from petstagram3.photoApp.forms import CreatePhotoForm, EditPhotoForm


class CreatePhoto(CreateView):
    template_name = 'photo_create.html'
    form_class = CreatePhotoForm

    def get_success_url(self):
        return reverse_lazy('dashPath')


class EditPhoto(UpdateView):
    template_name = 'photo_edit.html'
    form_class = EditPhotoForm
    queryset = PetPhoto.objects.prefetch_related('tagged_pets').all()
    model = PetPhoto

    #
    # def get_context_data(self, **kwargs):
    #     ctx = super().get_context_data(**kwargs)
    #     ctx[]
    #     return ctx
    #

    def get_success_url(self):
        return reverse_lazy('dashPath')

    # def get_queryset(self):
    #     # return EditPhotoForm.model.objects.prefetch_related('tagged_pets').all()
    #     return super().get_queryset().prefetch_related('tagged_pets')


class PhotoDetails(DetailView):
    template_name = 'photo_details.html'
    model = PetPhoto

    def get_context_data(self, **kwargs):
        ctx = super().get_context_data(**kwargs)
        print(self.request.user == self.object.owner)
        ctx['is_owner'] = self.request.user.pk == self.object.owner_id
        return ctx
