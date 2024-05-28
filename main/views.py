from django.shortcuts import render, redirect
from django.conf import settings
from django.contrib.auth import login, authenticate
from django.contrib.auth.forms import AuthenticationForm
from .forms import SignUpForm

def home(request):
    return render(request, 'home.html')

def explore(request):
    context = {
        'google_maps_api_key': settings.GOOGLE_MAPS_API_KEY
    }
    return render(request, 'explore.html', context)

def upgrade(request):
    return render(request, 'upgrade.html')

def login_view(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect('home')
    else:
        form = AuthenticationForm()
    return render(request, 'login.html', {'form': form})

def signup(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=password)
            login(request, user)
            return redirect('home')
    else:
        form = SignUpForm()
    return render(request, 'signup.html', {'form': form})

def route_detail(request, route_id):
    route = {
        'id': route_id,
        'name': f'Route {route_id}',
        'description': f'Details of Route {route_id}.',
        'image_url': f'images/route{route_id}.jpg'
    }
    return render(request, 'route_detail.html', {'route': route})

def plan_trail(request):
    if not request.user.is_authenticated:
        return redirect('login')
    return render(request, 'plan_trail.html')


def home(request):
    return render(request, 'home.html')

def explore(request):
    context = {
        'google_maps_api_key': settings.GOOGLE_MAPS_API_KEY
    }
    return render(request, 'explore.html', context)

def upgrade(request):
    return render(request, 'upgrade.html')

def login_view(request):
    return render(request, 'login.html')

def signup(request):
    return render(request, 'signup.html')

def route_detail(request, route_id):
    # route_id'ye göre detayları getir
    route = {
        'id': route_id,
        'name': f'Route {route_id}',
        'description': f'Details of Route {route_id}.',
        'image_url': f'static/images/route{route_id}.jpg'
    }
    return render(request, 'route_detail.html', {'route': route})

def plan_trail(request):
    if not request.user.is_authenticated:
        return redirect('login')
    return render(request, 'plan_trail.html')

from django.shortcuts import render, redirect
from django.conf import settings
from django.contrib.auth import login, authenticate
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.models import User
from .forms import SignUpForm

def home(request):
    return render(request, 'home.html')

def explore(request):
    context = {
        'google_maps_api_key': settings.GOOGLE_MAPS_API_KEY
    }
    return render(request, 'explore.html', context)

def upgrade(request):
    return render(request, 'upgrade.html')

def login_view(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect('home')
    else:
        form = AuthenticationForm()
    return render(request, 'login.html', {'form': form})

def signup(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('home')
    else:
        form = SignUpForm()
    return render(request, 'signup.html', {'form': form})

def route_detail(request, route_id):
    route = {
        'id': route_id,
        'name': f'Route {route_id}',
        'description': f'Details of Route {route_id}.',
        'image_url': f'images/route{route_id}.jpg'
    }
    return render(request, 'route_detail.html', {'route': route})

def plan_trail(request):
    if not request.user.is_authenticated:
        return redirect('login')
    return render(request, 'plan_trail.html')

from django.shortcuts import render, redirect
from django.conf import settings
from django.contrib.auth import login, authenticate
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.decorators import login_required
from .forms import SignUpForm, TrailForm
from .models import Trail

def home(request):
    return render(request, 'home.html')

def explore(request):
    context = {
        'google_maps_api_key': settings.GOOGLE_MAPS_API_KEY
    }
    return render(request, 'explore.html', context)

def upgrade(request):
    return render(request, 'upgrade.html')

def login_view(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect('home')
    else:
        form = AuthenticationForm()
    return render(request, 'login.html', {'form': form})

def signup(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('home')
    else:
        form = SignUpForm()
    return render(request, 'signup.html', {'form': form})

def route_detail(request, route_id):
    route = {
        'id': route_id,
        'name': f'Route {route_id}',
        'description': f'Details of Route {route_id}.',
        'image_url': f'images/route{route_id}.jpg'
    }
    return render(request, 'route_detail.html', {'route': route})

@login_required
def plan_trail(request):
    return render(request, 'plan_trail.html')

@login_required
def upload_trail(request):
    if request.method == 'POST':
        form = TrailForm(request.POST)
        if form.is_valid():
            trail = form.save(commit=False)
            trail.user = request.user
            trail.data = request.POST.get('trail_data')  # JSON data from client
            trail.length = request.POST.get('trail_length')
            trail.save()
            return redirect('your_trails')
    else:
        form = TrailForm()
    return render(request, 'upload_trail.html', {'form': form})

@login_required
def your_trails(request):
    trails = Trail.objects.filter(user=request.user)
    return render(request, 'your_trails.html', {'trails': trails})

def download(request):
    return render(request, 'download.html')

from django.shortcuts import render, redirect
from django.conf import settings
from django.contrib.auth import login, authenticate
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.decorators import login_required
from .forms import SignUpForm, TrailForm
from .models import Trail

def home(request):
    return render(request, 'home.html')

def explore(request):
    context = {
        'google_maps_api_key': settings.GOOGLE_MAPS_API_KEY
    }
    return render(request, 'explore.html', context)

def upgrade(request):
    return render(request, 'upgrade.html')

def login_view(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect('home')
    else:
        form = AuthenticationForm()
    return render(request, 'login.html', {'form': form})

def signup(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('home')
    else:
        form = SignUpForm()
    return render(request, 'signup.html', {'form': form})

@login_required
def plan_trail(request):
    return render(request, 'plan_trail.html')

def download(request):
    return render(request, 'download.html')

def about(request):
    return render(request, 'about.html')

def donors(request):
    return render(request, 'donors.html')

def team(request):
    return render(request, 'team.html')


