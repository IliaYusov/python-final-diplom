from django.urls import path, include
from django_rest_passwordreset.views import reset_password_request_token, reset_password_confirm

from backend.views import PartnerUpdate, RegisterAccount, LoginAccount, CategoryViewSet, ShopViewSet, ProductInfoView, \
    BasketView, AccountDetails, ContactView, OrderView, PartnerState, PartnerOrders, ConfirmAccount, \
    PasswordResetRequest, PasswordResetConfirm
from rest_framework.routers import DefaultRouter


router = DefaultRouter()
router.register('categories', CategoryViewSet, basename='categories')
router.register('shops', ShopViewSet, basename='shops')

app_name = 'backend'
urlpatterns = [
    path('partner/update', PartnerUpdate.as_view(), name='partner-update'),
    path('partner/state', PartnerState.as_view(), name='partner-state'),
    path('partner/orders', PartnerOrders.as_view(), name='partner-orders'),
    path('user/register', RegisterAccount.as_view(), name='user-register'),
    path('user/register/confirm', ConfirmAccount.as_view(), name='user-register-confirm'),
    path('user/details', AccountDetails.as_view(), name='user-details'),
    path('user/contact', ContactView.as_view(), name='user-contact'),
    path('user/login', LoginAccount.as_view(), name='user-login'),
    path('user/password_reset', PasswordResetRequest.as_view(), name='password-reset'),
    path('user/password_reset/confirm', PasswordResetConfirm.as_view(), name='password-reset-confirm'),
    path('products', ProductInfoView.as_view(), name='products'),
    path('basket', BasketView.as_view(), name='basket'),
    path('order', OrderView.as_view(), name='order'),
    path('', include(router.urls))
]
