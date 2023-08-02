from django.urls import path

from . import views

urlpatterns = [
    path('gtprods/<int:start>/<int:end>/', views.load_products, name="load_all_products"),
    path('gtprods/<int:start>/<int:end>/<int:page_id>', views.load_products, name="load_products"),
    path('gtdes/<int:start>/<int:end>', views.load_designs, name="load_design"),
    path('gtprodimgs/<int:product_id>', views.load_product_images, name="load_product_images"),
    path('gtimg/<int:image_id>', views.load_image, name="load_image"),
    path('gt404/', views.load_404, name="load_404"),
]