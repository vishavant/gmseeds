from django.urls import path
from website import views

app_name = 'website'

urlpatterns = [
    path('', views.homepage, name='home'),
    path('index', views.index, name='index'),
    path('about', views.aboutus, name='about'),
    path('product', views.product, name='product'),
    path('contact', views.ContactUs.as_view(), name='contact'),
    path('thanks', views.ThankYou.as_view(), name='thanks')
]


