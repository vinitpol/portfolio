from portfolio import views
from django.urls import path,include
from .views import contact_view

urlpatterns = [
    path('',views.home,name='home'),
    path('about',views.about,name='about'),
    path('certification',views.certification,name='certification'),
    path('project',views.project,name='project'),
    path('resume',views.resume,name='resume'),
    path('contact',views.contact_view,name='contact'),
]
