from django.shortcuts import render
from django.http import HttpResponse

from matplotlib.style import context

# Create your views here.
def index(request):
   context={
      'name':'Patrick',
      'age':23,
      'nationality':'British',
   }
   #return HttpResponse(request, 'Hey, Welcome')
   return render(request,'index.html',context) 

def counter(request):
      text=request.POST['text']
      amount_of_words=len(text.split()) 
      return render(request,'counter.html',{'amount':amount_of_words})