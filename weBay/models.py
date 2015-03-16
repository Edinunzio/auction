from django.db import models


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
