from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.http import JsonResponse
from app.models import Film
from .models import Profile  # Profile modelini import qilishni unutmang

@login_required
def my_profile(request):
    films = Film.objects.filter(created_by=request.user)
    return render(request, "profile.html", {
        "films": films
    })

@login_required
def change_avatar(request):
    if request.method == 'POST' and request.FILES.get('avatar'):
        avatar_file = request.FILES['avatar']

        # Agar userda Profile bo‘lmasa, yaratadi
        profile, created = Profile.objects.get_or_create(user=request.user)
        profile.avatar = avatar_file
        profile.save()

        return JsonResponse({
            'success': True,
            'avatar_url': profile.avatar.url
        })

    return JsonResponse({'success': False}, status=400)
