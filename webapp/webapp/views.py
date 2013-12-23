from django.shortcuts import render_to_response

from models import License
from forms import *

def home(request):
	"""
	home page
	"""

	licenses = License.objects.all()
	form = UserLicenseForm()
	if request.POST:
		form = UserLicenseForm(request.POST)
		if form.is_valid():
			form.save()
	return render_to_response('index.html', {'licenses': licenses, 'form': form})

#def create_license(request):
	#"""
	#create license view
	#"""

	#if request.POST:


	# license_selector = {'mit'}