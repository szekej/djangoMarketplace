from django.shortcuts import render
from item.models import Item, Category


# Create your views here.

def index(request):
    items = Item.objects.filter(is_sold=False)[:6]  # first six elements
    categories = Category.objects.all()
    return render(request, 'index.html',
                  {
                      'categories': categories,
                      'items': items
                  })


def contact(request):
    return render(request, 'contact.html')
