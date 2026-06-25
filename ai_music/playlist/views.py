from django.shortcuts import render, redirect
from django.core.mail import send_mail
from django.conf import settings
from .models import Profile, Song


def login(request):
    if request.method == "POST":
        email = request.POST.get('user')
        password = request.POST.get('password')

        user = Profile.objects.filter(
            user=email,
            password=password
        ).first()

        if user:
            return redirect('index')
        else:
            return render(request, 'login.html', {
                'error': 'Invalid Email or Password'
            })

    return render(request, 'login.html')


def user(request):
    if request.method == 'POST':
        email = request.POST.get('user')
        password = request.POST.get('password')
        password2 = request.POST.get('password2')

        if password == password2:

            if Profile.objects.filter(user=email).exists():
                return render(request, 'signup.html', {
                    'error': 'Email already exists'
                })

            Profile.objects.create(
                user=email,
                password=password
            )

            send_mail(
                "Thanks",
                "Dear User,\nYour account has been successfully created. Now you can enjoy unlimited music.",
                settings.EMAIL_HOST_USER,
                [email]
            )

            return redirect('login')

        return render(request, 'signup.html', {
            'error': 'Passwords do not match'
        })

    return render(request, 'signup.html')


def index(request):
    search = request.GET.get('search')

    if search:
        akash = Song.objects.filter(
            title__icontains=search
        )
    else:
        akash = Song.objects.all()

    return render(request, 'song.html', {
        'akash': akash
    })


def song_detail(request, id):
    song = Song.objects.get(id=id)

    return render(request, 'song_detail.html', {
        'song': song
    })