from django.shortcuts import render
from django.http import HttpResponse, Http404,JsonResponse
from .models import Tweet

# Create your views here.

def home_view(request, *args, **kwrgs):
    print(args,kwrgs)
    return render(request, 'pages/home.html', context={},status=200)

def tweets_list_view(request,*args, **kwrgs):
    """
    Rest API is consumed by javascript ,java 
    and other programming languages and return json format
    """
    objList=Tweet.objects.all()
    tweetsList=[{"id":i.id,"content":i.content} for i in objList]
    data={
        "response":tweetsList        
    }
    return JsonResponse(data)

def tweets_detail_view(request,tid, *args, **kwrgs):
    print(tid)
    data={ 'id':tid
    }

    status=200
    try:
        obj=Tweet.objects.get(id=tid)
        data['content'] = obj.content
    except:
        data['message'] = 'Not Found'
        status=404
    

    return JsonResponse(data,status=status)
    