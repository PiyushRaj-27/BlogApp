from django.shortcuts import render, HttpResponse, redirect
from .models import BLOG
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
loginInfo = 0
# Create your views here.
def index(request):
    if request.method == "POST":
        uname = request.POST.get('username')
        email = request.POST.get('email')
        password = request.POST.get("password")

        user = User.objects.create_user(uname,email,password)
        user.save()

    alldata = BLOG.objects.all()
    isuser = request.user.is_authenticated
    return render(request,"blog.html", context= {"blogs" : alldata, "isuser": isuser})

@login_required
def write(request):
    uname = request.user.username
    return render(request,'writeblog.html', context= {"uname": uname})

def edit(request, title):
    reblog = BLOG.objects.all().filter(Title = title)
    # print(reblog)
    found = False
    if reblog is not None:
        found = True
    return render(request,"editblog.html", context = {"blogs" : reblog , "found": found})

@login_required
def myblogs(request):
    uname = request.user.username
    ublogs = BLOG.objects.all().filter(author = uname)
    return render(request,"myblog.html", context= {"blogs" : ublogs, "uname" : uname})


def save(request):
    blogtitle = request.POST.get('titlefield')
    blogbody = request.POST.get('bodyfield')
    author = request.user.username
    obj1 = BLOG()
    obj1.Title = blogtitle
    obj1.body = blogbody
    obj1.author = author
    obj1.save()

    return redirect("/blog/myblogs")

def update(request):
    title = request.POST.get("titlefield")
    toUpdate = BLOG.objects.all().filter(Title = title)
    print(toUpdate)
    for blog in toUpdate:
        blog.body = request.POST.get("bodyfield")
        blog.save()
    return redirect("/blog/myblogs")

def viewblog(request, title):
    reblog = BLOG.objects.all().filter(Title = title)
    found = False
    try:
        blog1 = reblog[0]
        found = True
    except:
        found = False
    return render(request,"viewblog.html", context={"blog":reblog, "found":found})