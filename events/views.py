from django.shortcuts import render, redirect
from .models import EventCard
from .forms import EventCardForm
from django.contrib.auth import login
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required
from django.shortcuts import get_object_or_404
from django.http import JsonResponse
from django.template.loader import render_to_string

def search_cards(request):
    tag = request.GET.get('tag')
    type_filter = request.GET.get('type')
    search_query = request.GET.get('search')

    cards = EventCard.objects.all()

    if tag:
        cards = cards.filter(tag=tag)
    if type_filter:
        cards = cards.filter(type=type_filter)
    if search_query:
        cards = cards.filter(title__icontains=search_query)

    html = render_to_string('partials/card_grid.html', {'cards': cards})
    return JsonResponse({'html': html})

def event_detail(request, pk):
    card = get_object_or_404(EventCard, pk=pk)
    return render(request, 'events/event_detail.html', {'card': card})

def signup_view(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)  
            return redirect('event_list')
    else:
        form = UserCreationForm()
    return render(request, 'registration/signup.html', {'form': form})

def event_list(request):
    tag = request.GET.get('tag')
    type_filter = request.GET.get('type')
    search_query = request.GET.get('search')

    cards = EventCard.objects.all()

    if tag:
        cards = cards.filter(tag=tag)
    if type_filter:
        cards = cards.filter(type=type_filter)
    if search_query:
        cards = cards.filter(title__icontains=search_query)

    cards = cards.order_by('created_at')

    context = {
        'cards': cards,
        'selected_tag': tag,
        'selected_type': type_filter,
        'search_query': search_query,
    }
    return render(request, 'events/event_list.html', context)

@login_required(login_url='/accounts/login/')
def create_card(request):
    if request.method == "POST":
        form = EventCardForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('event_list')
    else:
        form = EventCardForm()
    return render(request, 'events/create_card.html', {'form': form})
