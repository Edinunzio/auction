from django.shortcuts import render, HttpResponse, get_list_or_404, get_object_or_404
from models import Auction
from forms import BidForm, AuctionForm


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
            a.current_bidder = ''
            a.save()
            return HttpResponse('Auction created!')
    else:
        a_form = AuctionForm()
        return render(request, 'new_auction.html', {'form': a_form})

def begin_auction(request, name):
    a = get_object_or_404(Auction, name=name)
    a.status = 'open'
    a.save()
    return HttpResponse('Auction started!')

def end_auction(request, name):
    a = get_object_or_404(Auction, name=name)
    if a.current_price > a.reserved_price:
        a.success = True
        a.status = "closed"
        a.save()
        return HttpResponse('Auction closed!')
    a.status = "closed"
    a.save()
    return HttpResponse('Auction closed!')

def update_auction(request, name):
    item = get_object_or_404(Auction, name=name)
    form = BidForm()
    if request.method == 'POST':
        form = BidForm(request.POST)
        if form.is_valid():
            form = form.process()
            if form['bid_price'] > item.current_price:
                # update bid for item
                item.current_price = form['bid_price']
                item.current_bidder = form['name']
                item.save()
                return HttpResponse('bid accepted!')
            else:
                return HttpResponse('bid rejected. aim higher')
    else:
        return render(request, 'detail.html', {'form': form, 'item': item})


def get_details(request, name):
    item = get_object_or_404(Auction, name=name)
    form = BidForm()
    if request.method == 'POST':
        form = BidForm(request.POST)
        if form.is_valid():
            form = form.process()
            if form['bid_price'] > item.current_price:
                # update bid for item
                item.current_price = form['bid_price']
                item.current_bidder = form['name']
                item.save()
                return HttpResponse('bid accepted!')
            else:
                return HttpResponse('bid rejected. aim higher')
    else:
        return render(request, 'detail.html', {'form': form, 'item': item})


def see_all(request):
    items = get_list_or_404(Auction)
    return render(request, 'list.html', {'items': items})
