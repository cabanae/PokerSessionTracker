from django.shortcuts import render
from django.contrib.auth.mixins import PermissionRequiredMixin
from django.urls import reverse
from django.contrib.auth.decorators import permission_required
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from django.views import generic
from django.contrib.auth import login, authenticate
from django.contrib.auth.forms import UserCreationForm
from django.shortcuts import render, redirect
from .models import Session, Place, Game


def index(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=raw_password)
            login(request, user)
            return redirect('index')
    else:
        form = UserCreationForm()
    return render(request, 'signup.html', {'form': form})

class SessionListView(generic.ListView):
    """
    Generic class-based view for a list of Sessions.
    """
    model = Session
    paginate_by = 10000
    def get_queryset(self):
        #if request.user.is_authenticated():
        return Session.objects.filter(session_user=self.request.user)
        #else:
         #   return render_to_response('login.html')

class SessionDetailView(generic.DetailView):
    """
    Generic class-based detail view for a Session.
    """
    model = Session

class GameDetailView(generic.DetailView):
    """
    Generic class-based detail view for a game.
    """
    model = Game

class PlaceDetailView(generic.DetailView):
    """
    Generic class-based detail view for a place.
    """
    model = Place

class SessionCreate(PermissionRequiredMixin, CreateView):
    model = Session
    #save current user to Session model
    def form_valid(self, form):
        form.instance.session_user = self.request.user
        return super(SessionCreate, self).form_valid(form)
    #exclude = ['session_user']
    #fields = '__all__'
    initial = {'time_start': '2018-04-04 06:31:00', 'time_end': '2018-04-04 07:31:00',}
    fields = (
        'time_start',
        'time_end',
        'Notes',
        'game_type',
        'amount',
        'place',
    )

    permission_required = 'tracker.can_mark_returned'

class SessionUpdate(PermissionRequiredMixin, UpdateView):
    model = Session
    fields = '__all__'
    permission_required = 'tracker.can_mark_returned'


class SessionDelete(PermissionRequiredMixin, DeleteView):
    model = Session
    success_url = reverse_lazy('sessions')
    permission_required = 'tracker.can_mark_returned'

class PlaceCreate(PermissionRequiredMixin, CreateView):
    model = Place
    #save current user to Session model
    def form_valid(self, form):
        form.instance.session_user = self.request.user
        return super(PlaceCreate, self).form_valid(form)
    #exclude = ['session_user']
    #fields = '__all__'

    fields = (
        'name',
    )

    permission_required = 'tracker.can_mark_returned'

class GameCreate(PermissionRequiredMixin, CreateView):
    model = Game
    #save current user to Session model
    def form_valid(self, form):
        form.instance.session_user = self.request.user
        return super(GameCreate, self).form_valid(form)
    #exclude = ['session_user']
    #fields = '__all__'

    fields = (
        'game_type',
    )

    permission_required = 'tracker.can_mark_returned'

def signup(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=raw_password)
            login(request, user)
            return redirect('home')
    else:
        form = UserCreationForm()
    return render(request, 'signup.html', {'form': form})

def edit_session(request):
    if request.method == 'POST':
        form = EditSessionForm(request.POST, instance=request.user)

        if form.is_valid():
            form.save()
            return redirect(reverse('tracker:view_profile'))
    else:
        form = EditSessionForm(instance=request.user)
        args = {'form': form}
        return render(request, 'tracker/edit_session.html', args)