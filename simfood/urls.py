from django.urls import path, include
from .views import *

urlpatterns = [
	path('', Home, name='home-page'),
	path('allmenu/', Menu, name='allmenu-page'),
	path('contact/', Contact, name='contact-page'),
	path('about/', About, name='about-page'),
	path('category/<int:code>/',MenuCategory,name='category-page'),
	path('register/', Register, name='register-page'),
	path('addtocart/<int:pid>/',AddtoCart,name='addtocart-page')

]