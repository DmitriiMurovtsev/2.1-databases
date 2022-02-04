from django.shortcuts import render, redirect
from phones.models import Phone


def index(request):
    return redirect('catalog')


def show_catalog(request):
    sort = request.GET.get('sort', 'no')
    pho = Phone.objects.all()
    phones = [{'name': c.name, 'price': c.price, 'slug': c.slug, 'image': c.image} for c in pho]
    if sort != 'no':
        if sort == 'min_price':
            phones_sort = sorted(phones, key=lambda k: k['price'])
        elif sort == 'max_price':
            phones_sort = sorted(phones, key=lambda k: k['price'], reverse=True)
        elif sort == 'name':
            phones_sort = sorted(phones, key=lambda k: k['name'])
        phones = phones_sort
    template = 'catalog.html'
    context = {'phones': phones}
    return render(request, template, context)


def show_product(request, slug):
    pho = Phone.objects.filter(slug=slug)
    phone = {}
    for c in pho:
        phone['name'] = c.name
        phone['image'] = c.image
        phone['price'] = c.price
        phone['release_date'] = c.release_date
        phone['lte_exists'] = c.lte_exists
    template = 'product.html'
    context = {'phone': phone}
    return render(request, template, context)
