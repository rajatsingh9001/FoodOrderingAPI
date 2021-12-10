from django.contrib import admin
from django.urls import path
from rest_framework.routers import SimpleRouter
from api.views import RestaurantDetailView, CustomerView, PartnerView, MenuItemsView, OrderView
from django.urls.conf import include


router = SimpleRouter()
router.register('restaurantdetail', RestaurantDetailView)
router.register('customer', CustomerView)
router.register('partner', PartnerView)
router.register('menuitems', MenuItemsView)
router.register('order', OrderView)
urlpatterns = [
    path('',include(router.urls)),
    
]