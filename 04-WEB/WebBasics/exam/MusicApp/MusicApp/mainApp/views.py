from django.shortcuts import render, redirect

from MusicApp.UTILS import get_first_profile, get_all_albums


def home_view(req):
    profile = get_first_profile()
    ctx = {
        'albums': get_all_albums(),
        'profile': profile,
    }
    if profile:
        return render(req, 'home-with-profile.html', ctx)
    return redirect('show create profile')
