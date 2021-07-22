from django.shortcuts import render, get_object_or_404
from django.db.models import Q
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.contrib.auth.models import User
from django.views.generic import (
    ListView,
    DetailView,
    CreateView,
    UpdateView,
    DeleteView
)
from .models import Candidate

def home(request):
    context = {
        'candidates': Candidate.objects.all()
    }
    return render(request, 'candidates/home.html', context)

class CandidateListView(ListView):
    model = Candidate
    template_name = 'candidates/home.html'  # <app>/<model>_<viewtype>.html
    context_object_name = 'candidates'
    ordering = ['id']
    paginate_by = 6

class CandidateListViewOverview(ListView):
    model = Candidate
    template_name = 'candidates/home_overview.html'  # <app>/<model>_<viewtype>.html
    context_object_name = 'candidates'
    ordering = ['id']
    paginate_by = 6



class ClientListView(ListView):
    model = Candidate
    template_name = 'candidates/client_candidates.html'  # <app>/<model>_<viewtype>.html
    context_object_name = 'candidates'
    paginate_by = 6

    def get_queryset(self):
        user = get_object_or_404(User, username=self.kwargs.get('username'))
        return Candidate.objects.filter(client=user).order_by('candidatefamilyname')


class CandidateDetailView(DetailView):
    model = Candidate


class CandidateCreateView(LoginRequiredMixin, CreateView):
    model = Candidate
    fields = ['candidatesalutation', 'candidatefirstname', 'candidatemiddlenames', 'candidatefamilyname', 'candidateemail']
    labels = {
        'candidatesalutation' : 'Salutation',
        'candidatefirstname' : 'First name',
        'candidatemiddlenames' : 'Middle name',
        'candidatefamilyname' : 'Family name',
        'candidateemail' : 'Email'
        }

    def form_valid(self, form):
        form.instance.client = self.request.user
        return super().form_valid(form)


class CandidateUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Candidate
    fields = ['title', 'content']

    def form_valid(self, form):
        form.instance.client = self.request.user
        return super().form_valid(form)

    def test_func(self):
        post = self.get_object()
        if self.request.user == candidate.client:
            return True
        return False


class CandidateDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Candidate
    success_url = '/'

    def test_func(self):
        Candidate = self.get_object()
        if self.request.user == candidate.client:
            return True
        return False


def about(request):
	return render(request, 'candidates/about.html', {'title': 'About'})

def search(request):
    return render(request, 'candidates/search.html')

class SearchResultsView(ListView):
    model = Candidate
    template_name = 'candidates/search_results.html'
    context_object_name = 'candidates'
    
    def get_queryset(self): # new
        queryparam1 = self.request.GET.get('p')
        queryparam2 = self.request.GET.get('userid')

        if self.request.user.is_superuser:
            return  Candidate.objects.filter(Q(candidatefamilyname=queryparam1))
        else:
            return  Candidate.objects.filter(Q(client_id=queryparam2) & Q(candidatefamilyname=queryparam1))
  
        #This works in python shell
        #>>>user.id
        #17
        #>>>Candidates.objects.filter(Q(client_id=user.id) & Q(candidatefamilyname='Green'))
        #<Queryset [<Candidate: May Green>, <Candidate: Diedre Green]

        #>>>Candidates.objects.filter(Q(client_id=user.id) & Q(candidatefamilyname='Black'))
        #Queryset []>
