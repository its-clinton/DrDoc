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
        
    files = models.Document.objects.all()
    context = {"files": files}
    
    return render(request, "index.html", context=context)
