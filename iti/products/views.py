from django.shortcuts import render , redirect
from django.http import HttpResponse
from products.models import Product 
from products.forms import ProductForm
from django.views.generic.edit import UpdateView , CreateView 
# Create your views here.
def productsindex(request):
       allproducts = [

              {"id":1,"name":"mobile","image":"product1.png"} ,
              {"id":2,"name":"laptop","image":"product2.png"} ,
              {"id":3,"name":"playstation","image":"product3.png"}
       ]
       #return HttpResponse ("This Is The Products Index")
       return render(request, "products/allproducts.html",context={"products":allproducts})

def index(request):
    products = Product.objects.all()
    return  render(request, "products/index.html", context={"products":products})

#show function


def show(request, id):
       product = Product.objects.get(pk=id)
       #return HttpResponse(product)
       #print(product.get_show_url())
       return  render(request, "products/show.html", context={"product":product})


#delete function
def delete(request, id):
       product = Product.objects.get(pk=id)
       product.delete()
       return redirect("/products")

#========Class_Based_View===========
class UpdateProductView(UpdateView):
    model = Product
    form_class = ProductForm
    template_name ='products/edit.html'
    success_url = "/products"

#=========Create_Based_View=========
class CreateProductView(CreateView):
    model = Product
    form_class = ProductForm
    template_name ='products/create.html'
    success_url = "/products"