from django.shortcuts import render
from django.conf import settings
from django.http import HttpResponseRedirect, HttpResponse

from .models import TutorDetails
from .forms import TutorDetailsForm

# Create your views here.
def tutor(request):
	form = TutorDetailsForm(request.POST or None)
	context = { "form" : form }
	if form.is_valid():
		form.save()
		return HttpResponseRedirect("/")
	return render(request, "tutor.html", context)


