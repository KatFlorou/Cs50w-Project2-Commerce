from django.contrib.auth import authenticate, login, logout
from django.db import IntegrityError
from django.http import HttpResponseRedirect
from django.shortcuts import render, redirect
from django.urls import reverse
from django.utils.translation import gettext_lazy as _

from .models import User, Category, Listing, Watchlist
from . import forms


def index(request):
    """
        Returns a page with the active listings.
    """
    
    listing = Listing.objects.filter(status=True).order_by('-pk')
    return render(request, "auctions/index.html", {
        "listings": listing
    })


def login_view(request):
    if request.method == "POST":

        # Attempt to sign user in
        username = request.POST["username"]
        password = request.POST["password"]
        user = authenticate(request, username=username, password=password)

        # Check if authentication successful
        if user is not None:
            login(request, user)
            return HttpResponseRedirect(reverse("index"))
        else:
            return render(request, "auctions/login.html", {
                "message": "Invalid username and/or password."
            })
    else:
        return render(request, "auctions/login.html")


def logout_view(request):
    logout(request)
    return HttpResponseRedirect(reverse("index"))


def register(request):
    if request.method == "POST":
        username = request.POST["username"]
        email = request.POST["email"]

        # Ensure password matches confirmation
        password = request.POST["password"]
        confirmation = request.POST["confirmation"]
        if password != confirmation:
            return render(request, "auctions/register.html", {
                "message": "Passwords must match."
            })

        # Attempt to create new user
        try:
            user = User.objects.create_user(username, email, password)
            user.save()
        except IntegrityError:
            return render(request, "auctions/register.html", {
                "message": "Username already taken."
            })
        login(request, user)
        return HttpResponseRedirect(reverse("index"))
    else:
        return render(request, "auctions/register.html")


    


def categories(request):
    """
        Returns a page with the list of all categories.
    """
    return render(request, "auctions/categories.html", {
        "categories": Category.objects.all(),
    })


def category_listings(request, title):
    """
        Returns a list of all active listings in a category.
    """
    thisCategory = Category.objects.get(categoryname=title)
    activeListings = thisCategory.categorylisting.filter(status=True).order_by('-pk')
    return render(request, "auctions/categ_list.html", {
        "title": title,
        "category_listings": activeListings
    })

def listing(request, title):
    """
        Returns the page of a listing.
        Possibility of adding listing in watchlist, biding and leaving a comment.
    """
    listing = Listing.objects.get(title=title) 
    lastbiding = listing.currentPrice.last()
    #Find last bider for listing and current_price
    lastbider = 0
    current_price = 0
    if lastbiding:
        lastbider = lastbiding.bider
        current_price = lastbiding.bid
    else:
        lastbider = 0 
        current_price = listing.startingPrice

    if request.method == "GET":
        form2 = forms.ListingComments
        form3 = forms.ListingBid
        watching = 0 
        #Find user watchlist
        if request.user.is_authenticated:
            if Watchlist.objects.filter(person=request.user).exists():
                userwatchlist = Watchlist.objects.get(person=request.user)
                watching = userwatchlist.items.all()
            else:
                watching = 0  
        return render(request, "auctions/listing.html", {
            "listing": listing,
            "current_price": current_price,
            "watching": watching,
            "form2": form2,
            "form3": form3,
            "comments": listing.feedback.all(),
            "lastbider": lastbider
        })

    if request.method == "POST":
        form2 = forms.ListingComments(request.POST)  
        form3 = forms.ListingBid(request.POST)      
        if form2.is_valid():      #Commenting
            new_opinion = form2.save(commit=False)
            new_opinion.person = request.user
            new_opinion.save()
            listing.feedback.add(new_opinion)
            return redirect("listing", listing.title)
        
        if form3.is_valid():  #Biding  
            bid_amount = form3.cleaned_data["bid"]
            if lastbiding:
                if bid_amount <= lastbiding.bid:
                    return render(request, "auctions/error.html", {
                    "message": "The amount you submitted is smaller than or equal to the item's Current Price"
                    })
                new_bid = form3.save(commit=False)
                new_bid.bider = request.user
                new_bid.save()
                listing.currentPrice.add(new_bid)
                return redirect("listing", listing.title)
            else:
                if bid_amount < listing.startingPrice:
                    return render(request, "auctions/error.html", {
                    "message": "The amount you submitted is smaller than the item's Current Price"
                    })
                new_bid = form3.save(commit=False)
                new_bid.bider = request.user
                new_bid.save()
                listing.currentPrice.add(new_bid)
                return redirect("listing", listing.title)
        
        statuschange = request.POST["closestatus"]
        print(statuschange)
        print(type(statuschange))
        if statuschange == 'False':
            listing.status = False
            listing.save()
            return redirect("listing", listing.title)
        else:
            return render(request, "auctions/error.html", {
                  "message": 'Please do not change the value of the button'
                })

        
def newlisting(request):
    """
        Creates a new listing.
    """
    if request.method == "GET":
        return render(request, "auctions/newlisting.html", {
            "form": forms.NewListingForm
        })

    if request.method == "POST":
        form = forms.NewListingForm(request.POST)
        if form.is_valid():
            new_listing = form.save(commit=False)
            new_listing.creator = request.user
            new_listing.save()
            return redirect(index)
        return render(request, "auctions/newlisting.html", {
            "form": form
        })


def watchlist(request):
    """
        Returns the page with the users watchlist.
        Adds an item to the users watchlist
    """
    if request.method == "GET":
        if Watchlist.objects.filter(person=request.user).exists():
            userIsWatching = Watchlist.objects.get(person=request.user)
            return render(request, "auctions/watchlist.html", {
                    "watchlist": userIsWatching.items.all()
                })
        else:
            return render(request, "auctions/watchlist.html")

    if request.method == "POST":
        form = request.POST
        givenid = form.get("item")
        action = form.get("action")
        # Check if Listing_pk is valid
        x = Listing.objects.values_list("pk")
        match = [i for i in x]
        if match:
            # Check if user has already a watchlist
            if Watchlist.objects.filter(person=request.user).exists():  # If user watchlist exists
                y = Watchlist.objects.get(person=request.user) # Take that user watchlist
                title = Listing.objects.get(pk=givenid)
                if action == "add": # If action is valid
                    y.items.add(givenid) # Add item to watchlist
                    return redirect(listing, title.title)
                elif action == "delete":
                    y.items.remove(givenid) # Delete item from watchlist
                    return redirect(listing, title.title)
                else: return render(request, "auctions/error.html", {
                    "message": "Action is not valid"
                    })
            else:
                if action == "add": # If action is valid
                    title = Listing.objects.get(pk=givenid)
                    y = Watchlist(person=request.user)
                    y.save()
                    y.items.add(givenid) # Save the new Watchlist
                    return redirect(listing, title.title)
                else:
                    return render(request, "auctions/error.html", {
                        "message": "Action is not valid"
                    }) 
        else:
            return render(request, "auctions/error.html", {
                "message": "Listing does not exist"
            })
       
        