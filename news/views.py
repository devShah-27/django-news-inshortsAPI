from django.shortcuts import render
import requests

def index(request):
    url = 'https://inshorts.me/news/all?offset=0&limit=9'
    response = requests.get(url)
    news = response.json()['data']['articles']
    return render(request, 'news/index.html', {'news': news})

def top(request):
    url = 'https://inshorts.me/news/top?offset=0&limit=9'
    response = requests.get(url)
    news = response.json()['data']['articles']
    return render(request, 'news/top.html', {'news': news})

def trending(request):
    url = 'https://inshorts.me/news/trending?offset=0&limit=9'
    response = requests.get(url)
    news = response.json()['data']['articles']
    return render(request, 'news/trending.html', {'news': news})

def science(request):
    url = 'https://inshorts.me/news/topics/science?offset=0&limit=9'
    response = requests.get(url)
    news = response.json()['data']['articles']
    return render(request, 'news/science.html', {'news': news})

def entertainment(request):
    url = 'https://inshorts.me/news/topics/entertainment?offset=0&limit=9'
    response = requests.get(url)
    news = response.json()['data']['articles']
    return render(request, 'news/entertainment.html', {'news': news})

def sports(request):
    url = 'https://inshorts.me/news/topics/sports?offset=0&limit=9'
    response = requests.get(url)
    news = response.json()['data']['articles']
    return render(request, 'news/sports.html', {'news': news})


