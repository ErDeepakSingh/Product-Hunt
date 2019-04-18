from django.shortcuts import render,get_object_or_404
from django.contrib.auth.decorators import login_required
from . import models as product_models
# from django.utils import timezone


# Create your views here.
def products_home(request):
    return render(request,'products/products_home.html')


@login_required(login_url='login')
def create_product(request):
    if request.method=='POST':
        if request.POST['title'] and request.POST['body'] and request.FILES['image'] and request.FILES['icon'] and request.POST['url']:
            product=product_models.Product()
            product.title=request.POST['title']
            product.body=request.POST['body']
            product.image=request.FILES['image']
            product.icon=request.FILES['icon']
            if request.POST['url'].startswith("http://")or request.POST['url'].startswith("https://"):
                product.url=request.POST['url']
            else:
                product.url = "http://"+request.POST['url']
            # product.pub_date = timezone.datetime.now()
            product.hunter=request.user
            product.save()
            return render(request,'products/create_product.html')
        else:
            return render(request,'products/create_product.html',{'error':'Please fill all fields'})
    else:
        return render(request,'products/create_product.html')
def show_products(request):
    context={
        'products':product_models.Product.objects.all()
    }
    return render(request,'products/show_products.html',context)

def product_details(request,prod_id):
    context = {
        'product': get_object_or_404(product_models.Product,pk=prod_id)
        # 'product': product_models.Product.objects.get(id=prod_id)
    }
    return render(request,'products/product_details.html',context)