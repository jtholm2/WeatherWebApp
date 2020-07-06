from django.http import HttpResponse, HttpResponseRedirect
import requests, json
from django.urls import reverse
from django.template import loader
from django.shortcuts import render

def intro_page(request):
    print(request.POST)
    return render(request, 'index.html')

def weather_by_zipcode(request):
    your_zipcode = request.POST.get('your_zipcode','')
    response = requests.get("http://api.openweathermap.org/data/2.5/weather?zip=%s&appid=a4d2ce939cf4d5f3bff277a482a337ab" % str(your_zipcode)) 
    test_dict = response.json()
    primary_info_dictionary = test_dict.get("main")
    template = loader.get_template('weather_by_zipcode/weather_by_zipcode.html')
    context = {
               'primary_info_dictionary': primary_info_dictionary,
              }
    
    return HttpResponse(template.render(context, request))

