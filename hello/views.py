import os
from django.shortcuts import render
from django.http import HttpResponse
import requests
from .models import Greeting

admin=int(os.environ.get('adminURL',3))

# Create your views here.
def index(request):
	times = int(os.environ.get('TIMES',3))
	return HttpResponse('Hello! ' * times)
	r = requests.get('http://httpbin.org/status/418')
	print r.text
	return HttpResponse('<pre>' + r.text + '</pre>')
	retrieveArray(admin)

def retrieveArray (url):
    try:
        Ws= requests.get(url)
        yy= Ws.text
        global results
        results = yy.splitlines()

        print ('stopwords ------------')
        print (results)
        return (results)
        print ('--------')
    
        print ('full list returned raw with line breaks --------')
        #print (yy)
        print ('results for '+url+' --------')
        # print (results)
        print ('--------')
        swCount=0
        for count in results:
            swCount+=1
        print ('count  for ' + url +'-----')
        print ('count = '+str(swCount))
        print (' end retrieveArray() ----------------------')
    # end retrieveArray
    except:
        print ('Can\'t connect to admin settings - no connection') 



def db(request):

    greeting = Greeting()
    greeting.save()

    greetings = Greeting.objects.all()

    return render(request, 'db.html', {'greetings': greetings})

