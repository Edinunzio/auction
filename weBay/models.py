from django.db import models

class Item(models.Model):

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


