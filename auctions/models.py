from django.contrib.auth.models import AbstractUser
from djmoney.models.fields import MoneyField
from djmoney.models.validators import MinMoneyValidator
from django.db import models


class User(AbstractUser):
    pass

class Category(models.Model):
    categoryname = models.CharField(max_length=64)

    def __str__(self):
        return f"{self.categoryname}"

class Comment(models.Model):
    opinion = models.TextField(max_length=1000, default="", blank=False)
    person = models.ForeignKey(User, on_delete=models.CASCADE, blank=False)

    def __str__(self):
        return f"Comment No: {self.pk} Posted by: {self.person}"

class Bid(models.Model):
    bid = MoneyField("", max_digits=14, decimal_places=2, default_currency='USD')
    bider = models.ForeignKey(User, on_delete=models.CASCADE)
    
    def __str__(self):
            return f"{self.bid}"

class Listing(models.Model):
    BOOL_CHOICES = ((1, True), (0, False)) #Problem in the AdminSite
   
    title = models.CharField(max_length=100, blank=False, unique=True)
    description = models.TextField(max_length=1000, blank=False)
    startingPrice = MoneyField("Price", max_digits=14, decimal_places=2, default_currency='USD', validators=[MinMoneyValidator(1)])
    image = models.URLField("Image URL",blank=True)
    categoryname = models.ForeignKey(Category, on_delete=models.SET_NULL, null=True, blank=True, related_name="categorylisting", verbose_name="Category")
    creator = models.ForeignKey(User, on_delete=models.CASCADE)
    feedback = models.ManyToManyField(Comment, blank=True)
    currentPrice = models.ManyToManyField(Bid, related_name="latestBid",)
    status = models.BooleanField(default=True, choices=BOOL_CHOICES)

    def __str__(self):
        return f"{self.title}"


class Watchlist(models.Model):
    person = models.ForeignKey(User, on_delete=models.CASCADE, related_name="userWatchlist")
    items = models.ManyToManyField(Listing, blank=True)

    def __str__(self):
        return f"{self.person}"



