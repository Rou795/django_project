from django.shortcuts import render, redirect

from phones.models import Phone


def index(request):
    return redirect('catalog')


def show_catalog(request):
    command = request.GET.get('sort', None)
    template = 'catalog.html'
    phones = Phone.objects.all()
    if command == 'name':
        phones = sorted(phones, key=lambda x: x.name)
    elif command == 'min_price':
        phones = sorted(phones, key=lambda x: x.price)
    elif command == 'max_price':
        phones = sorted(phones, key=lambda x: x.price, reverse=True)
    context = {'phones': phones}
    return render(request, template, context)


def show_product(request, name_slug):
    template = 'product.html'
    phone = Phone.objects.filter(slug=name_slug)[0]
    context = {'phone': phone}
    return render(request, template, context)
