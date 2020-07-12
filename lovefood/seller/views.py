from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.http import HttpResponse, HttpResponseRedirect, JsonResponse
from django.urls import reverse
#from django.contrib.auth.models import User
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.http import HttpResponse, HttpResponseRedirect, JsonResponse
from django.urls import reverse
#from django.contrib.auth.models import User
from django.contrib import messages
from user.models import *
# Create your views here.

def index(request):  
    if not request.user.is_authenticated:
        return render(request, 'seller/index.html')
    
    user = User.objects.get(email=request.user.email)
    seller_name = str(user.seller.name)
    return HttpResponseRedirect(reverse("seller", args=(seller_name,)))

    '''
    user = User.objects.get(email=request.user.email)
    seller_name = str(user.seller.name)
    context = {
        "seller_name" : seller_name
    }
    return render(request, 'seller/seller.html', context)
    '''


def login_seller(request):
    email = request.POST.get("email")
    password = request.POST.get("password")
    user = authenticate(request, email=email, password=password)
    
    if user is not None:
        login(request, user)
        user = User.objects.get(email=request.user.email)
        seller_name = str(user.seller.name)
        return HttpResponseRedirect(reverse("seller", args=(seller_name,)))

        #return HttpResponseRedirect(reverse("seller"))
        #return JsonResponse({"success": True})
    else:
        return render(request, "seller/index.html", {"message": "Invalid credentials."})

        #messages.warning(request, "Please provide correct username and password.")
        #return JsonResponse({"success": False})

def logout_seller(request):
    logout(request)
    return JsonResponse({"logout": True})

def seller(request, seller_name):
   # user = User.objects.get(email='f')
   # seller_name = str(user.seller.name)
    context = {
        "seller_name" : seller_name
    }
    return render(request, 'seller/seller.html', context)


def register_seller(request):

    if request.method == 'POST':

        name = request.POST.get('restaurant_name')
        email = request.POST.get('email')
        address = request.POST.get('address')
        contact = request.POST.get('contact')
        password = request.POST.get('password')
        confirm_password = request.POST.get('confirm_password')
        homeornot = request.POST.get('homeornot')

        if password == confirm_password:
            try:
                if  User.objects.get(email=email):
                    messages.error(request, "Username or email already exists.")
                    return JsonResponse({"Username or email already exists": True})
            except User.DoesNotExist:
                user = User.objects.create_user(user_type=2, email=email, password=password)
                seller = Seller.objects.create(user=user,name=name, address=address, contact=contact,homeornot=homeornot )
                messages.success(request, "Account created")

                user_log = authenticate(request, email=email, password=password)
                login(request, user_log)
                user = User.objects.get(email=request.user.email)
                seller_name = str(user.seller.name)
                return HttpResponseRedirect(reverse("seller", args=(seller_name,)))


                #return HttpResponseRedirect(reverse('login_seller'))
        else:
            messages.error(request, "Passwords do not match")
            return  JsonResponse({"Passwords do not match": True})

    if request.method == 'GET':
        return HttpResponseRedirect(reverse("seller_index"))

def getlist(request, seller_name):
    itemlist = []
    user = User.objects.get(email=request.user.email)
    seller = user.seller
    count = str(seller.cooks.all().count())
    for i in range(1, int(count) + 1):
        dish = seller.cooks.get(pk=i)
        dish_name = dish.name
        itemlist.append(dish_name)
    
    return JsonResponse({
        "itemlist": itemlist
    })





def getitems(request, seller_name):
    
    user = User.objects.get(email=request.user.email)
    seller = user.seller
    count = str(seller.cooks.all().count())
    items = [
        {
        "name":"abc", 
        "summary":"abc", 
        "nationality":"abc", 
        "no_of_serving":0, 
        "picture":"xyz.jpg",
        "glutten_free":"N",
        "customizable":"N"
     }]
    for i in range(1, int(count) + 1):
        item = seller.cooks.get(pk=i)
        items.append({"name" : str(item.name), "summary" : str(item.summary), "nationality" : str(item.nationality), "no_of_serving" : int(item.no_of_serving),"picture" : str(item.picture), "category" : str(item.category) , "glutten_free" : str(item.glutten_free), "customizable" : str(item.customizable)})
    #items = seller.cooks.all()
    return JsonResponse({
        "items": items
    })
