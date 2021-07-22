from django.conf import settings
from django.conf.urls import include, url

from django.urls import path
from django.contrib import admin
from .views import (
	CandidateListView,
	CandidateDetailView,
	CandidateCreateView,
    CandidateUpdateView,
    CandidateDeleteView,
    ClientListView,
    #CandidateSearch,
    SearchResultsView,
)
from . import views
from clients import views as user_views

urlpatterns = [
    path('user/', CandidateListView.as_view(), name='candidates-home'),
    path('candidate/<int:pk>/', CandidateDetailView.as_view(), name='candidates-detail'),

    path('user/', CandidateListView.as_view(), name='candidates-home-overview'),
    #path('clientprofile/', user_views.clientprofile, name='clientprofile'),
    path('user/<str:username>', ClientListView.as_view(), name='client-name'),
    
    #path('candidate/<int:pk>/', CandidateSearch.as_view(), name='candidates-search'),






    path('candidate/new/', CandidateCreateView.as_view(), name='candidates-create'),
    path('candidate/<int:pk>/update/', CandidateUpdateView.as_view(), name='candidates-update'),
    path('candidate/<int:pk>/delete/', CandidateDeleteView.as_view(), name='candidates-delete'),
    path('about/', views.about, name='candidates-about'),
    path('search/', views.search, name='candidates-search'),
    path('admin/', admin.site.urls, name='admin'),
    path('search/results/', SearchResultsView.as_view(), name='search-results'),
]

if settings.DEBUG:
    import debug_toolbar
    urlpatterns = [
        path('__debug__/', include(debug_toolbar.urls)),

        # For django versions before 2.0:
        # url(r'^__debug__/', include(debug_toolbar.urls)),

    ] + urlpatterns