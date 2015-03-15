from django.shortcuts import render, HttpResponse, get_list_or_404, get_object_or_404
from models import Bid, Item, User
from forms import BidForm


def index(request):
    items = get_list_or_404(Item)
    return render(request, 'list.html', {'items': items})
    #return HttpResponse(items)

def item_detail(request, item_id):
    item = get_object_or_404(Item, pk=item_id)
    current_price = item.current_price
    if request.method == 'POST':
        form = BidForm(request.POST)
        if form.is_valid():
            if form.bid_price > current_price:
                # update bid for item
                return HttpResponse('bid accepted!')
            else:
                return HttpResponse('bid rejected. aim higher')
    else:
        form = BidForm()
        return render(request, 'detail.html', {'form': form, 'item': item})

def get_bid(request):
    if request.method == 'POST':
        form = BidForm(request.POST)
        if form.is_valid():
            return HttpResponse('bid accepted!')
    else:
        form = BidForm()