from django.shortcuts import render
from . import models

# Create your views here.

def index(request):
    return render(request, "index.html")

# file upload view
def upload(request, method=["GET", "POST"]):
    
    # upload files to the Document model
    model = models.Document()
    if request.method == "POST":
        name = request.POST["name"]
        file = request.FILES["file"]
        model.name = name
        model.file = file
        model.save()
    
    return render(request, "index.html")

# delete document from 