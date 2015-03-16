from django.db import models

"""Auction:
	creator
	item name
	reserved price
	bidder = 'None'
	status = 'created'
	success = False
	begin_auction
	end_auction
	get_details"""


class Auction(models.Model):

    def __unicode__(self):
        return self.name

    owner = models.CharField(max_length=200)
    name = models.CharField(max_length=200)
    current_bidder = models.CharField(max_length=200)
    reserved_price = models.FloatField()
    current_price = models.FloatField()
    status = models.CharField(max_length=50)
    success = models.BooleanField(default=False)


class Bid(models.Model):
    def __unicode__(self):
        return self.id

    price = models.FloatField()
    name = models.CharField(max_length=200)
    item_id = models.ForeignKey(Auction)
"""class Item(models.Model):

    def __unicode__(self):
        return self.name

    name = models.CharField(max_length=200)
    reserved_price = models.DecimalField(max_digits=10, decimal_places=2)
    current_price = models.DecimalField(max_digits=10, default=0.00, decimal_places=2)
    status = models.BooleanField(default=True)


class User(models.Model):

    def __unicode__(self):
        return self.name

    name = models.CharField(max_length=200)
    email = models.EmailField()

class Bid(models.Model):

    def __unicode__(self):
        return self.item + self.user
    item = models.ForeignKey(Item)
    user = models.ForeignKey(User)
    bid_price = models.DecimalField(max_digits=10, decimal_places=2)
    """


