from django.shortcuts import render
from django.shortcuts import render,redirect,get_object_or_404,reverse
from .form import ProductsForm
from.models import Products
import requests
from bs4 import BeautifulSoup as bs
import json

# Create your views here.


data1 = {"lol": []}

nams = []
prices = []

z = ["a9", "b17", "c13", "d6", "e1", "f1", "g15", "h8", "j19", "k4","l5","m6","n7","d8","c9"]


def lol(url):
    # id=["ptglol1","ptglol2","ptglol3","ptglol4"]
    r = requests.get(url)
    soup = bs(r.content, "lxml")
    i = 0
    names = soup.find_all("div", {"class": "name"})
    price = soup.find_all("span", {"class": "price-new"})

    for name in names:
        nams.append(name.text)

    for pr in price:
        prices.append(pr.text)
    # print(nams)
    # print(prices

    zip1 = zip(nams, prices)
    zip2 = dict(zip(z, zip1))
    # dc=dict(zip2)

    djson = json.dumps(zip2, indent=4)
    #print(djson)
    data1["lol"].append(zip2)
    #print(json.dumps(data1, indent=4))
    #print(len(data1["lol"]))
    """for i in range(len(data1["lol"])):
        print(str(i) + ".index: " + str(data1["lol"][i]))
        for n in nams:
            if n in data1["lol"][i]:
                print("mevcut")
            else:
                print("yok")"""

    return data1["lol"][-1]
    print("**********")



urls = ["https://www.paththegame.com/oyunlar/league-of-legends/?sort=p.price&order=ASC",
        "https://www.paththegame.com/oyunlar/zula-altin/?sort=p.price&order=ASC",
        "https://www.paththegame.com/Hediye-Kartlar%C4%B1/Google-Play-Hediye-Kartlar%C4%B1/?sort=p.price&order=ASC"]

for url in urls:
    lol(url)

#print("======================")
#print(data1["lol"][-1])
"""for x in z:
    try:
        #print(data1["lol"][-1][x][0] + " : " +data1["lol"][-1][x][1])
    except KeyError:
        #print(x + "'e ait veri yok ")"""




def index(request):
    product=Products.objects.all()

    return render(request,"index.html",{"product":product})

def addProduct(request):
    form=ProductsForm(request.POST or None)
    if form.is_valid():
        product=form.save()
        return redirect("index")

def updateProduct(request,id):

    product = get_object_or_404(Products, id=id)
    pc=product.productCode
    print(pc)
    
    for pc in z:

        product.price = data1["lol"][-1][str(pc)][1]
        product.name = data1["lol"][-1][str(pc)][0]
        
        product.save()
        return redirect("index")


    return redirect("index")

def updateall(request):
    
    products=Products.objects.all()
    print(products)
    
    for product in products:
        pc=product.productCode
        product.price = data1["lol"][-1][str(pc)][1]
        product.name = data1["lol"][-1][str(pc)][0]
        
        product.save()
        return redirect("index")
        


    return render(request,"index.html")
    
    
