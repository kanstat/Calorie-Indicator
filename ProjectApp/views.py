from django.shortcuts import render, HttpResponse
import requests
import json
from os import getenv
from dotenv import load_dotenv
load_dotenv()

# Create your views here.


def calorie(request):
    if request.method == 'POST':
        query = request.POST['query']
        url = 'https://api.api-ninjas.com/v1/nutrition?query='
        api_request = requests.get(
            url + query, headers={'X-Api-Key': getenv('api_key')})
        try:
            api = json.loads(api_request.content)
            print(api_request.content)

        except Exception as e:
            api = "oops! There was an error"
            print(e)
        return render(request, 'home.html', {'api': api})
    else:
        return render(request, 'home.html', {'query': "Enter a valid query"})
