from django.shortcuts import render
from ipware.utils import is_loopback_ip
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import *
import re
from datetime import datetime
import  json,requests
import ipware

# Create your views here.
@api_view(['GET'])
def get_laptop(request):
    laptops = LaptopModel.objects.all()
    res = []
    for laptop in laptops:
        imgs = PostImage.objects.all().filter(laptop=laptop)
        images = []
        base_url = request.build_absolute_uri('/')
        for img in imgs:
            img_url = base_url+"media/"+str(img.images)
            images.append(img_url)
        lap = {
            "id":laptop.id,
            "title":laptop.title,
            "brand":laptop.brand,
            "ram_type":laptop.ram_type,
            "ram_capacity":laptop.ram_capacity,
            "ssd_present":laptop.ssd_present,
            "ssd_capacity":laptop.ssd_capacity,
            "hdd_present":laptop.hdd_present,
            "hdd_capacity":laptop.hdd_capacity,
            "size":laptop.size,
            "weight":laptop.weight,
            "price":laptop.price,
            "imgs":images
        }
        res.append(lap)
    return Response({"data":res},status=200)

@api_view(['POST'])
def get_orders(request):
    data = request.data
    email = data.get("email","")
    res = []
    orders = OrderModel.objects.all().filter(user_email=email)
    for order in orders:
        print(order.get_status_display())
        laptop = order.laptop
        imgs = PostImage.objects.all().filter(laptop=laptop)
        images = []
        base_url = request.build_absolute_uri('/')
        for img in imgs:
            img_url = base_url+"media/"+str(img.images)
            images.append(img_url)
        lap = {
            "id":laptop.id,
            "title":laptop.title,
            "brand":laptop.brand,
            "ram_type":laptop.ram_type,
            "ram_capacity":laptop.ram_capacity,
            "ssd_present":laptop.ssd_present,
            "ssd_capacity":laptop.ssd_capacity,
            "hdd_present":laptop.hdd_present,
            "hdd_capacity":laptop.hdd_capacity,
            "size":laptop.size,
            "weight":laptop.weight,
            "price":laptop.price,
            "imgs":images
        }
        data = {
            "laptop":lap,
            "email":email,
            "status":order.get_status_display(),
            "start_date":order.start_date,
            "end_date":order.end_date,
            "total_price":order.total_price
        }
        res.append(data)
    return Response({"data":res},status=200)

@api_view(['POST'])
def create_orders(request):
    date_regex = "^\d{4}\-(0?[1-9]|1[012])\-(0?[1-9]|[12][0-9]|3[01])$"
    data = request.data
    email = data.get("email","")
    id = data.get("laptop_id",1)
    start_date = data.get("start_date","")
    end_date = data.get("end_date","")
    if(re.search(date_regex,start_date) and re.search(date_regex,end_date)):
        laptop =  LaptopModel.objects.all().filter(id=id).first()
        if laptop is not None :
            date_format = '%Y-%m-%d'
            a = datetime.strptime(start_date, date_format)
            b = datetime.strptime(end_date, date_format)
            day_diff = (b - a).days+1
            day_price = laptop.price
            total_cost = day_price*day_diff
            order = OrderModel(user_email=email,laptop=laptop,start_date=start_date,end_date=end_date,total_price=total_cost)
            order.save()
            return Response({"message":"order created"},status=200)
    return Response({"message":"invalid data"},status=400)

@api_view(["GET"])
def get_ip(request):
    client_ip,is_loopback = ipware.get_client_ip(request)
    if client_ip is None:
        client_ip = '3.110.151.86'
    else:
        if not is_loopback:
            client_ip = '3.110.151.86'
    auth = 'f585aa86ca221a53c310b5f80ac9f9a6'
    url = 'http://api.ipapi.com/api/{}?access_key={}'.format(client_ip,auth)
    response = requests.get(url)
    data = json.loads(response.text)
    print(data)
    result = {
        "ip":data.get("ip"),
        "country_name":data.get("country_name"),
        "city":data.get("city"),
        "zip":data.get("zip"),
        "lat":data.get("latitude"),
        "lon":data.get("longitude")
    }
    return Response(result,status=200)
