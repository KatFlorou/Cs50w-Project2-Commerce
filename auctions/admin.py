from django.contrib import admin

from .models import Category, Listing, Watchlist, Comment, Bid

class FeedbackInline(admin.TabularInline):
    model = Listing.feedback.through
    extra = 0

class ItemsInline(admin.TabularInline):
    model = Watchlist.items.through
    extra = 0

class CurrentPriceInline(admin.TabularInline):
    model = Listing.currentPrice.through
    extra = 0

class WatchlistAdmin(admin.ModelAdmin):
    inlines = [
        ItemsInline,
    ]
    exclude = ('items',)

class CommentAdmin(admin.ModelAdmin):
    inlines = [
        FeedbackInline,
    ]

class BidAdmin(admin.ModelAdmin):
    inlines = [
        CurrentPriceInline
    ]
    list_display = ("id", "bider", "bid")

class ListingAdmin(admin.ModelAdmin):
    inlines = [
        FeedbackInline,
        CurrentPriceInline,
    ]
    exclude = ('feedback', 'currentPrice')
    list_filter = ('status', 'categoryname')

# Register your models here.
admin.site.register(Category)
admin.site.register(Listing, ListingAdmin)
admin.site.register(Watchlist, WatchlistAdmin)
admin.site.register(Comment)
admin.site.register(Bid, BidAdmin)
