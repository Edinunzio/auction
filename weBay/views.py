from django.shortcuts import render, HttpResponse, get_list_or_404, get_object_or_404
from models import Bid, Item, User
from forms import BidForm


def index(request):
    items = get_list_or_404(Item)
    return HttpResponse(items)

def item_detail(request, item_id):
    item = get_object_or_404(Item, pk=item_id)
    if request.method == 'POST':
        form = BidForm(request.POST)
        if form.is_valid():
            return HttpResponse('bid accepted!')
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