from django.shortcuts import render, get_object_or_404, redirect
from .models import Movie,Info,Comment
from .forms import movieForm,InfoForm, commentForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth import logout


def allcommnets(request,id):
    all_com= Comment.objects.all()
    movie=get_object_or_404(Movie,pk=id)
    movie_com = []
    for com in all_com:
        if com.movie == movie:
            movie_com.append(com)

    form = commentForm(request.POST or None)
    if request.method =="POST":
        comment=form.save(commit=False)
        comment.movie = movie
        comment.save()
        return redirect(allmovies)

    return render(request,"comments.html",{'comments':movie_com,'movies':movie,'form':form})

def allmovies(reqest):
    all_movies = Movie.objects.all()
    all_info= Info.objects.all()
    return render (reqest,"movies.html",{"all":all_movies})

@login_required
def newmovie(request):
    form =movieForm(request.POST or None ,  request.FILES or None)
    form_extr =InfoForm(request.POST or None )

    if all((form.is_valid(),form_extr.is_valid())):
        movie=form.save(commit=False)
        extr=form_extr.save()
        movie.spec_info = extr
        movie.save()
        return redirect(allmovies)

    return render(request, 'new_movie.html',{'form':form,'form_extr':form_extr,"new":True})

@login_required
def editmovie(request,id):
    movie=get_object_or_404(Movie,pk=id)
    try:
        extr = movie.spec_info
    except Info.DoesNotExist:
        extr =None

    form =movieForm(request.POST or None, request.FILES or None,instance=movie)
    form_extr =InfoForm(request.POST or None)

    if all((form.is_valid(),form_extr.is_valid())):
        movie=form.save(commit=False)
        extr=form_extr.save()
        movie.spec_info = extr
        movie.save()
        return redirect(allmovies)

    return render(request,'new_movie.html',{'form':form,'form_extr':form_extr,'new':False})

@login_required
def deletemovie(request,id):
     movie=get_object_or_404(Movie,pk=id)

     if request.method == "POST":
         movie.delete()
         return redirect(allmovies)

     return render(request,"confirm.html",{'movie': movie,})

def deletecoment(request,id):
     comment=get_object_or_404(Comment,pk=id)

     if request.method == "POST":
         comment.delete()
         return redirect(allmovies)

     return render(request,"confirm.html",{'movie': comment,})

def logout_view(request):
    logout(request)
    return redirect(allmovies)