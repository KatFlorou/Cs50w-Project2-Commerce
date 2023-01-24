from django import forms
from .models import Listing, Watchlist, Comment, Bid


class NewListingForm(forms.ModelForm):
    class Meta:
        model = Listing
        fields = ['title', 'description', 'startingPrice', 'image', 'categoryname']

class Watchlist(forms.ModelForm):
    class Meta:
        model = Watchlist
        fields = ['person', 'items']

class ListingComments(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ['opinion']
        labels = {
            'opinion': ''   
        }

class ListingBid(forms.ModelForm):
    class Meta:
        model = Bid
        fields = ['bid']

    