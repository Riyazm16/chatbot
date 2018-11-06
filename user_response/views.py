from django.shortcuts import render
from django.http import HttpResponseRedirect

from .forms import userResponseForm

from .models import User_data
# Create your views here.

def index(request):
	if request.method == 'POST':
		form = userResponseForm(request.POST)
		if form.is_valid():
			form.save()
			return render(request,'user_success.html')

	else:
		form = userResponseForm()

	return render(request,'user_response.html',{'form':form})
