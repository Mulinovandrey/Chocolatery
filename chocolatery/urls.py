
from django.urls import path
from .views import *

urlpatterns = [
    path('', index, name='home'),
    path('product/', view_product, name='view_product'),
    path('store/', view_store, name='view_store'),
    path('about/', view_about, name='view_about'),
    #path('', HomeNews.as_view(), name='home'),
    #path('category/<int:category_id>', get_category, name='category'),
    #path('category/<int:category_id>', NewsByCategory.as_view(), name='category'),
    #path('product/<int:product_id>/', view_product_id, name='view_product_id'),
    #path('news/<int:pk>/', ViewNews.as_view(), name='view_news'),
    #path('news/add-news/', add_news, name='add_news'),
    #path('news/add-news/', CreateNews.as_view(), name='add_news'),
]
