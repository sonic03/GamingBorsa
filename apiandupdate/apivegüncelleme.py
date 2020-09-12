import requests
from bs4 import BeautifulSoup as bs
import json
from products.models import Products
from django.shortcuts import render,redirect,get_object_or_404,reverse
import time
from fake_useragent import UserAgent
# Create your views here.




data1 = {"lol": []}
dataov=[]

nams = []
prices = []
namsoav = []
pricesoav = []
oavlist=[]
z = ["a9", "b17", "c13", "d6", "e1", "f1", "g15", "h8", "j19", "k4","l5","m6","n7","d8","c9"]
oavurun=["oavlolrp1","oavlolrp2","oavlolrp3","oavlolrp4","oavlolrp5","oavlolrp6","oavzula1","oavzula2","oavzula3","oavzula4","oavzula5","oavzula6"]


def lol():
    urls = ["https://www.paththegame.com/oyunlar/league-of-legends/?sort=p.price&order=ASC",
        "https://www.paththegame.com/oyunlar/zula-altin/?sort=p.price&order=ASC",
        "https://www.paththegame.com/Hediye-Kartlar%C4%B1/Google-Play-Hediye-Kartlar%C4%B1/?sort=p.price&order=ASC"]

    for url in urls:
    
    # id=["ptglol1","ptglol2","ptglol3","ptglol4"]
        ua=UserAgent()
        ua.random
        headers={"User-Agent":str(ua.random)}
        print(headers)
        r = requests.get(url,headers=headers)
        soup = bs(r.content, "lxml")
        i = 0
        names = soup.find_all("div", {"class": "name"})
        price = soup.find_all("span", {"class": "price-new"})

        for name in names:
            nams.append(name.text)

        for pr in price:
            prices.append(pr.text)
        print(nams)
        print(prices)

        zip1 = zip(nams, prices)
        zip2 = dict(zip(z, zip1))
        # dc=dict(zip2)

        djson = json.dumps(zip2, indent=4)
        #print(djson)
        
        data1["lol"].clear()
        data1["lol"].append(zip2)
        
        #print(json.dumps(data1, indent=4))
        print(len(data1["lol"]))
        

    print(data1["lol"])
    
    print("**********")
    time.sleep(3)
    nams.clear()
    prices.clear()

def oav():
    
    urls=["https://www.oyunalisveris.com/urun-kategorileri/tum-urunler?kategori=76&magaza=41",
    "https://www.oyunalisveris.com/urun-kategorileri/tum-urunler?kategori=129&magaza=41"]
    for url in urls:
        ua=UserAgent()
        ua.random
        headers={"User-Agent":str(ua.random)}
        print(headers)
        r = requests.get(url,headers=headers)
        soup = bs(r.content, "lxml")
        i = 0
        rps=soup.find_all("div",{"class":"col-xs-6 col-sm-4 col-md-3 col-lg-3"})
        for rp in rps:
            names = rp.find("p", {"class": "text-muted urunadi"})
            print(names.text)
            namsoav.append(names.text)
            price = rp.find("strong")
            print(names.text)
            pricesoav.append(price.text)

        """for name in names:
            nams.append(name.text)

        for pr in price:
            prices.append(pr.text)"""
        print(namsoav)
        print(pricesoav)

        zip3 = zip(namsoav, pricesoav)
        zip4 = dict(zip(oavurun, zip3))
        # dc=dict(zip2)

        djson1 = json.dumps(zip4, indent=4)
        #print(djson)
        oavlist.clear()
        oavlist.append(zip4)
        #print(json.dumps(data1, indent=4))
        print(len(oavlist))
        

    print(oavlist)
    
    print("**********")
    
    time.sleep(3)
    namsoav.clear()
    pricesoav.clear()







def updateall():
    
    products=Products.objects.all()
    print(products)
    print("_-_-_-_-_-_")
    print(data1["lol"])
    print("**********")
    print("-----oavlist---")
    print(oavlist)
    print("**********")
    for product in products:
        pc=product.productCode
        if "oav" in pc:
            product.price=oavlist[0][str(pc)][1]
            product.name=oavlist[0][str(pc)][0]
        else:

            product.price = data1["lol"][0][str(pc)][1]
            product.name = data1["lol"][0][str(pc)][0]
        
        product.save()
        
        


    return redirect("index")


