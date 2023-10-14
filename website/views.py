from django.shortcuts import render
from django.views.generic import TemplateView, CreateView
from .forms import ContactUsForm
from .models import Product
# Create your views here.


def homepage(request):
    return render(request, "website/homepage.html")


def index(request):
    return render(request, "website/index.html")


def aboutus(request):
    return render(request, "website/about_us.html")


class ContactUs(CreateView):
    form_class = ContactUsForm
    # print(ContactUsForm)
    template_name = "website/contact_us.html"
    success_url = 'thanks' 



def product(request):
    products = Product.objects.all()
    context = {
        'products': products
    }
    return render(request, "website/products.html", context)



class ThankYou(TemplateView):
    template_name = "website/thank_you.html" 


def product_detail(request):
    return render(request, "website/product_detail_page.html")