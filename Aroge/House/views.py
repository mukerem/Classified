from django.shortcuts import render
from House.models import House, Photo
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from .forms import HouseFilter
# Create your views here.
from random import random, randint  



def house_list(request):
    if request.method == "POST":
        form = HouseFilter(request.POST)
        if form.is_valid():
            location = request.POST.get('location')
            min_price = request.POST.get('min_price', None)
            max_price = request.POST.get('max_price', None)
            house_type = request.POST.get('house_type')

            house_list = house_filter(location, min_price, max_price, house_type)
        else:
            house_list = house_filter()

    else:
        form = HouseFilter()
        house_list = house_filter()

    for i in house_list:
        i.image = i.photo.all()[0].image
        # print(i.photo.all()[0].image)
    page_number = request.GET.get('page', 1)
    paginator = Paginator(house_list, 10) # Show 25 submits per page.

    try:
        house_list = paginator.page(page_number)
    except PageNotAnInteger:
        house_list = paginator.page(1)
    except EmptyPage:
        house_list = paginator.page(paginator.num_pages)

    context = {
        'house_list': house_list,
        'paginator': paginator,
        'form': form
    }
    return render(request, 'house_list.html', context)

def house_detail(request, house_id):
    try:
        house = House.objects.get(pk=house_id)
    except House.DoesNotExist:
        return render('house_list')
    return render(request, 'house_detail.html', {'house': house})



def house_filter(location=None, min_price=None, max_price=None, house_type=None):
    house_list = House.objects.all()
    if location:
        house_list = house_list.filter(location__region=location)
    
    if min_price:
        house_list = house_list.filter(price__gte=min_price)
    if max_price:
        house_list = house_list.filter(price__lte=max_price)

    if house_type:
        house_list = house_list.filter(sell_or_rent=house_type)

    return house_list