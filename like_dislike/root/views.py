from django.shortcuts import render
from .models import *

# Create your views here.

def like_dislike(request):
    likes = Like.objects.all().count() 
    if 'like' in request.POST:
        like_after = likes+1
        print(like_after)
        l = Like.objects.create(like = like_after)
    elif 'dislike' in request.POST:
        try:
            dislike =Like.objects.get(like=likes)
            dislike.delete()
            print(Like.objects.all().count())
        except:
            likes = 0
            print(likes)
    return render(request,'root/index.html',{"likes":likes})