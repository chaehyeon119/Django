from django.shortcuts import render
from django.http import HttpRequest

# Create your views here.
from shop.models import Item


def index(request: HttpRequest):
    qs = Item.objects.all()
    return render(request, "shop/Item_list.html", {
        "Item_list": qs,
    })

def Item_detail(request: HttpRequest, pk: int):
    item = Item.objects.get(pk=pk)
    return render(request, "shop/Item_detail.html", {
        "item": item,
    })