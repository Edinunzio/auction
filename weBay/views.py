from django.shortcuts import render, HttpResponse, get_list_or_404, get_object_or_404
from django.views.decorators.csrf import csrf_protect, ensure_csrf_cookie
from models import Auction, Bid
from forms import BidForm, AuctionForm
import decimal



def create_auction(request):

    a = Auction()
    if request.method == 'POST':
        a_form = AuctionForm(request.POST)
        if a_form.is_valid():
            form = a_form.process()
            a.owner = form['owner']
            a.name = form['name']
            a.reserved_price = form['reserved_price']
            a.current_price = 0.00
            a.success = False
            a.status = 'created'
            a.save()
            return HttpResponse(see_all(request))
            #return render(request, 'new_auction.html', {'form': a_form})
    else:
        a_form = AuctionForm()
        return render(request, 'new_auction.html', {'form': a_form})

def begin_auction(request):
    request.status = "open"
    pass

def end_auction(request):
    request.status = "closed"
    pass

def update_auction(request, id):
    item = get_object_or_404(Auction, pk=id)
    form = BidForm()
    if request.method == 'POST':
        form = BidForm(request.POST)
        if form.is_valid():
            if form.bid_price > id.current_price:
                # update bid for item
                id.current_price = form.bid_price
                return HttpResponse('bid accepted!')
            else:
                return HttpResponse('bid rejected. aim higher')
    else:
        form = BidForm()
        return render(request, 'detail.html', {'form': form, 'item': item})


def get_details(request, id):
    item = get_object_or_404(Auction, pk=id)
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

def see_all(request):
    #a = Auction
    items = get_list_or_404(Auction)
    return render(request, 'list.html', {'items': items})


"""class BidView():
    def post_bid(request, id):
        if request.method == 'POST':
            form = BidForm(request.POST)
            if form.is_valid():
                if form.bid_price > id.current_price:
                    # update bid for item
                    id.current_price = form.bid_price
                    return HttpResponse('bid accepted!')
                else:
                    return HttpResponse('bid rejected. aim higher')
        else:
            form = BidForm()
            return render(request, 'detail.html', {'form': form, 'item': item})

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
        form = BidForm()"""