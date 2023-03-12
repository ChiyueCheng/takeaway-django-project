from django.contrib import admin

from takeaway.models import UserProfile, Food, Wallet, Order, Comment, Basket

# Register your models here.

admin.site.register(UserProfile)
admin.site.register(Food)
admin.site.register(Wallet)
admin.site.register(Order)
admin.site.register(Comment)
admin.site.register(Basket)
