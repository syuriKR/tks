from django.http import HttpResponse
from django.shortcuts import render
from .forms import PriceForm
from .forms import CalorieForm
from .forms import button
from .models import Menu
from itertools import chain

# Create your views here
def home(request):
    return render(request,'roson/home.html')

def menu(request):
    data = Menu.objects.all()
    params={
        'form':button(),
        }

    if(request.method == 'POST'):
        request_num = request.POST['choice']
        request_num2= request.POST['choice2']
        int_request_num2 = int(request_num2)
        if(request_num == '0'):
            data = Menu.objects.filter(judge=int_request_num2).order_by('price').reverse()
        elif(request_num == '1'):
            data = Menu.objects.filter(judge=int_request_num2).order_by('price')
        elif(request_num == '2'):
            data = Menu.objects.filter(judge=int_request_num2).order_by('calorie').reverse()
        else:
            data = Menu.objects.filter(judge=int_request_num2).order_by('calorie')
        params['data']=data
        params['form']=button(request.POST)
        params['num']=request_num
        params['num2']=request_num2
    return render(request,'roson/menu.html',params)

def pricegacha(request):
    params={
        'form':PriceForm(),
    }
    if(request.method == 'POST'):
        request_price = request.POST['price']
        int_request_price = int(request_price)

        params['form']=PriceForm(request.POST)

        int_total_price = 0
        int_total_calorie = 0

        Truedata = Menu.objects.filter(price__lte=int_request_price).order_by("?")[0:1]
        for item in Truedata:
            int_item_price=int(item.price)
            int_item_calorie=int(item.calorie)

            int_total_price += int_item_price
            int_total_calorie += int_item_calorie

            int_request_price -= int_item_price

        i = 1
        while i<10:
            if Menu.objects.filter(price__lte=int_request_price).count()<=0:
                break
            data = Menu.objects.filter(price__lte=int_request_price).order_by("?")[0:1]
            for item in data:
                int_item_price=int(item.price)
                int_item_calorie=int(item.calorie)

                int_total_price += int_item_price
                int_total_calorie += int_item_calorie

                int_request_price -= int_item_price
            Truedata=list(chain(Truedata,data))
            i+=1
        params['total_price']=int_total_price
        params['total_calorie']=int_total_calorie
        params['data']=Truedata

    return render(request,'roson/pricegacha.html',params)

def caloriegacha(request):
    params={
        'form':CalorieForm(),
    }
    if(request.method == 'POST'):
        request_calorie = request.POST['calorie']
        int_request_calorie = int(request_calorie)

        params['form']=CalorieForm(request.POST)

        int_total_price = 0
        int_total_calorie = 0

        Truedata = Menu.objects.filter(calorie__lte=int_request_calorie).order_by("?")[0:1]
        for item in Truedata:
            int_item_price=int(item.price)
            int_item_calorie=int(item.calorie)

            int_total_price += int_item_price
            int_total_calorie += int_item_calorie

            int_request_calorie -= int_item_calorie

        i = 1
        while i<10:
            if Menu.objects.filter(calorie__lte=int_request_calorie).count()<=0:
                break
            data = Menu.objects.filter(calorie__lte=int_request_calorie).order_by("?")[0:1]
            for item in data:
                int_item_price=int(item.price)
                int_item_calorie=int(item.calorie)

                int_total_price += int_item_price
                int_total_calorie += int_item_calorie

                int_request_calorie -= int_item_calorie
            Truedata=list(chain(Truedata,data))
            i+=1
        params['total_price']=int_total_price
        params['total_calorie']=int_total_calorie
        params['data']=Truedata

    return render(request,'roson/caloriegacha.html',params)

def simulator(request):
    if (request.method == "GET"):
        data = Menu.objects.all()
        menus = [[] for i in range(15)]
        for i in data:
            menus[i.judge].append(i)
        categories = {
            "お惣菜":"osozai",
            "お惣菜サラダ":"osozai_salad",
            "弁当":"bento",
            "チルド弁当":"childbento",
            "デザート":"desert",
            "揚げ物":"fly",
            "冷凍食品":"child",
            "グラタン":"gratin",
            "インスタント":"instant",
            "粉物":"konamono",
            "麺類":"noodle",
            "おにぎり":"onigiri",
            "パスタ":"pasta",
            "サラダ":"salad",
            "スープ":"soup"
        }
        categorie_name = {
            "osozai": menus[0],
            "osozai_salad" : menus[1],
            "bento" : menus[2],
            "childbento" : menus[3],
            "desert" : menus[4],
            "fly" : menus[5],
            "child" : menus[6],
            "gratin" : menus[7],
            "instant" : menus[8],
            "konamono" : menus[9],
            "noodle" : menus[10],
            "onigiri" : menus[11],
            "pasta" : menus[12],
            "salad" : menus[13],
            "soup" : menus[14]
        }
        param = {"menus": menus, "categories" : categories, "categorie_name":categorie_name}
        return render(request,'roson/simulator.html', param)

def sim_result(request):
    nums = request.POST.getlist("checks")
    data = Menu.objects.all()
    hoge = [i for i in data if str(i.nameid) in nums]
    price = 0
    energy = 0
    for i in hoge:
        price += i.price
        energy += i.calorie
    param = {"data": hoge,
             "price": price,
             "energy": energy
    }
    return render(request, 'roson/result.html', param)
