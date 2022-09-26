from django.urls import path
from products.views import productsindex
from products.views import index ,show , delete , UpdateProductView , CreateProductView

urlpatterns = [

    path("all", productsindex, name="products.all"),
    path("", index, name="products.index"),
    path("<int:id>", show, name= "products.show"),
    path("delete/<id>", delete, name ='products.delete'),
    path("edit/<int:pk>", UpdateProductView.as_view(), name="products.edit"),
    path("create", CreateProductView.as_view(), name="products.create")

]