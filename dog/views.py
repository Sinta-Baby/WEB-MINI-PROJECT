from django.shortcuts import render
from adminside.models import Breeddb
from django.http import HttpResponse
import pandas as pd
import joblib
import os

# Create your views here.
def homepage(request):
    return render(request,"home.html")
def initial_select(request):
    data = Breeddb.objects.all()
    return render(request,"Alpha_Selection.html", {'data': data})

def filtered_breed(request,fletter):
    data = Breeddb.objects.filter(Alpha_name=fletter)
    return render(request,"Filtered_Breeds.html", {'data': data})
def single_breed(request,b_id):
    dog = Breeddb.objects.get(id=b_id)
    return render(request,"Single_breed.html",{'dog':dog})

# def get_nutri(request):
#     return render(request,"Nutrition.html")

def get_nutri(request,b_id):
    data = Breeddb.objects.get(id=b_id)
    if request.method == 'POST':
        # Load model and encoder
        model_filename = "dog/static/datafolders/random_forest_model.joblib"
        encoder_filename = "dog/static/datafolders/encoder.joblib"
        model = joblib.load(model_filename)
        encoder = joblib.load(encoder_filename)

        # Get user input for features
        breed = request.POST.get('breed').lower().strip()
        age = float(request.POST.get('age'))
        weight = float(request.POST.get('weight'))
        activity_level = request.POST.get('activity_level')

        # Create DataFrame with user input
        user_data = pd.DataFrame({
            'Dog Breed': [breed],
            'Age': [age],
            'Weight (kg)': [weight],
            'Activity Level': [activity_level]
        })

        # Apply encoding to categorical columns
        categorical_cols = ['Dog Breed', 'Activity Level']
        user_data[categorical_cols] = encoder.transform(user_data[categorical_cols])

        # Make prediction
        nutrition_prediction = model.predict(user_data)

        return render(request, 'Nutrition_Result.html', {'nutrition': nutrition_prediction[0],'data':data})
    else:
        return render(request, 'Nutrition.html',{'data':data})

def gallery(request):
    data = Breeddb.objects.all()
    return render(request,"Gallery.html",{'data':data})
def about(request):
    return render(request,"About.html",)

def blog(request):
    return render(request,"Blog.html",)
def contact(request):
    return render(request,"Contact.html",)
def training(request):
    return render(request,"training.html",)
def grooming(request):
    return render(request,"grooming.html",)
def dog_nutri(request):
    return render(request,"dog_nutri.html",)



def chatbot_view(request):
    return render(request, 'chatbot.html')



