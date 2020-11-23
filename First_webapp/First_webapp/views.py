from django.http import HttpResponse
from django.shortcuts import render
import operator
from . import counter




def home(request):
    return render (request,'home.html', {'key1': 'This is from Python family'})


#def downloads(request):
 #   return HttpResponse ('<h1> Hello... Nothing in downloads </h1>')

def result(request):
    age = request.GET['user_age']
    name = request.GET['user_name']
    message = f'Hii,{name} you are {age} years old'
    article = request.GET['article']
    var_dict,word_count = counter.count(article)

    return render (request, 'result.html', {'age': message, 'article': article, 'word_count': word_count, 'dict_word': var_dict})