from django.http import HttpResponse
from django.shortcuts import render
from django.views import View
import random
from django.views.generic import TemplateView
from .models import RestuarantLocation

def restuarant_listview(request):
	template_name = 'restuarants/restuarants_list.html'
	queryset = RestuarantLocation.objects.all()
	context = {
			"object_list":queryset
	}
	return render(request,template_name,context)


# Create your views here.
#function based view
# def home_old(request):
# 	html_var = 'f strings'
# 	html_ = f"""
# 	<!DOCTYPE html>
# 	<html lang="en">
# 	<head>
# 	<body>
# 	<h1>Hello World, Ravi Here</h1>
# 	<p>This is {html_var} coming</p>
# 	</body>
# 	</head>
# 	</html>
# 	"""
# 	#f strings --new to python 3.5
# 	return HttpResponse(html_)
# # 	#return render(request,"home.html",{})#response

# def home(request):
# 	num = random.randint(0,1000)
# 	some_list = [num,random.randint(0,1000),random.randint(0,1000) ]
# 	context = {"html_var":False,
# 				"num":num,
# 				"some_list":some_list
# 				}
# 	return render(request,"home.html",context)#response

# def about(request):
# 	context = {
# 				}
# 	return render(request,"about.html",context)#response

# def contact(request):
# 	context = {
# 				}
# 	return render(request,"contact.html",context)#response

# class ContactView(View):
# 	def get(self,request,*args,**kwargs):
# 		#print(kwargs)
# 		context= {}
# 		return render(request,"contact.html",context)
	
	# def post(self,request,*args,**kwargs):
	# 	#print(kwargs)
	# 	context= {}
	# 	return render(request,"contact.html",context)

	# def put(self,request,*args,**kwargs):
	# 	#print(kwargs)
	# 	context= {}
	# 	return render(request,"contact.html",context)
# class HomeView(TemplateView):
# 	template_name = 'home.html'

# 	def get_context_data(self, *args, **kwargs):
# 		context = super(HomeView,self).get_context_data(*args,**kwargs)
# 		num = random.randint(0,1000)
# 		some_list = [num,random.randint(0,1000),random.randint(0,1000) ]
# 		context = {"html_var":False,
# 				"num":num,
# 				"some_list":some_list
# 				}
# 		return context

# class AboutView(TemplateView):
# 	template_name = 'about.html'


# class ContactView(TemplateView):
# 	template_name = 'contact.html'