from django.shortcuts import render, get_object_or_404
from item.models import Item


# from .models import

# Create your views here.

def detail(request, pk):
    item = get_object_or_404(Item, pk=pk)
    related_items = Item.objects.filter(category=item.category, is_sold=False).exclude(pk=pk)[:3]

    return render(request, 'detail.html', context={
        'item': item,
        'related_item': related_items
    })