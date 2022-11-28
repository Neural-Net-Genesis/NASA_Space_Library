from django.shortcuts import render
import requests
# Create your views here.
"""
import json
import requests

response = requests.get("https://api.stackexchange.com/2.3/questions?order=desc&sort=activity&site=stackoverflow")



for data in response.json()['items']:
    print(data['title'])
    print(data['link'])
    print()
    print()

"""

def home(request):
    
    rec = []
    response = requests.get("https://api.nasa.gov/planetary/apod?api_key=e8YMmxeE0PF0Qbji0iAtmGUFt4uhCcc6lADJYfoH")

    cpy = response.json()["copyright"]
    date = response.json()["date"]
    title = response.json()["title"]
    exp = response.json()["explanation"]
    img = response.json()["url"]

    dct = [
        {'copy':cpy, 'date':date, 'title':title, 'exp':exp, 'img':img},
    ]

    employees = [
          {'ID':1,'name':'Jim','age':35},
          {'ID':2,'name':'Jane','age':25},
    ]
    return render(request, 'library/home.html', {"resp":dct})