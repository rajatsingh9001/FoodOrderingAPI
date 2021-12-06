from django.contrib import admin
from django.urls import path
from api.views import CustomerView, RestaurantListView, RestaurantDetailView, LoginView, RestMenuItemsView
from api.views import  GetOtpView, VerifyOtpView
from rest_framework.routers import SimpleRouter
from django.urls.conf import include


router = SimpleRouter()
# router.register('items', MenuItemView)
router.register('customer', CustomerView)
router.register('restdetail', RestaurantDetailView)
# router.register('order', OrderView)
router.register('menuItems', RestMenuItemsView)
router.register('login', LoginView)

urlpatterns = [
    path('',include(router.urls)),
    path('restlist/', RestaurantListView.as_view()),
    path('getotp/', GetOtpView.as_view()),
    path('verifyotp/', VerifyOtpView.as_view()),
    
]
