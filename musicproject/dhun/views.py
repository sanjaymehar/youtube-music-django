from dataclasses import field
from multiprocessing import context
from platform import release
from pyexpat import model
from turtle import title
from django.contrib.auth.models import User
from re import template
from urllib import request
from django.shortcuts import redirect, render,get_object_or_404
from django.http import HttpResponse
from .models import Album, Song, Profile
from django.contrib.auth import login,logout,authenticate
from .form import Register,Login
from django.views import generic
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.models import User
from django.urls import reverse_lazy
from rest_framework.decorators import api_view


def home(request):
    a=Album.objects.all()
    return render(request,"dhun/home.html",{"dinu":a})
#render(HttpRequest,template_file_name,context_data)

def detail(request,pk):
    al=get_object_or_404(Album,id=pk)
    return render(request,"dhun/songs.html",{'deepu':al})

def signup(request):
    f=Register(request.POST or None)
    if f.is_valid():
        data=f.save(commit=False)
        p=f.cleaned_data.get('password')
        data.set_password(p)
        data.save()
        return redirect("dhun:signin")
    return render(request,"dhun\login.html",{'form':f})

def signin(request):
    f=Login(request.POST or None)
    if f.is_valid():
        u=f.cleaned_data.get("username")
        p=f.cleaned_data.get("password")
        usr=authenticate(username=u,password=p)
        nxt=request.GET.get("next")
        if usr:
            login(request,usr)  
        if nxt:
            return redirect(nxt) 
        return redirect("dhun:home")
    return render(request,"dhun\login.html",{'form':f})

def signout(request):
    logout(request)
    return redirect("dhun:home")

class Add_Album(LoginRequiredMixin,generic.CreateView):
    login_url='dhun:signin'
    template_name="dhun/album.html"
    model=Album
    fields=['title','release','genre','image']
    context_object_name='form'
    def form_valid(self,form):
        form.instance.uid=User.objects.get(username=self.request.user.username)
        return super().form_valid(form)

class Upalbum(LoginRequiredMixin,generic.UpdateView):
    login_url='dhun:signin'
    template_name="dhun/album.html"
    model=Album
    fields=['title','release','genre','image']
    context_object_name='form'

class Delalbum(LoginRequiredMixin,generic.DeleteView):
    login_url='dhun:signin'
    template_name="dhun/delalbum.html"
    model=Album
    success_url=reverse_lazy("dhun:home")
    context_object_name='data'

class Add_song(LoginRequiredMixin,generic.CreateView):
    login_url='dhun:signin'
    template_name="dhun/album.html"
    model=Song
    fields=['title','genre',"lyricists",'file']
    context_object_name='form'
    def form_valid(self,form):
        form.instance.alid=Album.objects.get(id=self.kwargs.get('pk'))
        return super().form_valid(form)

class Upsong(LoginRequiredMixin,generic.UpdateView):
    login_url='dhun:signin'
    template_name="dhun/album.html"
    model=Song
    fields=['title','genre',"lyricists",'file']
    context_object_name='form'
    
class Delsong(LoginRequiredMixin,generic.DeleteView):
    login_url='dhun:signin'
    template_name="dhun/delalbum.html"
    model=Song
    success_url=reverse_lazy("dhun:home")
    context_object_name='data'

class Myhome(generic.ListView):
    template_name='dhun/myhome.html'
    context_object_name='dinu'
    def get_queryset(self):
        u=User.objects.get(username=self.request.user.username)
        return  u.album_set.all()

class addProfile(LoginRequiredMixin,generic.CreateView):
    login_url='dhun:signin'
    model = Profile
    template_name = "dhun/album.html"
    fields=['photo','phone','bio']
    context_object_name='form'
    def form_valid(self,form):
        form.instance.uid=User.objects.get(username=self.request.user.username)
        form.save()
        return super().form_valid(form)
       
class Uprofile(LoginRequiredMixin,generic.TemplateView):
    login_url='dhun:signin'
    template_name = "dhun/profile.html"

class UPProfile(LoginRequiredMixin,generic.UpdateView):
    login_url='dhun:signin'
    model = Profile
    template_name = "dhun/album.html"
    fields=['photo','phone','bio']
    context_object_name='form'

def search(request):
    query= request.GET['query']
    if len(query) > 78:
        allsongs = Song.objects.none()
    else:
        allsongstitle=Album.objects.filter(title__icontains=query)
        allsongsrelease=Album.objects.filter(release__icontains=query)
        allsongsgenre=Album.objects.filter(genre__icontains=query)
        allsongs = allsongstitle.union(allsongsrelease,allsongsgenre)
            
    lets={'Album':allsongs,'query':query}
    return render(request,'dhun/search.html',lets)

