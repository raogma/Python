from django.shortcuts import render

from MusicApp.UTILS import crud, get_first_profile
from MusicApp.albumApp.forms import AlbumForm, DeleteAlbumForm
from MusicApp.mainApp.models import Album


def album_details_view(req, pk):
    ctx = {
        'album': Album.objects.get(pk=pk),
        'profile': get_first_profile(),
    }
    return render(req, 'album-details.html', ctx)


def album_add_view(req):
    return crud(req, AlbumForm, None, 'show home', 'add-album.html')


def album_edit_view(req, pk):
    return crud(req, AlbumForm, Album.objects.get(pk=pk), 'show home', 'edit-album.html')


def album_delete_view(req, pk):
    return crud(req, DeleteAlbumForm, Album.objects.get(pk=pk), 'show home', 'delete-album.html')
