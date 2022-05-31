from django.shortcuts import render

from MusicApp.UTILS import get_first_profile, get_all_albums, crud
from MusicApp.profileApp.forms import CreateProfileForm, DeleteProfileForm

profile = get_first_profile()


def profile_details_view(req):
    albums = get_all_albums()
    ctx = {
        'profile': profile,
        'albums_count': len(albums),
    }
    return render(req, 'profile-details.html', ctx)


def profile_create_view(req):
    return crud(req, CreateProfileForm, None, 'show home', 'home-no-profile.html')


# def profile_edit_view(req):
#     return render(req, )


def profile_delete_view(req):
    return crud(req, DeleteProfileForm, profile, 'show home', 'profile-delete.html')
