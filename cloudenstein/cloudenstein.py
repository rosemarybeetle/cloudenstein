import os
from django.shortcuts import render
from django.http import HttpResponse
import requests
from .models import Greeting

adminURL='https://docs.google.com/spreadsheet/pub?key=0AgTXh43j7oFVdGp1NmxJVXVHcGhIel9CNUxJUk8yYXc&output=csv'


# Create your views here.
def index(request):
	#times = int(os.environ.get('TIMES',3))
	#return HttpResponse('Hello! ' * times)
	t=requests.get(adminURL)
	# return HttpResponse(t.text)
	#r = requests.get('http://httpbin.org/status/418')
	#print r.text
	#return HttpResponse('<pre>' + r.text + '</pre>')
	retrieveArray(adminURL)
	return HttpResponse(results[0]+' test. swCount= '+str (swCount))

def retrieveArray (url):
    try:
        Ws= requests.get(url)
        yy= Ws.text
        global results
        results = yy.splitlines()
        global swCount
        swCount=len(results)       
        return (results)
        return swCount
    # end retrieveArray
    except:
        print ('Can\'t connect to admin settings - no connection') 



def db(request):

    greeting = Greeting()
    greeting.save()

    greetings = Greeting.objects.all()

    return render(request, 'db.html', {'greetings': greetings})

