from django.shortcuts import render
finches = [
  {'name': 'Finchy', 'breed': 'Zebra', 'description': 'Black and white stripes like the crossing', 'age': 6},
  {'name': 'Finchette', 'breed': 'Purple', 'description': 'Purple Rain is their favourite song', 'age': 8},
]

def home(request):
    # Include the .html file extension - unlike when rendering EJS templates
    return render(request, 'home.html')

def about(request):
    # Include the .html file extension - unlike when rendering EJS templates
    return render(request, 'about.html')

def index(request):
    # Include the .html file extension - unlike when rendering EJS templates
    return render(request, 'finches/index.html', {'finches': finches})

