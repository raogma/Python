from django import forms
from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.views.generic import CreateView, UpdateView, DeleteView, TemplateView, DetailView

from petstagram3.mainApp.models import PetPhoto, Pet
from petstagram3.petApp.forms import CreatePetForm, EditPetForm, DeletePetForm


def like_fn(req, id):
    photo = PetPhoto.objects.get(pk=id)
    photo.likes += 1
    photo.save()
    return redirect('petDetailsPath', id)


class CreatePet(CreateView):
    template_name = 'pet_create.html'
    form_class = CreatePetForm

    def form_valid(self, form):
        res = super().form_valid(form)
        obj = form.save(commit=False)
        obj.owner_id = self.request.user.pk
        obj.save()
        return res

    def get_success_url(self):
        return reverse_lazy('dashPath')


class EditPet(UpdateView):
    template_name = 'pet_edit.html'
    form_class = EditPetForm

    def get_queryset(self):
        return super().get_queryset().select_related('owner')

    def get_success_url(self):
        return reverse_lazy('dashPath')


class DeletePet(DeleteView):
    template_name = 'pet_delete.html'
    form_class = DeletePetForm
    model = Pet

    def get_success_url(self):
        return reverse_lazy('dashPath')
