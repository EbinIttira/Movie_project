from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.views.generic.edit import DeleteView
from. models import movies
from.forms import MovieForm

# Create your views here.
def display(request):
    movie=movies.objects.all()
    return render(request,'index.html',{'moviekey':movie})

def detail(request,movie_id):
    movie=movies.objects.get(id=movie_id)
    return render(request,"detail.html",{'movie':movie})

def add(request):
    if request.method == 'POST':
        name=request.POST.get('name')
        desc=request.POST.get('desc')
        year=request.POST.get('year')
        img=request.FILES['img']
        movie=movies(name=name,desc=desc,year=year,img=img)
        movie.save()
    return render(request,'add.html')

def update(request,id):
    movie=movies.objects.get(id=id)
    form=MovieForm(request.POST or None,request.FILES,instance=movie)
    if form.is_valid():
        form.save()
        return redirect('/')
    return render(request,'edit.html',{'form':form,'movie':movie})

class MovieDeleteview(DeleteView):
    model=movies
    template_name ='delete.html'
    success_url = reverse_lazy('movieapp:display')