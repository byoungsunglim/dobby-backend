from django.http import HttpResponse
import requests, json


# Create your views here.
def photos(request, query):
    url = "https://api.unsplash.com/photos/random"
    
    if query == "null":
        query = ""

    params = {
        'client_id': 'e3c66d369193b9335bf39ed09d8bc816e9ab99e2cc35d9313f717f4861ea3d7b',
        'count': 30,
        'query': query 
    }
    res = requests.get(url, params=params)

    print(res.json())

    return HttpResponse(res, content_type="application/json")

    

    