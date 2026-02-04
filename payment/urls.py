from django.urls import path
from .views import stripe_webhook, CreatePaymentIntent

urlpatterns = [
    path('create-payment/', CreatePaymentIntent.as_view()),
    path('stripe-webhook/', stripe_webhook),
]
