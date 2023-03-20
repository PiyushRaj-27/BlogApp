from django.shortcuts import render, HttpResponse,redirect
from django.contrib.auth import authenticate, login as login1, logout as logout1
# Create your views here.

def login(request):
    if request.method == "POST":
        uname = request.POST.get("username")
        password = request.POST.get("password")
        user = authenticate(username=uname, password=password)
        if user is not None:
            login1(request, user)
            try:
                nextlink = request.GET["next"]
                print(nextlink)
                return redirect(nextlink)
            except:
                return redirect("/blog")
        else:
            message = "Username or password invalid!"
            return render(request, "login.html", context= {"msg" : message})
    return render(request, "login.html")

def logout(request):
    logout1(request)
    
    return redirect("/blog")