from django.shortcuts import render

# Create your views here.
def about(request):
	return render(request, 'about.html')

def faqs(request):
	return render(request, 'faqs.html')

def feedback(request):
	return render(request, 'feedback.html')

def help(request):
	return render(request, 'help.html')