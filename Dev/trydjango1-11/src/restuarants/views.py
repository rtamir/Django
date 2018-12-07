import random
from django.http import HttpResponse
from django.shortcuts import render
from django.views import View
from django.views.generic import TemplateView

# Create your views here.
#fun based view

# def home_old(request):
# 	html_var = 'f strings'
# 	html_ = f"""<!DOCTYPE html>
# 	<html lang=en>
# 	<head>
# 	</head>
# 	<body>
# 	<h1>Hello</h1>
# 	<p>This is {html_var} page</p>
# 	</body>
# 	</html>
# 	"""
# 	return HttpResponse(html_)
# 	#return render(request,"home.html",{})#response

# def home(request):
# 	num = None
# 	some_list = [random.randint(0,1000000),random.randint(0,1000000), random.randint(0,1000000) ]
# 	cond_bool_itm = False
# 	if cond_bool_itm:
# 		num = random.randint(0,1000000)
# 	context = {
# 				"some_list": some_list,
# 				"num" : num}
# 	return render(request,"home.html",context)#response

# def about(request):

# 	context = {}
# 	return render(request,"about.html",context)#response

# def contact(request):
# 	context = {}
# 	return render(request,"contact.html",context)#response

# class ContactView(View):
# 	"""docstring for ContactView"""
# 	def get(self,request,*args,**kwargs):
# 		#print(kwargs)
# 		context={}
# 		return render(request,"contact.html",context)

# 	def post(self,request,*args,**kwargs):
# 		#print(kwargs)
# 		context={}
# 		return render(request,"contact.html",context)

# 	def put(self,request,*args,**kwargs):
# 		#print(kwargs)
# 		context={}
# 		return render(request,"contact.html",context)

# class ContactTemplateView(TemplateView):
# 	template_name = 'contact.html'

class HomeView(TemplateView):
	template_name = 'home.html'

	def get_context_data(self,*args,**kwargs):
		context = super(HomeView,self).get_context_data(*args,**kwargs)
		num = None
		some_list = [random.randint(0,1000000),random.randint(0,1000000), random.randint(0,1000000) ]
		cond_bool_itm = True
		if cond_bool_itm:
			num = random.randint(0,1000000)
		context = {
					"some_list": some_list,
					"num" : num}
		return(context)

# class AboutView(TemplateView):
# 	template_name = 'about.html'

# class ContactView(TemplateView):
# 	template_name = 'contact.html'
# 		