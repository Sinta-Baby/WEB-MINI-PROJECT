from django.shortcuts import render, redirect
from adminside.models import Breeddb
from django.utils.datastructures import MultiValueDictKeyError
from django.core.files.storage import FileSystemStorage

# Create your views here.
def indexpage(request):
    return render(request,"index.html")
def add_breedpage(request):
    return render(request,"add_breed.html")
def save_breed(request):
    if request.method =="POST":
        br=request.POST.get('b_name')
        alp=request.POST.get('alpha')
        dp=request.POST.get('des')
        h=request.POST.get('hel')
        t=request.POST.get('tr')
        e=request.POST.get('ex')
        im=request.FILES['img']
        obj=Breeddb(Breed_name=br,Alpha_name=alp,Description=dp,Health=h,Training=t,Exercise=e,breed_image=im)
        obj.save()
        return redirect(add_breedpage)
def display_breed(request):
    data = Breeddb.objects.all()
    return render(request,"display.html",{'data':data})
def edit_breed(request,b_id):
    data = Breeddb.objects.get(id=b_id)
    return render(request,"edit_breed.html",{'data':data})

def update_breed(request,b_id):
    if request.method =="POST":
        br=request.POST.get('b_name')
        alp=request.POST.get('alpha')
        dp=request.POST.get('des')
        h=request.POST.get('hel')
        t=request.POST.get('tr')
        e=request.POST.get('ex')
        try:
            im = request.FILES['img']
            fs = FileSystemStorage()
            fs.save(im.name, im)
        except MultiValueDictKeyError:
            file = Breeddb.objects.get(id=b_id).breed_image
            Breeddb.objects.filter(id=b_id).update(Breed_name=br, Alpha_name=alp, Description=dp, Health=h, Training=t, Exercise=e, breed_image=file)
            return redirect(display_breed)
def delete_breed(request,b_id):
    x = Breeddb.objects.filter(id=b_id)
    x.delete()
    return redirect(display_breed)

