from django.contrib import messages
from django.http import HttpResponse
from django.shortcuts import render, redirect
from newsapi import NewsApiClient

from .forms import AddNewsForm
from .models import Comment, AddNews

newsapi = NewsApiClient(api_key="297d30af40954978970d1d142514919e")


# Create your views here.
def index(request):
    everything = newsapi.get_top_headlines(country='us', page_size=10)['articles']

    business = newsapi.get_top_headlines(category="business", country='us', page_size=6)['articles']
    entertainment = newsapi.get_top_headlines(category="entertainment", country='us', page_size=6)['articles']
    general = newsapi.get_top_headlines(category="general", country='us', page_size=6)['articles']
    health = newsapi.get_top_headlines(category="health", country='us', page_size=6)['articles']
    science = newsapi.get_top_headlines(category="science", country='us', page_size=6)['articles']
    sports = newsapi.get_top_headlines(category="sports", country='us', page_size=6)['articles']
    technology = newsapi.get_top_headlines(category="technology", country='us', page_size=6)['articles']
    bbc = newsapi.get_top_headlines(sources='bbc-news', page_size=4)['articles']
    cnn = newsapi.get_top_headlines(sources='cnn', page_size=4)['articles']
    engadget = newsapi.get_top_headlines(sources='engadget', page_size=4)['articles']
    politico = newsapi.get_top_headlines(sources='politico', page_size=4)['articles']
    foxNews = newsapi.get_top_headlines(sources='fox-news', page_size=4)['articles']
    theWallStreetJournal = newsapi.get_top_headlines(sources='the-wall-street-journal', page_size=4)['articles']
    theWashingtonPost = newsapi.get_top_headlines(sources='the-washington-post', page_size=4)['articles']

    # context ={
    #     'everything':everything
    # }

    context = {

        'bbc': bbc,
        'cnn': cnn,
        'engadget': engadget,
        'politico': politico,
        'foxNews': foxNews,
        'theWallStreetJournal': theWallStreetJournal,
        'theWashingtonPost': theWashingtonPost,
        'everything': everything,
        'business': business,
        'entertainment': entertainment,
        'general': general,
        'health': health,
        'science': science,
        'sports': sports,
        'technology': technology,
    }

    return render(request, 'pages/index.html', context)


def sources(request):
    bbc = newsapi.get_top_headlines(sources='bbc-news', page_size=6)['articles']
    cnn = newsapi.get_top_headlines(sources='cnn', page_size=6)['articles']
    engadget = newsapi.get_top_headlines(sources='engadget', page_size=6)['articles']
    politico = newsapi.get_top_headlines(sources='politico', page_size=6)['articles']
    foxNews = newsapi.get_top_headlines(sources='fox-news', page_size=6)['articles']
    theWallStreetJournal = newsapi.get_top_headlines(sources='the-wall-street-journal', page_size=6)['articles']
    theWashingtonPost = newsapi.get_top_headlines(sources='the-washington-post', page_size=6)['articles']

    context = {
        'bbc': bbc,
        'cnn': cnn,
        'engadget': engadget,
        'politico': politico,
        'foxNews': foxNews,
        'theWallStreetJournal': theWallStreetJournal,
        'theWashingtonPost': theWashingtonPost,
    }

    return render(request, 'pages/sources.html', context)


def singlepost(request):
    verge = newsapi.get_top_headlines(sources='the-verge', page_size=3)['articles']
    techcrunch = newsapi.get_top_headlines(sources='techcrunch', page_size=3)['articles']
    if (request.method == 'POST'):
        title = request.POST['title']
        description = request.POST['description']
        image = request.POST['image']
        url = request.POST['url']
        date = request.POST['date']
        author = request.POST['author']

    if '_reply' in request.POST:
        content = request.POST['content']
        username = request.POST['name']
        comment_id = request.POST['comment_id']
        comment_qs = None
        if comment_id:
            comment_qs = Comment.objects.get(id=comment_id)
        comment = Comment.objects.create(title=title, username=username, content=content, reply=comment_qs)
        comment.save()

    if '_comment' in request.POST:
        content = request.POST['content']
        username = request.POST['name']
        comment = Comment.objects.create(title=title, username=username, content=content)
        comment.save()

    comments = Comment.objects.order_by('-created_on').filter(reply=None)

    context = {
        'title': title,
        'description': description,
        'image': image,
        'url': url,
        'date': date,
        'author': author,
        'verge': verge,
        'techcrunch': techcrunch,
        'comments': comments,
    }

    return render(request, 'pages/singlenews.html', context)


def business(request):
    business = newsapi.get_top_headlines(category="business", country='us', page_size=21)['articles']

    context = {
        'business': business,
    }

    return render(request, 'category/business.html', context)


def entertainment(request):
    entertainment = newsapi.get_top_headlines(category="entertainment", country='us', page_size=21)['articles']

    context = {
        'entertainment': entertainment,
    }

    return render(request, 'category/entertainment.html', context)


def general(request):
    general = newsapi.get_top_headlines(category="general", country='us', page_size=21)['articles']

    context = {
        'general': general,

    }

    return render(request, 'category/general.html', context)


def sports(request):
    sports = newsapi.get_top_headlines(category="sports", country='us', page_size=21)['articles']

    context = {
        'sports': sports,
    }

    return render(request, 'category/sports.html', context)


def technology(request):
    technology = newsapi.get_top_headlines(category="technology", country='us', page_size=21)['articles']

    context = {
        'technology': technology,
    }

    return render(request, 'category/technology.html', context)


def science(request):
    science = newsapi.get_top_headlines(category="science", country='us', page_size=21)['articles']

    context = {
        'science': science,

    }

    return render(request, 'category/science.html', context)


def health(request):
    health = newsapi.get_top_headlines(category="health", country='us', page_size=21)['articles']

    context = {
        'health': health,

    }

    return render(request, 'category/health.html', context)


def search(request):
    if request.method == 'POST':
        query = request.POST['search']
        querysearch = newsapi.get_everything(q=query, page_size=21)['articles']

    context = {
        'querysearch': querysearch
    }
    return render(request, 'pages/search.html', context)


def addnews(request):
    verge = newsapi.get_top_headlines(sources='the-verge', page_size=3)['articles']
    techcrunch = newsapi.get_top_headlines(sources='techcrunch', page_size=3)['articles']
    if request.method == 'POST':
        form = AddNewsForm(request.POST)
        if form.is_valid():
            form.save()
        messages.success(request, "The News has been received.")

    form = AddNewsForm()

    context={
        'verge':verge,
        'techcrunch':techcrunch,
        'form':form,
    }


    return render(request, 'pages/form.html', context)

def postednews(request):
    news = AddNews.objects.filter(to_publish=True).order_by('-created_on')

    return render(request,'pages/postednews.html',{'news':news})