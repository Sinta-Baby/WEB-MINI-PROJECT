from django.urls import path
from dog import views

from .views import chatbot_view


urlpatterns = [
    path('',views.homepage,name="homepage"),
    path('initial_select/',views.initial_select,name="initial_select"),
    path('filtered_breed/<fletter>/',views.filtered_breed,name="filtered_breed"),
    path('single_breed/<int:b_id>/',views.single_breed,name="single_breed"),
    path('get_nutri/<int:b_id>/',views.get_nutri,name="get_nutri"),
    path('gallery/',views.gallery,name="gallery"),
    path('about/',views.about,name="about"),
    path('blog/',views.blog,name="blog"),
    path('contact/',views.contact,name="contact"),
    path('training/',views.training,name="training"),
    path('grooming/',views.grooming,name="grooming"),
    path('dog_nutri/',views.dog_nutri,name="dog_nutri"),
    path('chatbot/', chatbot_view, name='chatbot'),







]