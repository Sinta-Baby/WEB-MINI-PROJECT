from django.urls import path
from adminside import views
urlpatterns=[
    path('indexpage/',views.indexpage,name="indexpage"),
    path('add_breedpage/',views.add_breedpage,name="add_breedpage"),
    path('save_breed/',views.save_breed,name="save_breed"),
    path('display_breed/',views.display_breed,name="display_breed"),
    path('edit_breed/<int:b_id>/',views.edit_breed,name="edit_breed"),
    path('update_breed/<int:b_id>/',views.update_breed,name="update_breed"),
    path('delete_breed/<int:b_id>/',views.delete_breed,name="delete_breed"),

]