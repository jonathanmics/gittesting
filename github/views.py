from django.shortcuts import render
from github import urls
import os
from localStoragePy import localStoragePy
# Create your views here.


def index(request):
        nam = request.COOKIES.get('tweet')
        if nam == "" :
            return render(request, 'index.html')
        else:
            nam2 = request.COOKIES.get('tweet')
            f = open('D:/django_practise/gitest/templates/index.html','a')
            data =  f.write("\n<div>" + nam2 + "</div>\n")
            f.close()
            return render(request, 'index.html')



   