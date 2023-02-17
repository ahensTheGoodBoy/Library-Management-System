from django.urls import path
from .views import login_page, categorylist_page, add_category_page

urlpatterns = [
    path('', login_page, name="logIn"),
    path('categories/', categorylist_page, name="categorylist"),
    path('categories/add/', add_category_page, name="addcategory"),
]
