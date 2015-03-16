from django.shortcuts import render, HttpResponse, get_list_or_404, get_object_or_404
from models import Bid, Item, User, Auctions
from forms import BidForm, ItemForm, AuctionForm


def index(request):
    auctions = get_list_or_404(Auctions)
    #items = get_list_or_404(Item)
    return render(request, 'list.html', {'auctions': auctions})
    #return HttpResponse(items)

def item_detail(request, item_id):
    item = get_object_or_404(Item, pk=item_id)
    auctions = get_object_or_404(Auctions, pk=item_id)
    current_price = item.current_price
    if request.method == 'POST':
        form = BidForm(request.POST)
        if form.is_valid():
            if form.bid_price > item.current_price:
                # update bid for item
                return HttpResponse('bid accepted!')
            else:
                return HttpResponse('bid rejected. aim higher')
    else:
        form = BidForm()
        return render(request, 'detail.html', {'form': form, 'item': item})


def item_create(request):
    form = ItemForm(request.POST)
    if form.is_valid():
        return HttpResponse('Item created')


def begin_auction(request, item_id):
    form = AuctionForm(request.POST)
    item = get_object_or_404(Item, pk=item_id)
    auction = Auctions
    if form.is_valid():
        return HttpResponse('Auction begun!')

def end_auction(request):
    form = AuctionForm(request.POST)
    if form.is_valid():
        return HttpResponse('Auction over!')

def create_bid(request):
    if request.method == 'POST':
        form = BidForm(request.POST)
        if form.is_valid():
            return HttpResponse('bid accepted!')
    else:
        form = BidForm()
