from django.urls import path
from . import views 
app_name = "speakersd"

urlpatterns = [
    path('', views.home, name='home'),
    #path('about/', views.about, name='about'),
    path('AddSpeaker/', views.AddSpeaker.as_view(), name='addspeaker'),
    path('SpeakersList/', views.SpeakerListView.as_view(), name='speakerlist'),
    path('SpeakersList/Speaker/<pk>/', views.SpeakerDetailView.as_view(), name='speaker-detail'),
]