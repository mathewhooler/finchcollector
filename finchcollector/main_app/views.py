from django.shortcuts import render
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from .models import Finch



def home(request):
    # Include the .html file extension - unlike when rendering EJS templates
    return render(request, 'home.html')

def about(request):
    # Include the .html file extension - unlike when rendering EJS templates
    return render(request, 'about.html')

def index(request):
    # Include the .html file extension - unlike when rendering EJS templates
    finches = Finch.objects.all()
    return render(request, 'finches/index.html', {'finches': finches})

def finches_detail(request, finch_id):
    finch = Finch.objects.get(id=finch_id)
    return render(request, 'finches/detail.html', {'finch': finch} )

class FinchCreate(CreateView):
  model = Finch
  fields = '__all__'
  success_url = '/finches'

class FinchUpdate(UpdateView):
  model = Finch
  fields = '__all__'

class FinchDelete(DeleteView):
  model = Finch
  success_url = '/finches'
