from django.shortcuts import render
from django.http import HttpResponse
from .models import *

def Home(request):
	return render(request,'simfood/home.html')	
def Contact(request):
	return render(request,'simfood/contact.html')
def About(request):
	return render(request,'simfood/about.html')

def Menu(request):
	menu2 = Allmenu.objects.all().order_by('id').reverse()
	context = {'menu':menu2}
	return render(request,'simfood/allmenu.html',context)

def MenuCategory(request,code):
	select = Category.objects.get(id=code)
	menu = Allmenu.objects.filter(catname=select).order_by('id').reverse()
	context = {'menu':menu,'catname': select.catname}
	return render(request,'simfood/allmenucat.html',context)


# register page
from django.contrib.auth.models import User
def Register(request):
	if request.method == 'POST':
		data  = request.POST.copy()
		first_name = data.get('first_name')
		number_phone = data.get('number_phone')
		email = data.get('email')
		password = data.get('password')
		# no try except, alert and reset password
		newuser = User()
		newuser.username = email
		newuser.first_name = first_name
		newuser.number_phone = number_phone
		newuser.email = email
		newuser.set_password(password)
		newuser.save()
	return render(request, 'simfood/register.html')

def AddtoCart(request,pid):
	print('CERRENT USER:', request.user)
	username = request.user.username
	user = User.objects.get(username=username)
	check = Allmenu.objects.get(id=pid)

	newcart = Cart()
	newcart.user = user
	newcart.productid = pid
	newcart.productname = check.name
	newcart.price = int(check.price)
	newcart.quantity = 1
	calculate = int(check.price)*1
	newcart.total = calculate
	newcart.save()
	return redirect('allmenu-page')