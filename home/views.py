from django.shortcuts import render,HttpResponse ,redirect
from datetime import datetime
from home.models import Contact
from django.contrib import messages


# Create your views here.
def home(request):
    # return HttpResponse("Hello World")
    return render(request, "home.html", {"name": "John"})

def index(request):
    return render(request, "index.html")


def contact(request):
    if request.method == "POST":
        name = request.POST.get("name")
        email = request.POST.get("email")
        subject = request.POST.get("subject")
        message = request.POST.get("message")
        contact=Contact(name=name,email=email,subject=subject,message=message,date=datetime.today())
        contact.save()
        print(name, email, subject, message)
        messages.success(request, "Your message has been sent!")
    # return redirect(request, "contact.html")
    return redirect("/")