from django.shortcuts import render,redirect
from django.http import HttpResponse
from AdminApp.models import Book,Category
from UserApp.models import UserInfo,MyCart
# Create your views here.
def homepage(request):
    cats = Category.objects.all()   
    books = Book.objects.all()
    return render(request,"homepage.html",{"cats":cats,"books":books})

def ViewBooks(request,cid):
    cats = Category.objects.all() 
    #select * from books where cid = cid
    #Get the category object
    cat = Category.objects.get(id=cid)
    #We will get books filtered based on category
    books = Book.objects.filter(category = cat)
    return render(request,"homepage.html",{"cats":cats,"books":books,"cat":cat})

def ViewDetails(request,book_id):
    if request.method == "GET":
        cats = Category.objects.all()
        book = Book.objects.get(id=book_id)
        return render (request,"ViewDetails.html",{"cats":cats,"book":book})
    else:
        if "uname" in request.session:
            book_id = request.POST["book_id"]
            book = Book.objects.get(id=book_id)
            user = UserInfo.objects.get(username=request.session["uname"])
            qty = request.POST["qty"]
            try:
                cart = MyCart.objects.get(book=book,user=user)
            except:
                cart = MyCart(user=user,book=book,qty=qty)
                cart.save()
                return redirect(homepage)
            else:   
                return HttpResponse("Duplicat, itam is alrady present")
        else:
            return redirect(login)

def showcart(request):
    if request.method=="GET":
        if "uname" in request.session:
            cats = Category.objects.all()
            user = UserInfo.objects.get(username=request.session["uname"])
            items = MyCart.objects.filter(user=user)
            total = 0
            for item in items:
                total += item.book.price*item.qty
            request.session["total"] = total
            return render(request,"showcart.html",{"cats":cats,"items":items})
        else:
            return redirect(login)
    else:
        pass

def login(request):
    if request.method == "GET":
        return render(request,"login.html")
    else:
        uname = request.POST["uname"]
        pwd = request.POST["pwd"]
        #It willthoug exeption if Username and password doent match
        try:
            user = UserInfo.objects.get(username=uname , password=pwd) 
        except:
            #login has failed
            return redirect(login)
        else:
            # Login is successful
            request.session["uname"]=uname
            return redirect(homepage)
        

def signup(request):
    if request.method == "GET":
        return render(request,"signup.html")
    else:
        uname = request.POST["uname"]
        pwd = request.POST ["pwd"]
        #It willthoug exeption if Username and password doent match
        try:
            user = UserInfo.objects.get(username=uname) 
        except:
            #User is not present
            user= UserInfo(username=uname,password=pwd)
            user.save()
            return redirect(login)
        else:
            #User is alrady present
            return redirect(signup)

def logout(request):
    request.session.clear()
    return redirect(homepage)

